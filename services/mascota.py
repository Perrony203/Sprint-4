from services.data import mascotas, dueños
from services.dueño import registrar_dueño
from models.mascota import Mascota
from models.dueño import Dueño
<<<<<<< HEAD
from util.exceptions import DuenoNoEncontradoError, EntradaInvalidaError
=======
from util.exceptions import DueñoNoEncontradoError, EntradaInvalidaError
from util.logger import log_info, log_warning, log_error
>>>>>>> 1b4e62e0900213d647b81137bbfd51b45a2b1fc3

def registrar_mascota(nombre = None):
    try:
<<<<<<< HEAD
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
    dueño_registro:Dueño = None    
    for dueño in dueños:
        if dueño.telefono == numero_dueño:
            dueño_registro = dueño
            break
=======
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
            if edad < 0:
                log_error(f"Intento de registrar edad negativa: {edad}")
                raise EntradaInvalidaError("edad", "La edad no puede ser negativa.")
        except ValueError:
            log_error("Intento de registrar edad con formato inválido")
            raise EntradaInvalidaError("edad", "Debe ser un número entero.")
        
        # Se solicita el numero del dueño
        numero_dueño = input("Ingrese el número de telefono del dueño: ")   

        #verificar si el dueño ya existe
        dueño_registro:Dueño = None    
        for dueño in dueños:
            if dueño.telefono == numero_dueño:
                dueño_registro = dueño
                log_info(f"Dueño encontrado: {dueño.nombre}")
                break
>>>>>>> 1b4e62e0900213d647b81137bbfd51b45a2b1fc3

        if dueño_registro is None:
            log_warning(f"Dueño no encontrado con teléfono: {numero_dueño}")
            print("===================================")
            print("Dueño no encontrado. Se procederá a registrar un nuevo dueño.")
            print("===================================")
            # Se registra un nuevo dueño
            dueño_registro = registrar_dueño(numero_dueño)

<<<<<<< HEAD
    mascota = Mascota(nombre, especie, raza, edad, dueño_registro)
    # Se agrega la mascota a la lista de mascotas
    mascotas.append(mascota)
    
    print("✅ Mascota registrada con éxito.")
=======
        mascota = Mascota(nombre, especie, raza, edad, dueño_registro)
        # Se agrega la mascota a la lista de mascotas
        mascotas.append(mascota)
        
        log_info(f"Mascota registrada exitosamente: {nombre} ({especie})")
        print("Mascota registrada con éxito.")
    except Exception as e:
        log_error(f"Error al registrar mascota: {str(e)}")
        raise
>>>>>>> 1b4e62e0900213d647b81137bbfd51b45a2b1fc3
    
def listar_mascotas():
    try:
        if len(mascotas) == 0:
            log_warning("Intento de listar mascotas cuando no hay ninguna registrada")
            print("No hay mascotas registradas.")
            return
        log_info(f"Listando {len(mascotas)} mascotas registradas")
        for mascota in mascotas:
            print(mascota.__str__())
            print("===================================")
    except Exception as e:
        log_error(f"Error al listar mascotas: {str(e)}")
        raise