import copy
import json
import os
import typing
import minecraft_launcher_lib
import minecraft_launcher_lib.helper
class MinecraftOptions(typing.TypedDict, total=False):
    username: str
    uuid: str
    token: str
    executablePath: str
    defaultExecutablePath: str
    jvmArguments: typing.List[str]
    launcherName: str
    launcherVersion: str
    gameDirectory: str
    demo: bool
    customResolution: bool
    resolutionWidth: str
    resolutionHeight: str
    server: str
    port: str
    nativesDirectory: str
    enableLoggingConfig: bool
    disableMultiplayer: bool
    disableChat: bool
def hx():
    print('游戏结束了')
def minecraft_command(version: str, minecraft_directory: typing.Union[str, os.PathLike], options: MinecraftOptions,what_run_minecraft:bool,_后续处理=hx) -> typing.List[str]:

    path = str(minecraft_directory)
    if not os.path.isdir(os.path.join(path, "versions", version)):
        raise minecraft_launcher_lib.command.VersionNotFound(version)
    options = copy.copy(options)
    with open(os.path.join(path, "versions", version, version + ".json")) as f:
        data = json.load(f)
    if "inheritsFrom" in data:
        data = minecraft_launcher_lib.helper.inherit_json(data, path)
    options["nativesDirectory"] = options.get("nativesDirectory", os.path.join(path, "versions", data["id"], "natives"))
    options["classpath"] = minecraft_launcher_lib.command.get_libraries(data, path)
    command = []
    # Add Java executable
    if "executablePath" in options:
        command.append(options["executablePath"])
    elif "javaVersion" in data:
        java_path = minecraft_launcher_lib.runtime.get_executable_path(data["javaVersion"]["component"], path)
        if java_path is None:
            command.append("java")
        else:
            command.append(java_path)
    else:
        command.append(options.get("defaultExecutablePath", "java"))
    if "jvmArguments" in options:
        command = command + options["jvmArguments"]
    # Newer Versions have jvmArguments in version.json
    if isinstance(data.get("arguments", None), dict):
        if "jvm" in data["arguments"]:
            command = command + minecraft_launcher_lib.command.get_arguments(data["arguments"]["jvm"], data, path, options)
        else:
            command.append("-Djava.library.path=" + options["nativesDirectory"])
            command.append("-cp")
            command.append(options["classpath"])
    else:
        command.append("-Djava.library.path=" + options["nativesDirectory"])
        command.append("-cp")
        command.append(options["classpath"])
    # The argument for the logger file
    if options.get("enableLoggingConfig", False):
        if "logging" in data:
            if len(data["logging"]) != 0:
                logger_file = os.path.join(path, "assets", "log_configs", data["logging"]["client"]["file"]["id"])
                command.append(data["logging"]["client"]["argument"].replace("${path}", logger_file))
    command.append(data["mainClass"])
    if "minecraftArguments" in data:
        # For older versions
        command = command + minecraft_launcher_lib.command.get_arguments_string(data, path, options)
    else:
        command = command + minecraft_launcher_lib.command.get_arguments(data["arguments"]["game"], data, path, options)
    if "server" in options:
        command.append("--server")
        command.append(options["server"])
        if "port" in options:
            command.append("--port")
            command.append(options["port"])
    if options.get("disableMultiplayer", False):
        command.append("--disableMultiplayer")
    if options.get("disableChat", False):
        command.append("--disableChat")
    
    if what_run_minecraft:
        import subprocess
        subprocess.run(command)
        _后续处理()
    else:
        return command
def download_game(version):
        current_max = 0

        # 这里定义了一个函数，获取当前的状态
        def set_status(status: str):
            print(status)

        # 这个函数获取了当前的进度
        def set_progress(progress: int):
            if current_max != 0:
                # 这条函数打印出了当前进度/最大值
                print(f"{progress}/{current_max}")

        # 这个函数获取了最大值
        def set_max(new_max: int):
            # 定义一个全局变量
            global current_max
            # 赋值
            current_max = new_max

        # 这个函数获取了默认的.minecraft文件夹路径

        # 这个dict设定了回调的内容，全部是刚才设定的函数
        callback = {
            "setStatus": set_status,
            "setProgress": set_progress,
            "setMax": set_max
        }
        minecraft_launcher_lib.install.install_minecraft_version(version,r'D:\mcl3\bbs',callback=callback)

