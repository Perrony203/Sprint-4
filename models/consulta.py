from models.mascota import Mascota
# Clase consulta
class Consulta:
    #Constructor
    def __init__(self, fecha: str, motivo: str, diagnostico: str, mascota: Mascota):
        self.fecha = fecha
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.mascota = mascota

    # Impresión de la información de una instancia consulta 
    def __str__(self):
        return f"\n Paciente:\n =================================== \n {self.mascota} \n =================================== \n Motivo: {self.motivo} \n Diagnóstico: {self.diagnostico} \n Fecha de revisión: {self.fecha}"

    # Devolución de la información de una instancia consulta a modo de diccionario 
    def to_dict(self):
        return {
            "mascota": self.mascota.to_dict(),
            "motivo": self.motivo,
            "diagnostico": self.diagnostico,
            "fecha": self.fecha
        }