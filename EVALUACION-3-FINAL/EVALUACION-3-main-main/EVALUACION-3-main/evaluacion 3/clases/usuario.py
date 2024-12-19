from datetime import datetime

class Usuario:
    def __init__(self, nombre_usuario, contrasena, tipo_usuario):
        self.nombre_usuario = nombre_usuario
        self.contrasena_hash = contrasena
        self.tipo_usuario = tipo_usuario
        self.fecha_creacion = datetime.now()

    def __str__(self):
        return f"Usuario: {self.nombre_usuario}, Tipo: {self.tipo_usuario}, Creado: {self.fecha_creacion}"
