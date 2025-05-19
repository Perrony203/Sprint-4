import logging
from datetime import datetime
from collections import deque
import codecs

class MemoryHandler(logging.Handler):
    def __init__(self, capacity=1000):
        super().__init__()
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def emit(self, record):
        self.buffer.append(self.format(record))

    def get_logs(self):
        return list(self.buffer)

# Configuración del logger
def setup_logger():
    # Crear el logger
    logger = logging.getLogger('clinica_veterinaria')
    logger.setLevel(logging.INFO)

    # Crear el manejador de archivo con codificación UTF-8
    file_handler = logging.FileHandler('clinica_veterinaria.log', encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    # Crear el manejador de memoria
    memory_handler = MemoryHandler()
    memory_handler.setLevel(logging.INFO)

    # Crear el formato del log
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    memory_handler.setFormatter(formatter)

    # Agregar los manejadores al logger
    logger.addHandler(file_handler)
    logger.addHandler(memory_handler)

    return logger, memory_handler

# Crear una instancia global del logger y su manejador de memoria
logger, memory_handler = setup_logger()

def log_info(message):
    """Registra un mensaje de nivel INFO"""
    logger.info(message)

def log_warning(message):
    """Registra un mensaje de nivel WARNING"""
    logger.warning(message)

def log_error(message):
    """Registra un mensaje de nivel ERROR"""
    logger.error(message)

def mostrar_logs():
    """Muestra todos los logs almacenados en memoria"""
    print("\n=== Registro de Actividad ===")
    for log in memory_handler.get_logs():
        print(log)
    print("===========================\n") 