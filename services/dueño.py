from models.dueño import Dueño
from services.data import dueños
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

    # Se crea una instancia de Dueño
    dueño = Dueño(nombre, telefono, direccion)

    # Se agrega el dueño a la lista de dueños
    dueños.append(dueño)

    print("Dueño registrado con éxito.")   
    return dueño