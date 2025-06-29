from models.consulta import Consulta
from models.mascota import Mascota
from database import mascota, consulta, dueño
from datetime import datetime
from util.exceptions import ConsultaNoEncontradaError, EntradaVaciaError, MascotaNoEncontradaError
from util.logger import log_info, log_warning, log_error


def registrar_consulta():    
    try:
        nombre_mascota = input("Ingrese el nombre de la mascota: ")
        motivo = input("Ingrese el motivo de la consulta: ")
        diagnostico = input("Ingrese el diagnóstico de la consulta: ")
        
        if nombre_mascota == "":
            log_error("Intento de registrar consulta con nombre de mascota vacío")
            raise EntradaVaciaError("nombre de la mascota")
        elif motivo == "":
            log_error("Intento de registrar consulta con motivo vacío")
            raise EntradaVaciaError("motivo de la consulta")
        elif diagnostico == "":
            log_error("Intento de registrar consulta con diagnóstico vacío")
            raise EntradaVaciaError("diagnóstico de la consulta")
        else:
            
            # Buscar la mascota en la lista de mascotas
            mascota_encontrada = mascota.consultar_mascota_por_nombre(nombre_mascota)
            
            if mascota_encontrada is None:                
                log_error(f"Error al registrar nueva mascota: {nombre_mascota}")
                raise MascotaNoEncontradaError(nombre_mascota)

            # Crear una nueva consulta
            consulta.insertar_consulta(motivo, diagnostico, nombre_mascota)
            log_info(f"Consulta registrada exitosamente para mascota: {nombre_mascota}")
            print("✅ Consulta registrada con éxito.")
    except Exception as e:
        log_error(f"Error al registrar consulta: {str(e)}")
        raise
    
def ver_historial():
    try:
        #ingreso del nombre de la mascota
        nombre_mascota = input("Ingrese el nombre de la mascota: ")

        if nombre_mascota == "":
            log_error("Intento de ver historial con nombre de mascota vacío")
            raise EntradaVaciaError("nombre de la mascota")
        else:
            # Buscar la mascota
            mascota_encontrada = None
            mascota_encontrada = mascota.consultar_mascota_por_nombre(nombre_mascota)
            
            if mascota_encontrada is None:
                log_error(f"Mascota no encontrada al intentar ver historial: {nombre_mascota}")
                raise MascotaNoEncontradaError(nombre_mascota)

            consultas_mascota = consulta.consultar_consultas_mascota(mascota_encontrada[0])
            if not consultas_mascota:
                log_warning(f"No se encontraron consultas para la mascota: {nombre_mascota}")
                raise ConsultaNoEncontradaError(nombre_mascota)
        
            log_info(f"Mostrando historial de consultas para mascota: {nombre_mascota}")
            print("===================================")
            print(f"Historial de consultas para {mascota_encontrada[1]}:")
            print("-----------------------------------")
            dueño_mascota = dueño.consultar_dueño_id(mascota_encontrada[5])
            print(f"Dueño: {dueño_mascota[1]}")
            print(f"Telefono: {dueño_mascota[2]}")
            print("-----------------------------------")
            # Mostrar el historial de consultas
            for consulta_find in consultas_mascota:                
                print(f"Fecha: {consulta_find[1]}, Motivo: {consulta_find[2]}, Diagnóstico: {consulta_find[3]}")
            print("===================================")

    except Exception as e:
        log_error(f"Error al ver historial de consultas: {str(e)}")
        raise