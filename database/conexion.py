import sqlite3

def conectar():
    conexion = sqlite3.connect('mascotasJJSCRIPT.db')
    return conexion

def crear_tablas():
    """Crea las tablas necesarias en la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()

    # Crear tabla de dueños
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dueños (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) NOT NULL,
            telefono VARCHAR(15) NOT NULL UNIQUE,
            direccion VARCHAR(100) NOT NULL
        )
    ''')
    
    # Crear tabla de mascotas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mascotas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) NOT NULL,
            especie VARCHAR(100) NOT NULL,
            raza VARCHAR(100) NOT NULL,
            edad INTEGER NOT NULL,
            dueño_id INTEGER,
            FOREIGN KEY (dueño_id) REFERENCES dueños (id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,                
            fecha DATETIME NOT NULL,                
            motivo TEXT NOT NULL,
            diagnostico TEXT NOT NULL,
            mascota_id INTEGER NOT NULL,
            FOREIGN KEY (mascota_id) REFERENCES mascotas (id)
        )
    ''')

    conexion.commit()
    print("Tablas creadas o verificadas correctamente.")
    conexion.close()