import requests

class JSONPlaceholderService:
    BASE_URL = "https://jsonplaceholder.typicode.com"

  
    def obtener_posts():
        response = requests.get(f"{JSONPlaceholderService.BASE_URL}/posts")
        return response.json() if response.status_code == 200 else []


    def obtener_comentarios():
        response = requests.get(f"{JSONPlaceholderService.BASE_URL}/comments")
        return response.json() if response.status_code == 200 else []

    
    def obtener_albums():
        response = requests.get(f"{JSONPlaceholderService.BASE_URL}/albums")
        return response.json() if response.status_code == 200 else []

    def obtener_fotos():
        response = requests.get(f"{JSONPlaceholderService.BASE_URL}/photos")
        return response.json() if response.status_code == 200 else []

    
    def obtener_tareas():
        response = requests.get(f"{JSONPlaceholderService.BASE_URL}/todos")
        return response.json() if response.status_code == 200 else []

    
    def obtener_usuarios():
        response = requests.get(f"{JSONPlaceholderService.BASE_URL}/users")
        return response.json() if response.status_code == 200 else []

    
    def crear_post(post_data):
        response = requests.post(f"{JSONPlaceholderService.BASE_URL}/posts", json=post_data)
        return response.json() if response.status_code == 201 else {"error": "No se pudo crear el post"}
 
 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///mi_base.db")
Session = sessionmaker(bind=engine)
session = Session()

def obtener_datos_api():
    print("\nSeleccione tipo de datos:")
    print("1. Posts")
    print("2. Comentarios")
    print("3. Álbumes")
    print("4. Fotos")
    print("5. Tareas")
    print("6. Usuarios")
    
    opcion = input("Elija una opción: ")
    
    datos_api = {
        '1': JSONPlaceholderService.obtener_posts,
        '2': JSONPlaceholderService.obtener_comentarios,
        '3': JSONPlaceholderService.obtener_albums,
        '4': JSONPlaceholderService.obtener_fotos,
        '5': JSONPlaceholderService.obtener_tareas,
        '6': JSONPlaceholderService.obtener_usuarios
    }
    
    if opcion in datos_api:
        datos = datos_api[opcion]()
        print(f"Se obtuvieron {len(datos)} registros")
    else:
        print("Opción inválida")

def enviar_datos_api():
    nuevo_post = {
        'title': input("Ingrese título del post: "),
        'body': input("Ingrese contenido del post: "),
        'userId': int(input("Ingrese ID de usuario: "))
    }
    
    respuesta = JSONPlaceholderService.crear_post(nuevo_post)
    print("Respuesta de la API:", respuesta)

if __name__ == "__main__":
    print("\nSeleccione una operación:")
    print("1. Obtener datos de la API")
    print("2. Enviar datos a la API")

    eleccion = input("Elija una opción: ")
    if eleccion == '1':
        obtener_datos_api()
    elif eleccion == '2':
        enviar_datos_api()
    else:
        print("Opción no válida")
