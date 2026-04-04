import json
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils import check_username, format_result, C


def banner():
    print(f"""
{C.CYAN}
  ██████╗  █████╗ ██████╗ ██╗  ██╗███████╗██╗███╗   ██╗██████╗ ███████╗██████╗
  ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
  ██║  ██║███████║██████╔╝█████╔╝ █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
  ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
  ██████╔╝██║  ██║██║  ██║██║  ██╗███████╗██║██║ ╚████║██████╔╝███████╗██║  ██║
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
{C.RESET}
{C.DIM}  OSINT Username Finder | by Yeiner Parra Rincón | Solo uso educativo y ético{C.RESET}
""")


def load_sites() -> dict:
    try:
        with open("sites.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{C.RED}[!] No se encontró sites.json{C.RESET}")
        exit(1)
    except json.JSONDecodeError:
        print(f"{C.RED}[!] sites.json tiene formato inválido{C.RESET}")
        exit(1)


def check_site(name: str, url: str, username: str) -> str:
    full_url = url.format(username)
    status = check_username(full_url)
    return format_result(name, full_url, status)


def buscar(username: str) -> None:
    sites = load_sites()
    total = len(sites)
    encontrados = 0

    print(f"{C.CYAN}[*] Buscando: {C.BOLD}{username}{C.RESET}")
    print(f"{C.DIM}[*] Revisando {total} sitios con 10 hilos paralelos...{C.RESET}\n")

    # as_completed → imprime resultados conforme van llegando (no espera al final)
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {
            executor.submit(check_site, name, url, username): name
            for name, url in sites.items()
        }

        for future in as_completed(futures):
            resultado = future.result()
            print(resultado)
            if "ENCONTRADO" in resultado:
                encontrados += 1

    print(f"\n{C.DIM}{'─' * 50}{C.RESET}")
    print(f"{C.CYAN}[*] Resultados: {C.GREEN}{encontrados} encontrados{C.RESET} de {total} sitios\n")


def main():
    parser = argparse.ArgumentParser(description="DarkFinder - OSINT Username Tool")
    parser.add_argument("-u", "--user", help="Username a buscar", metavar="USERNAME")
    args = parser.parse_args()

    banner()

    if args.user:
        buscar(args.user)
    else:
        username = input(f"{C.CYAN}  Username{C.RESET} » ").strip()
        if not username:
            print(f"{C.RED}[!] Debes ingresar un username{C.RESET}")
            exit(1)
        buscar(username)


if __name__ == "__main__":
    main()