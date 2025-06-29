from database import dueño
from util.exceptions import EntradaInvalidaError

# Función para registrar un nuevo dueño
def registrar_dueño(telefono: str):
    # Se solicita el nombre del dueño
    nombre = input("Ingrese el nombre del dueño: ")
    # Se solicita la direccion del dueño
    direccion = input("Ingrese la dirección del dueño: ")
    
    if nombre == "":    
        raise EntradaInvalidaError("nombre del dueño", "No puede estar vacío.")
    if telefono == "":
        raise EntradaInvalidaError("número de teléfono", "No puede estar vacío.")
    if direccion == "":
        raise EntradaInvalidaError("dirección", "No puede estar vacío.")

    dueño.insertar_dueño(nombre, telefono, direccion)

    print("Dueño registrado con éxito.")  
    