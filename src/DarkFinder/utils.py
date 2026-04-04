import requests

class C:
    GREEN  = "\033[92m"
    RED    = "\033[91m"
    CYAN   = "\033[96m"
    YELLOW = "\033[93m"
    RESET  = "\033[0m"
    DIM    = "\033[2m"
    BOLD   = "\033[1m"


# Sesión reutilizable para mejor rendimiento con hilos
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
})


def check_username(url: str) -> bool | None:
    try:
        r = session.get(url, timeout=7, allow_redirects=True)

        # 404 claro → no existe
        if r.status_code == 404:
            return False

        # Algunos sitios redirigen a /login o /home cuando no existe el user
        # Si la URL final es distinta a la que pedimos, probablemente no existe
        if r.url != url and any(x in r.url for x in ["/login", "/home", "/404", "/signup", "/register"]):
            return False

        if r.status_code == 200:
            # Palabras clave que indican que el usuario NO existe
            texto = r.text.lower()
            palabras_negativas = [
                "not found", "no existe", "user not found",
                "page not found", "doesn't exist", "no user",
                "perfil no encontrado", "cuenta no encontrada",
                "this account doesn't exist", "sorry, this page isn't available"
            ]
            if any(p in texto for p in palabras_negativas):
                return False
            return True

        # Otros códigos (403, 429, 500...) → error/indefinido
        return None

    except requests.exceptions.Timeout:
        return None
    except requests.exceptions.ConnectionError:
        return None
    except requests.RequestException:
        return None


def format_result(site: str, url: str, status: bool | None) -> str:
    if status is True:
        return f"{C.GREEN}{C.BOLD}[+] ENCONTRADO{C.RESET}  {site:<20} → {url}"
    elif status is False:
        return f"{C.RED}[-] No existe{C.RESET}   {site:<20}"
    else:
        return f"{C.YELLOW}[!] Error/timeout{C.RESET} {site:<20}"