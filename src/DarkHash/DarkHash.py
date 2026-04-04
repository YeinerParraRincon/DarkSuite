
"""
DarkHash — Herramienta educativa de cracking de hashes
by Yeiner Parra Rincón | WorldSkills 🥈 | SENA ADSO
Solo para uso ético y educativo.
"""

import hashlib
import sys
import os
import time
import argparse



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
    print(f"""
{C.PURPLE}{C.BOLD}
  ██████╗  █████╗ ██████╗ ██╗  ██╗██╗  ██╗ █████╗ ███████╗██╗  ██╗
  ██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██║  ██║██╔══██╗██╔════╝██║  ██║
  ██║  ██║███████║██████╔╝█████╔╝ ███████║███████║███████╗███████║
  ██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██║██╔══██║╚════██║██╔══██║
  ██████╔╝██║  ██║██║  ██║██║  ██╗██║  ██║██║  ██║███████║██║  ██║
  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{C.RESET}
{C.CYAN}  [ Hash Cracker — Herramienta Educativa de Ciberseguridad ]{C.RESET}
{C.DIM}  by Yeiner Parra Rincón | WorldSkills 🥈 | SENA ADSO{C.RESET}
{C.YELLOW}  ⚠️  Solo para uso ético y autorizado.{C.RESET}
""")



def detect_hash_type(hash_str: str) -> str:
    tipos = {
        32:  "MD5",
        40:  "SHA-1",
        56:  "SHA-224",
        64:  "SHA-256",
        96:  "SHA-384",
        128: "SHA-512",
    }
    return tipos.get(len(hash_str.strip()), "Desconocido")



def generar_hash(texto: str, algoritmo: str = "md5") -> str:
    algo = algoritmo.lower().replace("-", "")
    try:
        h = hashlib.new(algo)
        h.update(texto.encode("utf-8"))
        return h.hexdigest()
    except ValueError:
        print(f"{C.RED}[!] Algoritmo no soportado: {algoritmo}{C.RESET}")
        sys.exit(1)



def crackear_hash(target_hash: str, wordlist_path: str, algoritmo: str = "md5") -> None:
    target_hash = target_hash.strip().lower()
    detectado   = detect_hash_type(target_hash)

    print(f"\n{C.CYAN}[*] Hash objetivo  : {C.BOLD}{target_hash}{C.RESET}")
    print(f"{C.CYAN}[*] Tipo detectado : {C.BOLD}{detectado}{C.RESET}")
    print(f"{C.CYAN}[*] Algoritmo usado: {C.BOLD}{algoritmo.upper()}{C.RESET}")
    print(f"{C.CYAN}[*] Wordlist       : {C.BOLD}{wordlist_path}{C.RESET}\n")

    if not os.path.isfile(wordlist_path):
        print(f"{C.RED}[!] Wordlist no encontrada: {wordlist_path}{C.RESET}")
        sys.exit(1)

    inicio    = time.time()
    intentos  = 0
    encontrado = False

    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for linea in f:
                palabra = linea.strip()
                if not palabra:
                    continue

                intentos += 1
                candidato = generar_hash(palabra, algoritmo)

                if intentos % 10_000 == 0:
                    elapsed = time.time() - inicio
                    velocidad = intentos / elapsed if elapsed > 0 else 0
                    print(
                        f"{C.DIM}[~] Intentos: {intentos:,} | "
                        f"Velocidad: {velocidad:,.0f} h/s | "
                        f"Último: {palabra[:30]}{C.RESET}",
                        end="\r"
                    )

                if candidato == target_hash:
                    elapsed = time.time() - inicio
                    print(f"\n\n{C.GREEN}{C.BOLD}[✓] ¡HASH CRACKEADO!{C.RESET}")
                    print(f"{C.GREEN}    Hash     : {target_hash}{C.RESET}")
                    print(f"{C.GREEN}    Texto    : {C.BOLD}{palabra}{C.RESET}")
                    print(f"{C.GREEN}    Intentos : {intentos:,}{C.RESET}")
                    print(f"{C.GREEN}    Tiempo   : {elapsed:.3f}s{C.RESET}\n")
                    encontrado = True
                    break

    except KeyboardInterrupt:
        print(f"\n\n{C.YELLOW}[!] Interrumpido por el usuario.{C.RESET}")

    if not encontrado:
        elapsed = time.time() - inicio
        print(f"\n\n{C.RED}[-] Hash no encontrado en el diccionario.{C.RESET}")
        print(f"{C.DIM}    Intentos: {intentos:,} | Tiempo: {elapsed:.3f}s{C.RESET}\n")



def modo_interactivo():
    banner()
    print(f"{C.BOLD}¿Qué deseas hacer?{C.RESET}")
    print(f"  {C.CYAN}1{C.RESET}) Crackear un hash con wordlist")
    print(f"  {C.CYAN}2{C.RESET}) Generar un hash desde texto")
    print(f"  {C.CYAN}3{C.RESET}) Identificar tipo de hash")
    print(f"  {C.RED}0{C.RESET}) Salir\n")

    opcion = input(f"{C.PURPLE}darkhash{C.RESET} » ").strip()

    if opcion == "1":
        target = input(f"  {C.CYAN}[?]{C.RESET} Hash objetivo  : ").strip()
        wlist  = input(f"  {C.CYAN}[?]{C.RESET} Ruta wordlist  : ").strip()
        algo   = input(f"  {C.CYAN}[?]{C.RESET} Algoritmo [md5]: ").strip() or "md5"
        crackear_hash(target, wlist, algo)

    elif opcion == "2":
        texto = input(f"  {C.CYAN}[?]{C.RESET} Texto a hashear: ").strip()
        algo  = input(f"  {C.CYAN}[?]{C.RESET} Algoritmo [md5]: ").strip() or "md5"
        resultado = generar_hash(texto, algo)
        print(f"\n{C.GREEN}[+] {algo.upper()} de '{texto}':{C.RESET}")
        print(f"    {C.BOLD}{resultado}{C.RESET}\n")

    elif opcion == "3":
        h = input(f"  {C.CYAN}[?]{C.RESET} Hash a identificar: ").strip()
        tipo = detect_hash_type(h)
        print(f"\n{C.GREEN}[+] Tipo detectado: {C.BOLD}{tipo}{C.RESET} ({len(h)} caracteres)\n")

    elif opcion == "0":
        print(f"\n{C.DIM}  [~] Saliendo... hasta pronto.{C.RESET}\n")
        sys.exit(0)
    else:
        print(f"{C.RED}[!] Opción no válida.{C.RESET}")



def main():
    parser = argparse.ArgumentParser(
        description="DarkHash — Herramienta educativa de cracking de hashes",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-c", "--crack",    metavar="HASH",      help="Hash a crackear")
    parser.add_argument("-w", "--wordlist", metavar="WORDLIST",  help="Ruta al archivo wordlist")
    parser.add_argument("-g", "--generate", metavar="TEXTO",     help="Texto para generar hash")
    parser.add_argument("-a", "--algo",     metavar="ALGORITMO", help="Algoritmo: md5, sha1, sha256... (default: md5)", default="md5")
    parser.add_argument("-i", "--identify", metavar="HASH",      help="Identificar tipo de hash")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        modo_interactivo()
        return

    banner()

    if args.crack:
        if not args.wordlist:
            print(f"{C.RED}[!] Debes indicar una wordlist con -w{C.RESET}")
            sys.exit(1)
        crackear_hash(args.crack, args.wordlist, args.algo)

    elif args.generate:
        resultado = generar_hash(args.generate, args.algo)
        print(f"\n{C.GREEN}[+] {args.algo.upper()} de '{args.generate}':{C.RESET}")
        print(f"    {C.BOLD}{resultado}{C.RESET}\n")

    elif args.identify:
        tipo = detect_hash_type(args.identify)
        print(f"\n{C.GREEN}[+] Tipo detectado: {C.BOLD}{tipo}{C.RESET} ({len(args.identify)} caracteres)\n")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()