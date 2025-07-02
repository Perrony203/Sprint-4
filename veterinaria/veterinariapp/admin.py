from django.contrib import admin
from .models import Propietario, Mascota

# Registro de los modelos para que aparezcan en el panel de administración
admin.site.register(Propietario)
admin.site.register(Mascota)
