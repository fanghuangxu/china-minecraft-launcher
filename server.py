def downver(mc_dir,version):
    import json,requests
    with open(f'{mc_dir}\\versions\\{version}\\{version}.json','r') as json_file:
        server_url=json.loads(json_file.read())
    server_jar=requests.get(url=server_url)
    with open(f'{mc_dir}\\versions\\{version}\\{version}_server.jar','w') as file:
        file.write(str(server_jar))
    return 'exit'
