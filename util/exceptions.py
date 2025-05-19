class MascotaNoEncontradaError(Exception):
    def __init__(self, nombre):
        super().__init__(f"La mascota '{nombre}' no fue encontrada.")


class DuenoNoEncontradoError(Exception):
    def __init__(self, telefono):
        super().__init__(f"No se encontró dueño con el número {telefono}.")


class EntradaInvalidaError(Exception):
    def __init__(self, campo, mensaje_extra=""):
        mensaje = f"Entrada inválida para el campo '{campo}'."
        if mensaje_extra:
            mensaje += f" {mensaje_extra}"
        super().__init__(mensaje)


class ConsultaNoEncontradaError(Exception):
    def __init__(self, nombre_mascota):
        super().__init__(f"No hay consultas registradas para '{nombre_mascota}'.")

class EntradaVaciaError(Exception):
    def __init__(self, campo):
        super().__init__(f"El campo '{campo}' no puede estar vacío.")