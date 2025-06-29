from database import mascota, dueño
from util.exceptions import DuenoNoEncontradoError, EntradaInvalidaError
from services.DB.dueño import registrar_dueño

def registrar_mascota(nombre = None):
    if nombre is None:
        # Se solicita el nombre de la mascota
        nombre = input("Ingrese el nombre de la mascota: ")
    # Se solicita la especie de la mascota
    especie = input("Ingrese la especie de la mascota: ")
    # Se solicita la raza de la mascota
    raza = input("Ingrese la raza de la mascota: ")
    # Se solicita la edad de la mascota
    try:
        edad = int(input("Ingrese la edad de la mascota (en años): "))        
    except ValueError:
        raise EntradaInvalidaError("edad", "Debe ser un número entero.")
    
    if edad < 0:
        raise EntradaInvalidaError("edad", "La edad no puede ser negativa.")
        
    # Se solicita el numero del dueño
    numero_dueño = input("Ingrese el número de telefono del dueño: ")   

    if nombre == "":
        raise EntradaInvalidaError("nombre de la mascota", "No puede estar vacío.")
    if especie == "":
        raise EntradaInvalidaError("especie", "No puede estar vacío.")
    if raza == "":
        raise EntradaInvalidaError("raza", "No puede estar vacío.")
    if edad == "":
        raise EntradaInvalidaError("edad", "No puede estar vacío.")
    if numero_dueño == "":
        raise EntradaInvalidaError("número de teléfono", "No puede estar vacío.")

    #verificar si el dueño ya existe
    dueño_mascota = dueño.consultar_dueño(numero_dueño)
        
    if dueño_mascota is None:
        print("===================================")
        print("Dueño no encontrado. Registrelo antes de registrar la mascota.")
        print("===================================")
        registrar_dueño(numero_dueño)

    dueño_mascota = dueño.consultar_dueño(numero_dueño)
    mascota.insertar_mascota(nombre, especie, raza, edad, dueño_mascota[0])

    print("✅ Mascota registrada con éxito.")
    
def listar_mascotas():
    mascotas = mascota.consultar_mascotas()
    if len(mascotas) == 0:
        print("No hay mascotas registradas.")
        return
    
    for mascota_find in mascotas:
        print(f"ID: {mascota_find[0]}, Nombre: {mascota_find[1]}, Especie: {mascota_find[2]}, Raza: {mascota_find[3]}, Edad: {mascota_find[4]} años, Dueño: {dueño.consultar_dueño_id(mascota_find[5])[1]}")
    
    print("===================================")