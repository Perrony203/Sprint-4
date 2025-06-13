import csv
import json
from datetime import datetime
from models.mascota import Mascota
from models.dueño import Dueño
from models.consulta import Consulta
from util.logger import log_info, log_warning, log_error

def guardar_mascotas_dueños(mascotas, dueños):
    """Guarda la información de mascotas y dueños en un archivo CSV"""
    try:
        # Abrimos el archivo CSV en modo escritura con codificación UTF-8 para manejar caracteres especiales
        with open('mascotas_dueños.csv', 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)
            # Definimos las columnas del archivo CSV
            writer.writerow(['Tipo', 'Nombre', 'Especie', 'Raza', 'Edad', 'Nombre Dueño', 'Teléfono Dueño', 'Dirección'])
            
            # Guardamos primero todas las mascotas con la información de sus dueños
            for mascota in mascotas:
                writer.writerow([
                    'Mascota',
                    mascota.nombre,
                    mascota.especie,
                    mascota.raza,
                    mascota.edad,
                    mascota.dueño.nombre,
                    mascota.dueño.telefono,
                    mascota.dueño.direccion
                ])
            
            # Guardamos los dueños que no tienen mascotas registradas
            # Usamos un conjunto para identificar rápidamente los teléfonos de dueños con mascotas
            dueños_con_mascotas = {mascota.dueño.telefono for mascota in mascotas}
            for dueño in dueños:
                if dueño.telefono not in dueños_con_mascotas:
                    writer.writerow([
                        'Dueño',
                        '',  # nombre mascota (vacío porque es solo dueño)
                        '',  # especie (vacío porque es solo dueño)
                        '',  # raza (vacío porque es solo dueño)
                        '',  # edad (vacío porque es solo dueño)
                        dueño.nombre,
                        dueño.telefono,
                        dueño.direccion
                    ])
        
        log_info("Datos de mascotas y dueños guardados exitosamente en CSV")
    except Exception as e:
        log_error(f"Error al guardar datos en CSV: {str(e)}")
        raise

def cargar_mascotas_dueños():
    """Carga la información de mascotas y dueños desde el archivo CSV"""
    try:
        mascotas = []
        dueños = []
        # Usamos un diccionario para mantener referencia de dueños por teléfono
        # Esto evita duplicados y permite relacionar mascotas con sus dueños
        dueños_dict = {}

        with open('mascotas_dueños.csv', 'r', encoding='utf-8') as archivo:
            reader = csv.DictReader(archivo)
            for fila in reader:
                if fila['Tipo'] == 'Dueño':
                    # Creamos un nuevo dueño con la información del CSV
                    # Si no hay dirección, usamos 'No especificada' como valor por defecto
                    dueño = Dueño(fila['Nombre Dueño'], fila['Teléfono Dueño'], fila.get('Dirección', 'No especificada'))
                    dueños.append(dueño)
                    dueños_dict[fila['Teléfono Dueño']] = dueño
                elif fila['Tipo'] == 'Mascota':
                    # Buscamos el dueño por teléfono o lo creamos si no existe
                    telefono = fila['Teléfono Dueño']
                    if telefono not in dueños_dict:
                        dueño = Dueño(fila['Nombre Dueño'], telefono, fila.get('Dirección', 'No especificada'))
                        dueños.append(dueño)
                        dueños_dict[telefono] = dueño
                    else:
                        dueño = dueños_dict[telefono]
                    
                    # Creamos la mascota con su información y la relacionamos con su dueño
                    mascota = Mascota(
                        fila['Nombre'],
                        fila['Especie'],
                        fila['Raza'],
                        int(fila['Edad']),
                        dueño
                    )
                    mascotas.append(mascota)

        log_info("Datos de mascotas y dueños cargados exitosamente desde CSV")
        return mascotas, dueños
    except FileNotFoundError:
        log_warning("Archivo de mascotas y dueños no encontrado")
        return [], []
    except Exception as e:
        log_error(f"Error al cargar datos desde CSV: {str(e)}")
        raise

def guardar_consultas(consultas):
    """Guarda las consultas en un archivo JSON"""
    try:
        # Convertimos cada consulta a un diccionario con su información
        consultas_data = []
        for consulta in consultas:
            consulta_dict = {
                'fecha': consulta.fecha,
                'motivo': consulta.motivo,
                'diagnostico': consulta.diagnostico,
                'mascota': {
                    'nombre': consulta.mascota.nombre,
                    'especie': consulta.mascota.especie,
                    'raza': consulta.mascota.raza,
                    'edad': consulta.mascota.edad,
                    'dueño': {
                        'nombre': consulta.mascota.dueño.nombre,
                        'telefono': consulta.mascota.dueño.telefono
                    }
                }
            }
            consultas_data.append(consulta_dict)

        # Guardamos las consultas en formato JSON con indentación para mejor legibilidad
        with open('consultas.json', 'w', encoding='utf-8') as archivo:
            json.dump(consultas_data, archivo, indent=4, ensure_ascii=False)
        
        log_info("Consultas guardadas exitosamente en JSON")
    except Exception as e:
        log_error(f"Error al guardar consultas en JSON: {str(e)}")
        raise

def cargar_consultas(mascotas):
    """Carga las consultas desde el archivo JSON"""
    try:
        consultas = []
        with open('consultas.json', 'r', encoding='utf-8') as archivo:
            consultas_data = json.load(archivo)
            
            for consulta_dict in consultas_data:
                # Buscamos la mascota correspondiente a la consulta
                mascota_data = consulta_dict['mascota']
                mascota_encontrada = next(
                    (m for m in mascotas if m.nombre == mascota_data['nombre']),
                    None
                )
                
                if mascota_encontrada:
                    # Si encontramos la mascota, creamos la consulta
                    consulta = Consulta(
                        consulta_dict['fecha'],
                        consulta_dict['motivo'],
                        consulta_dict['diagnostico'],
                        mascota_encontrada
                    )
                    consultas.append(consulta)
                else:
                    # Si no encontramos la mascota, registramos una advertencia
                    log_warning(f"Mascota no encontrada para consulta: {mascota_data['nombre']}")

        log_info("Consultas cargadas exitosamente desde JSON")
        return consultas
    except FileNotFoundError:
        log_warning("Archivo de consultas no encontrado")
        return []
    except Exception as e:
        log_error(f"Error al cargar consultas desde JSON: {str(e)}")
        raise 