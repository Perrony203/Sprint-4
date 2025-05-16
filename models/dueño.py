# Clase dueño
class Dueño:
    # Constructor
    def __init__(self, nombre: str, telefono: str, direccion: str):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    # Impresión de la información de una instancia dueño 
    def __str__(self):
        return f"Nombre: {self.nombre}. \n Teléfono: {self.telefono} \n Dirección: {self.direccion}"

    # Devolución de la información de una instancia dueño a modo de diccionario 
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion
        }