import sqlite3

def conectar():
    conexion = sqlite3.connect('mascotasJJSCRIPT.db')
    return conexion

def consultar_dueño_id(id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM dueños WHERE id = ?", (str(id),))
    dueño = cursor.fetchone()
    conexion.close()

    return dueño

def consultar_dueño(telefono):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM dueños WHERE telefono = ?", (str(telefono),))
    dueño = cursor.fetchone()
    conexion.close()

    return dueño

def consultar_masctotas_dueño(nombre_dueño):
    conexion = conectar()
    cursor = conexion.cursor()
    
    cursor.execute("SELECT id FROM dueños WHERE nombre = ?", (nombre_dueño,))
    dueño = cursor.fetchone()
    
    if dueño is None:
        print(f"No se encontró un dueño con el nombre {nombre_dueño}.")
        conexion.close()
        return []

    cursor.execute("SELECT * FROM mascotas WHERE dueño_id = ?", (dueño[0],))
    mascotas = cursor.fetchall()

    conexion.close()

    return mascotas

def insertar_dueño(nombre, telefono, direccion):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO dueños (nombre, telefono, direccion) VALUES (?, ?, ?)", (nombre, telefono, direccion))
    conexion.commit()

    conexion.close()