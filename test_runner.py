import unittest
import sys
from datetime import datetime

# Códigos de colores ANSI
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ColoredTestRunner(unittest.TextTestRunner):
    """Runner personalizado con colores para las pruebas unitarias"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_time = None
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        self.error_tests = 0
        self.skipped_tests = 0

    def run(self, test):
        """Ejecuta las pruebas y muestra los resultados con colores"""
        self.start_time = datetime.now()
        self.total_tests = test.countTestCases()
        
        print(f"\n{Colors.HEADER}{Colors.BOLD}=== Iniciando Pruebas Unitarias ==={Colors.ENDC}")
        print(f"{Colors.BLUE}Total de pruebas a ejecutar: {self.total_tests}{Colors.ENDC}\n")
        
        result = super().run(test)
        
        # Calcular estadísticas
        self.passed_tests = self.total_tests - len(result.failures) - len(result.errors) - len(result.skipped)
        self.failed_tests = len(result.failures)
        self.error_tests = len(result.errors)
        self.skipped_tests = len(result.skipped)
        
        # Mostrar resumen
        self._print_summary(result)
        
        return result

    def _print_summary(self, result):
        """Imprime un resumen colorido de los resultados"""
        duration = datetime.now() - self.start_time
        
        print(f"\n{Colors.HEADER}{Colors.BOLD}=== Resumen de Pruebas ==={Colors.ENDC}")
        print(f"{Colors.GREEN}✓ Pruebas exitosas: {self.passed_tests}{Colors.ENDC}")
        print(f"{Colors.RED}✗ Pruebas fallidas: {self.failed_tests}{Colors.ENDC}")
        print(f"{Colors.YELLOW}! Pruebas con errores: {self.error_tests}{Colors.ENDC}")
        print(f"{Colors.BLUE}↷ Pruebas omitidas: {self.skipped_tests}{Colors.ENDC}")
        print(f"{Colors.BOLD}Tiempo total: {duration.total_seconds():.2f} segundos{Colors.ENDC}\n")
        
        # Mostrar detalles de fallos
        if result.failures:
            print(f"{Colors.RED}{Colors.BOLD}=== Detalles de Fallos ==={Colors.ENDC}")
            for failure in result.failures:
                print(f"{Colors.RED}✗ {failure[0]}{Colors.ENDC}")
                print(f"{Colors.YELLOW}{failure[1]}{Colors.ENDC}\n")
        
        # Mostrar detalles de errores
        if result.errors:
            print(f"{Colors.YELLOW}{Colors.BOLD}=== Detalles de Errores ==={Colors.ENDC}")
            for error in result.errors:
                print(f"{Colors.YELLOW}! {error[0]}{Colors.ENDC}")
                print(f"{Colors.YELLOW}{error[1]}{Colors.ENDC}\n")

def run_tests():
    """Función principal para ejecutar las pruebas"""
    # Descubrir y cargar todas las pruebas
    loader = unittest.TestLoader()
    start_dir = '.'
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Ejecutar las pruebas con el runner personalizado
    runner = ColoredTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    run_tests() 