import zipfile
import os
import shutil


def banner():
    green = "\033[92m"
    cyan = "\033[96m"
    yellow = "\033[93m"
    dim = "\033[2m"
    reset = "\033[0m"

    print(green + r"""
██████╗  █████╗ ██████╗ ██╗  ██╗███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
██║  ██║███████║██████╔╝█████╔╝ ███████╗█████╗  ███████║██████╔╝██║     ███████║
██║  ██║██╔══██║██╔══██╗██╔═██╗ ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
██████╔╝██║  ██║██║  ██║██║  ██╗███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝

        [ DarkSearch - File Malware Analyzer ]
""" + reset)

    print(cyan + "        Análisis de archivos comprimidos (.zip)" + reset)
    print(dim + "        by Yeiner Parra Rincón | SENA ADSO" + reset)
    print(yellow + "        ⚠️  Uso educativo y autorizado únicamente\n" + reset)



def analizar_archivo(ruta_zip):
    temporal_dir = "temp_extract"

    if not os.path.exists(temporal_dir):
        os.makedirs(temporal_dir)

    with zipfile.ZipFile(ruta_zip,'r') as zip_ref:
        zip_ref.extractall(temporal_dir)

    peligrosos = [".exe", ".bat", ".vbs", ".ps1"]
    sospechosos = ["powershell", "cmd.exe", "wget", "curl", "base64"]
    
    print("\n[*] Analizando Archivos...\n")

    for root, dirs, files in os.walk(temporal_dir):
        for file in files:
            ruta = os.path.join(root,file)

            print(f"[+] Revisando: {file}")

            if file.count(".") > 1:
                print(f"[!] Posible archivo camuflado: {file}")

            for ext in peligrosos:
                if file.lower().endswith(ext):
                    print(f"[!] Archivo Peligroso detectado: {file}")

            try:
                with open(ruta,"r",errors="ignore") as f:
                    contenido = f.read().lower()

                    for palabras in sospechosos:
                        if palabras in contenido:
                            print(f"[!] String Sospechoso '{palabras}' en {file}")
            
            except:
                pass


    print("\n[✓] Analisis Terminado")


    shutil.rmtree(temporal_dir)
    print("[*] Carpeta Temporal Eliminada")


if __name__ == "__main__":
    banner()
    archivo = input("Ingrese la ruta del archivo .zip: ")

    if not os.path.exists(archivo):
        print("[!] Archivo no existe")
        exit()

    if not archivo.endswith(".zip"):
        print("[!] El Archivo no es .zip")
        exit()

    analizar_archivo(archivo)