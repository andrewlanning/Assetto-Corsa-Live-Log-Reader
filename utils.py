import time
import datetime
import os
import glob

def find_log_file(server_log_path):
    while True:
        ftype = r'\*log'
        files = glob.glob(server_log_path+ftype)
        if str("output"+str(time.strftime("%Y%m%d_%H%M%S"))+".log") == str(os.path.basename(max(files, key=os.path.getctime))):
            return max(files, key=os.path.getctime)
        else:
            pass
                  
def follow(newest_file):
    newest_file.seek(0, os.SEEK_END)
    while True:
        line = newest_file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line