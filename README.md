# Proyecto Veterinaria

Este proyecto es una aplicación web desarrollada en Django para la gestión de una veterinaria. Permite registrar, consultar y editar información sobre propietarios, mascotas, bitácoras de consulta, medicamentos, cirugías y más.

## Requisitos previos
- Python 3.10 o superior
- pip
- (Opcional) Entorno virtual recomendado

## Instalación
1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Sprint-4
   ```
2. (Opcional) Crea y activa un entorno virtual:
   - **Windows (CMD):**
     ```cmd
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - **Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
3. Instala las dependencias:
   ```bash
   pip install -r veterinaria/requirements.txt
   ```

## Configuración
No se requiere configuración adicional para la base de datos, ya que se utiliza SQLite por defecto.

## Migraciones de la base de datos
Ejecuta las migraciones para preparar la base de datos:
```bash
cd veterinaria
python manage.py migrate
```

## Ejecución del servidor de desarrollo
Desde la carpeta `veterinaria`:
```bash
python manage.py runserver
```
Accede a la aplicación en [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Funcionalidades principales
- Registro, edición y consulta de propietarios
- Registro, edición y consulta de mascotas
- Registro y edición de bitácoras de consulta
- Registro de medicamentos y cirugías
- Panel de administración de Django

## Validación de funcionalidades
1. **Propietarios:**
   - Accede a la sección de propietarios para registrar, editar y consultar información.
2. **Mascotas:**
   - Registra nuevas mascotas y asócialas a propietarios existentes.
3. **Bitácoras:**
   - Crea y edita bitácoras de consulta para cada mascota.
4. **Medicamentos y cirugías:**
   - Añade medicamentos y cirugías desde sus respectivas secciones.
5. **Panel de administración:**
   - Accede a `/admin` con un superusuario para gestionar todos los modelos.

## Crear superusuario (opcional)
```bash
python manage.py createsuperuser
```

## Notas
- El archivo de base de datos SQLite se encuentra en `veterinaria/db.sqlite3`.
- Los archivos estáticos y plantillas están en `veterinaria/veterinariapp/static/` y `veterinaria/veterinariapp/templates/` respectivamente.

## Contacto
Para dudas o soporte, contacta al desarrollador del proyecto. 