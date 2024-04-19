import os

def clear_terminal():
    os.system('cls' if os.name=='nt' else 'clear')
def kill():
    os.system('taskkill /F /T /PID %i' % os.getpid())