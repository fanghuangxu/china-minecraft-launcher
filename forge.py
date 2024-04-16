def install_forge(version=str(),mc_dir=str(),callback=None):
    import minecraft_launcher_lib
    forge_version=minecraft_launcher_lib.forge.find_forge_version(vanilla_version=version)
    if not forge_version:
        class NotForgeVersion(Exception):
            def __init__(self,m):
                super().__init__(m)
        raise NotForgeVersion(f'没有支持原版：{version}的forge版本')
    if callback==None:
        minecraft_launcher_lib.forge.install_forge_version(path=mc_dir,versionid=forge_version)
    else:
        minecraft_launcher_lib.forge.install_forge_version(path=mc_dir,versionid=forge_version,callback=callback)

    
