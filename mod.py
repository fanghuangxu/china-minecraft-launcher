import minecraft_launcher_lib
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
print(minecraft_launcher_lib.forge.find_forge_version('1.18.2'))
#fabric-loader-0.15.10-1.16.4 
#minecraft_launcher_lib.forge.install_forge_version(path=r'D:\mcl3\bbs',versionid=minecraft_launcher_lib.forge.find_forge_version('1.18.2'),callback=callback)