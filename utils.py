import time
import os
import glob

def find_log_file(server_log_path):
    """ Returns the most recent server log file.
    
        Currently not functional if server is already running.
    """
    while True:
        ftype = r'\*log'
        files = glob.glob(server_log_path+ftype)
        if str("output"+time.strftime("%Y%m%d"+"_"+"%#H%M%S")+".log") == str(os.path.basename(max(files, key=os.path.getctime))):
            return max(files, key=os.path.getctime)
        elif str(time.strftime("%H")) == str('00'):
            if str("output"+time.strftime("%Y%m%d"+"_"+"%M%S")+".log") == str(os.path.basename(max(files, key=os.path.getctime))):
                return max(files, key=os.path.getctime)
        else:
            pass
                  
def follow(newest_file):
    """ Yields new lines in log file.
    """
    newest_file.seek(0, os.SEEK_END)
    while True:
        line = newest_file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line
