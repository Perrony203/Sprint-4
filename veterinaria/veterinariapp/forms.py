from django import forms
from .models import Propietario, Mascota, Cita

# Formulario para registrar propietarios usando el modelo Propietario
class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = ['nombre', 'telefono', 'email']

# Formulario para registrar mascotas usando el modelo Mascota
class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'edad', 'propietario']

# Formulario para registrar citas usando el modelo Cita
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['mascota', 'fecha_hora', 'motivo', 'notas']
        widgets = {
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        } 