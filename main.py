import utils

server_log_path = "E:\\SteamLibrary\\steamapps\\common\\assettocorsa\\server\\logs\\session"

utils.find_log_file(server_log_path)

for l in utils.follow(open(utils.find_log_file(server_log_path))):
    print(l)