from models.dueño import Dueño
# Clase mascota
class Mascota:
    #Constructor
    def __init__(self, nombre: str, especie: str, raza: str, edad: int, dueño: Dueño):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.dueño = dueño

    # Impresión de la información de una instancia mascota 
    def __str__(self):
        return f"\n Nombre: {self.nombre} \n Especie: {self.especie} \n Raza: {self.raza} \n Edad: {self.edad} años \n =================================== \nDueño: \n{self.dueño}\n"

    # Devolución de la información de una instancia mascota a modo de diccionario 
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "especie": self.especie,
            "raza": self.raza,
            "edad": self.edad,
            "dueño": self.dueño.to_dict()
        }