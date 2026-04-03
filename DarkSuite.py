import argparse
import subprocess
import os
import sys

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


def Banner_Map():
    print("""
\033[95m\033[1m
  ██████╗  █████╗ ██████╗ ██╗  ██╗███╗   ███╗ █████╗ ██████╗ 
  ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝████╗ ████║██╔══██╗██╔══██╗
  ██║  ██║███████║██████╔╝█████╔╝ ██╔████╔██║███████║██████╔╝
  ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██║╚██╔╝██║██╔══██║██╔═══╝ 
  ██████╔╝██║  ██║██║  ██║██║  ██╗██║ ╚═╝ ██║██║  ██║██║     
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
\033[0m
\033[96m  [ DarkMap — Port Scanner | Ethical Hacking Tool ]\033[0m
\033[2m  by Yeiner Parra Rincón | SENA ADSO\033[0m
\033[93m  ⚠️  Uso educativo y autorizado únicamente\033[0m
""")


parse = argparse.ArgumentParser(description="DarkSuite")


parse.add_argument("-m","--module",type=int,choices=[1,2,3],help="1 = DarkHash | 2 = DarkFinder | 3 = DarkMap")

arg = parse.parse_args()

banner()

ruta = os.path.join("src","DarkMap","DarkMap.py")

if arg.module == 1:
    print("DarkHash")
elif arg.module == 2:
    print("DarkFinder")
elif arg.module == 3:
    Banner_Map()
    ip = input("Ingrese la Ip del Objetivo: ")
    subprocess.run([sys.executable,ruta,"-i",ip])
else:
    print("Module Incorrect pls verify --module or -m ")