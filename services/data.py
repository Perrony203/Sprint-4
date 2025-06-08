from models.dueño import Dueño
from models.consulta import Consulta
from models.mascota import Mascota
from util.serializador import cargar_mascotas_dueños, cargar_consultas

# Base de datos temporal de los objetos requeridos para la aplicación
dueños: list[Dueño] = []
mascotas: list[Mascota] = []
consultas: list[Consulta] = []

# Cargar datos al inicio
mascotas, dueños = cargar_mascotas_dueños()
consultas = cargar_consultas(mascotas)