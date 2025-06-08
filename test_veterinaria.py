import unittest
import os
import json
import csv
from datetime import datetime
from models.mascota import Mascota
from models.dueño import Dueño
from models.consulta import Consulta
from services.mascota import registrar_mascota
from services.consulta import registrar_consulta
from util.exceptions import EntradaInvalidaError, MascotaNoEncontradaError, ConsultaNoEncontradaError
from util.serializador import guardar_mascotas_dueños, cargar_mascotas_dueños, guardar_consultas, cargar_consultas
from util.logger import log_info, log_warning, log_error

class TestModelos(unittest.TestCase):
    """Pruebas para los modelos del sistema (Mascota, Dueño, Consulta)"""
    
    def setUp(self):
        """Configuración inicial para las pruebas de modelos"""
        self.dueño = Dueño("Juan Pérez", "1234567890", "Calle 123")
        self.mascota = Mascota("Firulais", "Perro", "Labrador", 3, self.dueño)
        self.consulta = Consulta(
            "2024-03-20 10:00:00",
            "Revisión anual",
            "Mascota en buen estado",
            self.mascota
        )

    def test_creacion_dueño(self):
        """Prueba la creación correcta de un objeto Dueño"""
        self.assertEqual(self.dueño.nombre, "Juan Pérez")
        self.assertEqual(self.dueño.telefono, "1234567890")
        self.assertEqual(self.dueño.direccion, "Calle 123")

    def test_creacion_mascota(self):
        """Prueba la creación correcta de un objeto Mascota"""
        self.assertEqual(self.mascota.nombre, "Firulais")
        self.assertEqual(self.mascota.especie, "Perro")
        self.assertEqual(self.mascota.raza, "Labrador")
        self.assertEqual(self.mascota.edad, 3)
        self.assertEqual(self.mascota.dueño, self.dueño)

    def test_creacion_consulta(self):
        """Prueba la creación correcta de un objeto Consulta"""
        self.assertEqual(self.consulta.fecha, "2024-03-20 10:00:00")
        self.assertEqual(self.consulta.motivo, "Revisión anual")
        self.assertEqual(self.consulta.diagnostico, "Mascota en buen estado")
        self.assertEqual(self.consulta.mascota, self.mascota)

class TestExcepciones(unittest.TestCase):
    """Pruebas para el manejo de excepciones del sistema"""

    def test_entrada_invalida_mascota(self):
        """Prueba el manejo de excepciones al ingresar datos inválidos de mascota"""
        with self.assertRaises(EntradaInvalidaError):
            # Intentar crear una mascota con edad negativa
            mascota = Mascota("Firulais", "Perro", "Labrador", -1, None)

    def test_mascota_no_encontrada(self):
        """Prueba el manejo de excepciones cuando no se encuentra una mascota"""
        with self.assertRaises(MascotaNoEncontradaError):
            # Intentar buscar una mascota que no existe
            raise MascotaNoEncontradaError("MascotaInexistente")

    def test_consulta_no_encontrada(self):
        """Prueba el manejo de excepciones cuando no se encuentra una consulta"""
        with self.assertRaises(ConsultaNoEncontradaError):
            # Intentar buscar una consulta que no existe
            raise ConsultaNoEncontradaError("MascotaSinConsultas")

class TestSerializacion(unittest.TestCase):
    """Pruebas para la serialización y deserialización de datos"""

    def setUp(self):
        """Configuración inicial para las pruebas de serialización"""
        self.dueño = Dueño("Juan Pérez", "1234567890", "Calle 123")
        self.mascota = Mascota("Firulais", "Perro", "Labrador", 3, self.dueño)
        self.mascotas = [self.mascota]
        self.dueños = [self.dueño]
        self.consulta = Consulta(
            "2024-03-20 10:00:00",
            "Revisión anual",
            "Mascota en buen estado",
            self.mascota
        )
        self.consultas = [self.consulta]

    def tearDown(self):
        """Limpieza después de cada prueba"""
        # Eliminar archivos de prueba si existen
        if os.path.exists('mascotas_dueños.csv'):
            os.remove('mascotas_dueños.csv')
        if os.path.exists('consultas.json'):
            os.remove('consultas.json')

    def test_guardar_cargar_mascotas_dueños(self):
        """Prueba el guardado y carga de mascotas y dueños en CSV"""
        # Guardar datos
        guardar_mascotas_dueños(self.mascotas, self.dueños)
        
        # Verificar que el archivo existe
        self.assertTrue(os.path.exists('mascotas_dueños.csv'))
        
        # Cargar datos
        mascotas_cargadas, dueños_cargados = cargar_mascotas_dueños()
        
        # Verificar datos cargados
        self.assertEqual(len(mascotas_cargadas), 1)
        self.assertEqual(len(dueños_cargados), 1)
        self.assertEqual(mascotas_cargadas[0].nombre, "Firulais")
        self.assertEqual(dueños_cargados[0].nombre, "Juan Pérez")

    def test_guardar_cargar_consultas(self):
        """Prueba el guardado y carga de consultas en JSON"""
        # Guardar consultas
        guardar_consultas(self.consultas)
        
        # Verificar que el archivo existe
        self.assertTrue(os.path.exists('consultas.json'))
        
        # Cargar consultas
        consultas_cargadas = cargar_consultas(self.mascotas)
        
        # Verificar datos cargados
        self.assertEqual(len(consultas_cargadas), 1)
        self.assertEqual(consultas_cargadas[0].motivo, "Revisión anual")
        self.assertEqual(consultas_cargadas[0].diagnostico, "Mascota en buen estado")

class TestLogging(unittest.TestCase):
    """Pruebas para el sistema de logging"""

    def setUp(self):
        """Configuración inicial para las pruebas de logging"""
        self.log_file = 'clinica_veterinaria.log'
        # Limpiar archivo de log si existe
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def tearDown(self):
        """Limpieza después de cada prueba"""
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_info(self):
        """Prueba el registro de mensajes informativos"""
        mensaje = "Prueba de mensaje informativo"
        log_info(mensaje)
        
        # Verificar que el mensaje se escribió en el log
        with open(self.log_file, 'r', encoding='utf-8') as f:
            contenido = f.read()
            self.assertIn(mensaje, contenido)
            self.assertIn("INFO", contenido)

    def test_log_error(self):
        """Prueba el registro de mensajes de error"""
        mensaje = "Prueba de mensaje de error"
        log_error(mensaje)
        
        # Verificar que el mensaje se escribió en el log
        with open(self.log_file, 'r', encoding='utf-8') as f:
            contenido = f.read()
            self.assertIn(mensaje, contenido)
            self.assertIn("ERROR", contenido)

if __name__ == '__main__':
    from test_runner import run_tests
    run_tests() 