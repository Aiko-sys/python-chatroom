import os, datetime

from modules.exceptions import LogException
from modules.classes import keys

MAIN_PATH = os.getcwd()
logsPath = MAIN_PATH+"/logs"

class Logger():
    
    def __init__(self):
        pass


    def log(self, msg, level):
        qtty_logs = len(os.listdir(logsPath))

        if keys.logKey:
            
            if self.get_log_lenght(logsPath+f"/log{qtty_logs-1}.log") >= 200:
                log = open(logsPath+f"/log{qtty_logs}.log", "a")
            else:
                log = open(logsPath+f"/log{qtty_logs-1}.log", "a")

            with log:
                log.writelines(f"{datetime.datetime.now()} : [{level.upper()}] - {msg}\n")
            log.close()

    def get_log_lenght(self, path):
        countLines = 0
        with open(path, "r") as log:
            for l in log:
                countLines += 1
        return countLines

    