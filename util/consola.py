from services.mascota import registrar_mascota, listar_mascotas
from services.consulta import registrar_consulta, ver_historial

# Se insertan 100 saltos de línea en la consola 
def limpiar_pantalla():
    print("\n" * 100)

def pausar():
    print("===================================")
    input("Presione Enter para realizar una nueva operación...")

def menu_principal():
    while True:
        limpiar_pantalla()
        print("=== Clínica Veterinaria 'Amigos Peludos' ===")
        print("1. Registrar nueva mascota")
        print("2. Registrar nueva consulta")
        print("3. Listar todas las mascotas")
        print("4. Ver historial de consultas de una mascota")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_mascota()
        elif opcion == "2":
            registrar_consulta()
        elif opcion == "3":
            listar_mascotas()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            #Se rompe el ciclo principal de ejecución
            break
        else:
            print("Opción inválida.")
        
        pausar()