from django import forms
from .models import Propietario, Mascota, Cita, Cirugia, BitacoraConsulta, Medicamento, Veterinario

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

class BitacoraConsultaForm(forms.ModelForm):
    class Meta:
        model = BitacoraConsulta
        fields = ['mascota', 'observaciones', 'diagnostico', 'tratamiento', 'proxima_revision']
        widgets = {
            'proxima_revision': forms.DateInput(attrs={'type': 'date'}),
        }

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'descripcion', 'cantidad_disponible', 'fecha_vencimiento']
        widgets = {
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}),
        }

class CirugiaForm(forms.ModelForm):
    class Meta:
        model = Cirugia
        fields = ['mascota', 'veterinario', 'fecha', 'tipo', 'descripcion', 'estado']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class VeterinarioForm(forms.ModelForm):
    class Meta:
        model = Veterinario
        fields = ['nombre', 'apellido', 'especialidad', 'telefono', 'email']