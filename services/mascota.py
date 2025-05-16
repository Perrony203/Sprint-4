from services.data import mascotas, dueños
from services.dueño import registrar_dueño
from models.mascota import Mascota
from models.dueño import Dueño

def registrar_mascota(nombre = None):
    if nombre is None:
        # Se solicita el nombre de la mascota
        nombre = input("Ingrese el nombre de la mascota: ")
    # Se solicita la especie de la mascota
    especie = input("Ingrese la especie de la mascota: ")
    # Se solicita la raza de la mascota
    raza = input("Ingrese la raza de la mascota: ")
    # Se solicita la edad de la mascota
    edad = int(input("Ingrese la edad de la mascota (en años): "))
    
    # Se solicita el numero del dueño
    numero_dueño = input("Ingrese el número de telefono del dueño: ")   

    #verificar si el dueño ya existe
    dueño_registro:Dueño = None    
    for dueño in dueños:
        if dueño.telefono == numero_dueño:
            dueño_registro = dueño
            break

    if dueño_registro is None:
        print("===================================")
        print("Dueño no encontrado. Se procederá a registrar un nuevo dueño.")
        print("===================================")
        # Se registra un nuevo dueño
        dueño_registro = registrar_dueño(numero_dueño)

    mascota = Mascota(nombre, especie, raza, edad, dueño_registro)
    # Se agrega la mascota a la lista de mascotas
    mascotas.append(mascota)
    
    print("Mascota registrada con éxito.")
    
def listar_mascotas():
    if len(mascotas) == 0:
        print("No hay mascotas registradas.")
        return
    for mascota in mascotas:
        print(mascota.__str__())
        print("===================================")