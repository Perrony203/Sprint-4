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

class Cita(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='citas')
    fecha_hora = models.DateTimeField()
    motivo = models.CharField(max_length=200)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cita para {self.mascota.nombre} el {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}"
