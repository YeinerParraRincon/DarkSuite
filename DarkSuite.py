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


parse.add_argument("-m","--module",type=int,choices=[1,2,3,4],help="1 = DarkFinder | 2 = DarkHash | 3 = DarkMap | 4 = DarkSearch")

arg = parse.parse_args()

banner()

ruta_Map = os.path.join("src","DarkMap","DarkMap.py")

ruta_Hash = os.path.join("src","DarkHash","DarkHash.py")

ruta_finder = os.path.join("src","DarkFinder","DarkFinder.py")

ruta_search = os.path.join("src","DarkSearch","DarkSearch.py")

if arg.module == 1:
    subprocess.run([sys.executable,ruta_finder])
elif arg.module == 2:
    subprocess.run([sys.executable,ruta_Hash])
elif arg.module == 3:
    subprocess.run([sys.executable,ruta_Map])
elif arg.module == 4:
    subprocess.run([sys.executable,ruta_search])
else:
    print("Module Incorrect pls verify --module or -m ")