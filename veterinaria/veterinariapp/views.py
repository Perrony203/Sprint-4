from django.shortcuts import render, redirect
from .forms import PropietarioForm, MascotaForm

# Página principal de bienvenida
def landingView(request):
    return render(request, 'landing.html')

# Vista para registrar un nuevo propietario
def registrar_propietario(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_propietarios')  # Redirige al listado después de registrar
    else:
        form = PropietarioForm()
    return render(request, 'registrar_propietario.html', {'form': form})

# Vista para mostrar la lista de propietarios registrados
def lista_propietarios(request):
    from .models import Propietario
    propietarios = Propietario.objects.all()
    return render(request, 'lista_propietarios.html', {'propietarios': propietarios})

# Vista para registrar una nueva mascota
def registrar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')  # Redirige al listado después de registrar
    else:
        form = MascotaForm()
    return render(request, 'registrar_mascota.html', {'form': form})

# Vista para mostrar la lista de mascotas registradas
def lista_mascotas(request):
    from .models import Mascota
    mascotas = Mascota.objects.all()
    return render(request, 'lista_mascotas.html', {'mascotas': mascotas})