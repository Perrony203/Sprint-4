from django.db import models
from datetime import date

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

class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} - {self.especialidad}"
    
    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

class Medicamento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    cantidad_disponible = models.PositiveIntegerField()
    fecha_vencimiento = models.DateField()
    
    def __str__(self):
        return f"{self.nombre} - Stock: {self.cantidad_disponible}"
    
    @property
    def esta_vencido(self):
        return self.fecha_vencimiento < date.today()
    
    @property
    def stock_bajo(self):
        return self.cantidad_disponible < 10

class BitacoraConsulta(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='bitacoras')
    fecha_consulta = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    proxima_revision = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"Bitácora de {self.mascota.nombre} - {self.fecha_consulta.strftime('%d/%m/%Y %H:%M')}"
    
    class Meta:
        ordering = ['-fecha_consulta']

class Cirugia(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='cirugias')
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, related_name='cirugias')
    fecha = models.DateTimeField()
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.CharField(max_length=50, choices=[('Programada', 'Programada'), ('Realizada', 'Realizada'), ('Cancelada', 'Cancelada')], default='Programada')

    def __str__(self):
        return f"{self.tipo} para {self.mascota.nombre} el {self.fecha.strftime('%d/%m/%Y %H:%M')} ({self.estado})"