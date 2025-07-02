from django.db import models

# Modelo para almacenar información de los propietarios de mascotas
class Propietario(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del propietario
    telefono = models.CharField(max_length=20) # Teléfono de contacto
    email = models.EmailField()                # Correo electrónico

    def __str__(self):
        return self.nombre

# Modelo para almacenar información de las mascotas
class Mascota(models.Model):
    nombre = models.CharField(max_length=100)      # Nombre de la mascota
    especie = models.CharField(max_length=50)      # Especie (perro, gato, etc.)
    edad = models.PositiveIntegerField()           # Edad de la mascota
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='mascotas') # Relación con el propietario

    def __str__(self):
        return f"{self.nombre} ({self.especie})"
