import utils

server_log_path = "E:\\SteamLibrary\\steamapps\\common\\assettocorsa\\server\\logs\\session"

utils.find_log_file(server_log_path)

newest_file = open(utils.find_log_file(server_log_path))

for l in utils.follow(newest_file):
    print(l)