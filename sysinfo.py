import os
import socket


def show_sysinfo():
    print(f"Hostname : {socket.gethostname()}")
    print(f"User     : {os.getlogin()}")
    print(f"CWD      : {os.getcwd()}")
