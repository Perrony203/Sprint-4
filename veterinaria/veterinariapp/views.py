from django.shortcuts import render, redirect
from .forms import PropietarioForm, MascotaForm, CitaForm, MedicamentoForm
from .models import Cita

# Página principal de bienvenida
def landingView(request):
    return render(request, 'landing.html')

# Página de inicio/Sobre nosotros
def inicioView(request):
    return render(request, 'inicio.html')

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

def registrar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm()
    return render(request, 'registrar_cita.html', {'form': form})

def lista_citas(request):
    citas = Cita.objects.select_related('mascota', 'mascota__propietario').all().order_by('-fecha_hora')
    return render(request, 'lista_citas.html', {'citas': citas})

def lista_medicamentos(request):
    from .models import Medicamento
    medicamentos = Medicamento.objects.all()    
    return render(request, 'lista_medicamentos.html', {'medicamentos': medicamentos})

def agregar_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_medicamentos')
    else:
        form = MedicamentoForm()
    return render(request, 'agregar_medicamento.html', {'form': form})

def editar_medicamento(request, nombre):
    from .models import Medicamento
    medicamento = Medicamento.objects.get(nombre=nombre)
    
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('lista_medicamentos')
    else:
        form = MedicamentoForm(instance=medicamento)
    
    return render(request, 'editar_medicamento.html', {'form': form, 'medicamento': medicamento})

def eliminar_medicamento(request, nombre):
    from .models import Medicamento
    medicamento = Medicamento.objects.get(nombre=nombre)
    
    if medicamento:
        medicamento.delete()
        
    return redirect('lista_medicamentos')