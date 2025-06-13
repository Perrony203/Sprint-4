from services.mascota import registrar_mascota, listar_mascotas
from services.consulta import registrar_consulta, ver_historial
from services.data import mascotas, dueños, consultas
from util.logger import log_info, log_warning, log_error, mostrar_logs
from util.serializador import guardar_mascotas_dueños, guardar_consultas

# Se insertan 100 saltos de línea en la consola 
def limpiar_pantalla():
    print("\n" * 100)

def pausar():
    print("===================================")
    input("Presione Enter para realizar una nueva operación...")

def menu_principal():
    log_info("Iniciando aplicación de Clínica Veterinaria 'Amigos Peludos'")
    while True:
        limpiar_pantalla()
        print("=== Clínica Veterinaria 'Amigos Peludos' ===")
        print("1. Registrar nueva mascota")
        print("2. Registrar nueva consulta")
        print("3. Listar todas las mascotas")
        print("4. Ver historial de consultas de una mascota")
        print("5. Exportar datos actuales")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

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
                log_info("Usuario seleccionó: Exportar datos")
                guardar_mascotas_dueños(mascotas, dueños)
                guardar_consultas(consultas)
                print("✅ Datos exportados exitosamente")
            elif opcion == "6":
                log_info("Usuario seleccionó: Salir de la aplicación")
                # Guardar datos antes de salir
                guardar_mascotas_dueños(mascotas, dueños)
                guardar_consultas(consultas)
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