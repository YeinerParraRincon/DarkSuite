import argparse
import subprocess
import os
import sys


class C:
    PURPLE = "\033[95m"
    CYAN   = "\033[96m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"
    DIM    = "\033[2m"

def banner():
    green = "\033[92m"
    reset = "\033[0m"

    print(green + r"""
██████╗  █████╗ ██████╗ ██╗  ██╗███████╗██╗   ██╗██╗████████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██║   ██║██║╚══██╔══╝██╔════╝
██║  ██║███████║██████╔╝█████╔╝ ███████╗██║   ██║██║   ██║   █████╗  
██║  ██║██╔══██║██╔══██╗██╔═██╗ ╚════██║██║   ██║██║   ██║   ██╔══╝  
██████╔╝██║  ██║██║  ██║██║  ██╗███████║╚██████╔╝██║   ██║   ███████╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝

        [ DarkSuite - Python Cybersecurity Toolkit ]
        OSINT • Networking • Cracking
    """ + reset)





parse = argparse.ArgumentParser(description="DarkSuite")


parse.add_argument("-m","--module",type=int,choices=[1,2,3],help="1 = DarkHash | 2 = DarkFinder | 3 = DarkMap")

arg = parse.parse_args()

banner()

ruta_Map = os.path.join("src","DarkMap","DarkMap.py")

ruta_Hash = os.path.join("src","DarkHash","DarkHash.py")

if arg.module == 1:
    print("DarkHash")
elif arg.module == 2:
    subprocess.run([sys.executable,ruta_Hash])
elif arg.module == 3:
    subprocess.run([sys.executable,ruta_Map])
else:
    print("Module Incorrect pls verify --module or -m ")