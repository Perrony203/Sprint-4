import sqlite3

def conectar():
    conexion = sqlite3.connect('mascotasJJSCRIPT.db')
    return conexion

def consultar_mascotas():
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM mascotas as m INNER JOIN dueños as d ON m.dueño_id = d.id")
    mascotas = cursor.fetchall()
    conexion.close()

    return mascotas

def consultar_mascota_por_nombre(nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT * FROM mascotas WHERE nombre = ?", (nombre,))
    mascota = cursor.fetchone()
    
    conexion.close()
    
    return mascota

def insertar_mascota(nombre, especie, raza, edad, dueño):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM mascotas WHERE nombre = ?", (nombre,))
    mascota = cursor.fetchone()
    
    if mascota is None:
        cursor.execute("INSERT INTO mascotas (nombre, especie, raza, edad, dueño_id) VALUES (?, ?, ?, ?, ?)", (nombre, especie, raza, edad, dueño))
        conexion.commit()
    else: 
        print(f"La mascota con nombre {nombre} ya existe.")
    
    conexion.close()