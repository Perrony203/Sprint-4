from services.DB.mascota import registrar_mascota, listar_mascotas
from services.DB.consulta import registrar_consulta, ver_historial
from util.logger import log_info, log_warning, log_error, mostrar_logs
from database import conexion

# Se insertan 100 saltos de línea en la consola 
def limpiar_pantalla():
    print("\n" * 100)

def pausar():
    input("Presione Enter para realizar una nueva operación...")

def menu_principal():
    log_info("Iniciando aplicación de Clínica Veterinaria 'Amigos Peludos'")
    log_info("Iniciando aplicación de Clínica Veterinaria 'Amigos Peludos'")
    log_info("Conectando a la base de datos...")
    try:
        conexion.crear_tablas()
        log_info("Conexión a la base de datos establecida correctamente")
    except Exception as e:
        log_error(f"Error al conectar a la base de datos: {str(e)}")
        print("No se pudo conectar a la base de datos. Por favor, verifique la conexión.")
        return
    
    while True:
        limpiar_pantalla()
        print("=== Clínica Veterinaria 'Amigos Peludos' ===")
        print("1. Registrar nueva mascota")
        print("2. Registrar nueva consulta")
        print("3. Listar todas las mascotas")
        print("4. Ver historial de consultas de una mascota")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")
        print("===================================")
        
        try:
            if opcion == "1":
                log_info("Usuario seleccionó: Registrar nueva mascota")
                registrar_mascota()
            elif opcion == "2":
                log_info("Usuario seleccionó: Registrar nueva consulta")
                registrar_consulta()
            elif opcion == "3":
                log_info("Usuario seleccionó: Listar todas las mascotas")
                listar_mascotas()
            elif opcion == "4":
                log_info("Usuario seleccionó: Ver historial de consultas")
                ver_historial()
            elif opcion == "5":
                log_info("Usuario seleccionó: Salir de la aplicación")
                print("Gracias por usar la aplicación. ¡Hasta luego!")
                mostrar_logs()
                break
            else:
                log_warning(f"Opción inválida seleccionada: {opcion}")
                print("Opción inválida.")
        except Exception as e:
            log_error(f"Error en la operación: {str(e)}")
            print(f"Ha ocurrido un error: {str(e)}")
        
        pausar()
    
    log_info("Aplicación finalizada correctamente") 