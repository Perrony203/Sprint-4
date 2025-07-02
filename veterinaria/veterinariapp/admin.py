from django.contrib import admin
from .models import Propietario, Mascota, Cita, Veterinario, Medicamento, BitacoraConsulta, Cirugia

# Registro de los modelos para que aparezcan en el panel de administración
admin.site.register(Propietario)
admin.site.register(Mascota)
admin.site.register(Cita)
admin.site.register(Veterinario)
admin.site.register(Medicamento)
admin.site.register(BitacoraConsulta)
admin.site.register(Cirugia)
