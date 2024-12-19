import requests
from auxiliares.constantes import URL_API

def obtener_datos(tipo):
    try:
        response = requests.get(f"{URL_API}/{tipo}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

def enviar_datos(tipo, datos):
    try:
        response = requests.post(f"{URL_API}/{tipo}", json=datos)
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

def actualizar_datos(tipo, datos):
    try:
        response = requests.put(f"{URL_API}/{tipo}", json=datos)
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

def eliminar_datos(tipo, id_dato):
    try:
        response = requests.delete(f"{URL_API}/{tipo}/{id_dato}")
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
