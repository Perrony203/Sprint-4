from django import forms
from .models import Propietario, Mascota

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