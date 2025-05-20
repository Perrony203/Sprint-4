from models.consulta import Consulta
from models.mascota import Mascota
from services.data import mascotas, consultas, dueños
from services.mascota import registrar_mascota
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
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Buscar la mascota en la lista de mascotas
            mascota_encontrada = next((m for m in mascotas if m.nombre == nombre_mascota), None)
            
            if mascota_encontrada is None:
                log_warning(f"Mascota no encontrada: {nombre_mascota}")
                print("===================================")
                print("Mascota no encontrada. Se procederá a registrar una nueva mascota.")
                print("===================================")
                registrar_mascota(nombre_mascota)
                # Buscar nuevamente la mascota después de registrar
                mascota_encontrada = next((m for m in mascotas if m.nombre == nombre_mascota), None)
                if mascota_encontrada is None:
                    log_error(f"Error al registrar nueva mascota: {nombre_mascota}")
                    raise MascotaNoEncontradaError(nombre_mascota)
            
            # Crear una nueva consulta
            consulta = Consulta(fecha, motivo, diagnostico, mascota_encontrada)
            consultas.append(consulta)
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
            mascota_encontrada = next((m for m in mascotas if m.nombre == nombre_mascota), None)

            if mascota_encontrada is None:
                log_error(f"Mascota no encontrada al intentar ver historial: {nombre_mascota}")
                raise MascotaNoEncontradaError(nombre_mascota)

            consultas_mascota = [consulta for consulta in consultas if consulta.mascota == mascota_encontrada]
            if not consultas_mascota:
                log_warning(f"No se encontraron consultas para la mascota: {nombre_mascota}")
                raise ConsultaNoEncontradaError(nombre_mascota)
        
            log_info(f"Mostrando historial de consultas para mascota: {nombre_mascota}")
            print(f"Historial de consultas para {mascota_encontrada.nombre}:")
            # Mostrar el historial de consultas
            for consulta in consultas_mascota:
                print(consulta.__str__())
    except Exception as e:
        log_error(f"Error al ver historial de consultas: {str(e)}")
        raise