class MascotaNoEncontradaError(Exception):
    def __init__(self, nombre):
        print(f"La mascota '{nombre}' no fue encontrada.")


class DueñoNoEncontradoError(Exception):
    def __init__(self, telefono):
        print(f"No se encontró dueño con el número {telefono}.")


class EntradaInvalidaError(Exception):
    def __init__(self, campo, mensaje_extra=""):
        mensaje = f"Entrada inválida para el campo '{campo}'."
        if mensaje_extra:
            mensaje += f" {mensaje_extra}"
        print(mensaje)


class ConsultaNoEncontradaError(Exception):
    def __init__(self, nombre_mascota):
        print(f"No hay consultas registradas para '{nombre_mascota}'.")
