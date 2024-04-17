def download_game(mc_dir,version,callback):
        import minecraft_launcher_lib
        minecraft_launcher_lib.install.install_minecraft_version(version,mc_dir,callback=callback)

