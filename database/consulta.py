from datetime import datetime
import sqlite3

def conectar():
    conexion = sqlite3.connect('mascotasJJSCRIPT.db')
    return conexion

def consultar_consultas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM consultas")
    consultas = cursor.fetchall()
    
    conexion.close()

    return consultas

def consultar_consultas_mascota(mascota_id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM consultas WHERE mascota_id = ?", (mascota_id,))
    consultas = cursor.fetchall()
    
    conexion.close()

    return consultas

def insertar_consulta(motivo, diagnostico, nombre_mascota):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM mascotas WHERE nombre = ?", (nombre_mascota,))
    mascota = cursor.fetchone()

    if mascota is None:
        print(f"No se encontró una mascota con el nombre {nombre_mascota}.")
        conexion.close()
        return

    cursor.execute("INSERT INTO consultas (fecha, motivo, diagnostico, mascota_id) VALUES (?, ?, ?, ?)", (datetime.now(), motivo, diagnostico, mascota[0]))
    conexion.commit()

    conexion.close() 
