from services.mascota import registrar_mascota, listar_mascotas
from services.consulta import registrar_consulta, ver_historial
import os
from util.exceptions import *

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
        
        try:
            if opcion == "1":
                print("\n======== Registro de mascota ========\n")
                registrar_mascota()
            elif opcion == "2":
                print("\n\n ======== Registro de consulta ========\n")
                registrar_consulta()
            elif opcion == "3":
                print("\n\n ======== Mascotas registradas ========\n")
                listar_mascotas()
            elif opcion == "4":
                print("\n\n ======== Consultas ========\n")
                ver_historial()
            elif opcion == "5":
                print("\n Gracias por usar la aplicación. ¡Hasta luego!")
                break
            else:
                raise EntradaInvalidaError("menú", "La opción ingresada no es válida.")
        except (MascotaNoEncontradaError, DuenoNoEncontradoError,
                EntradaInvalidaError, ConsultaNoEncontradaError,
                EntradaVaciaError) as e:
            print(f"⚠️  {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

        pausar()


# Se insertan 100 saltos de línea en la consola 
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    print("===================================")
    input("Presione Enter para realizar una nueva operación...")

