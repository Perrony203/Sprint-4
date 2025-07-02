from django.shortcuts import render, redirect, get_object_or_404
from .forms import PropietarioForm, MascotaForm, CitaForm, CirugiaForm, VeterinarioForm, MedicamentoForm, BitacoraConsultaForm
from .models import Cita, Cirugia, Mascota, BitacoraConsulta, Medicamento, Veterinario
import csv
from django.http import HttpResponse
import io
import zipfile
import logging

logger = logging.getLogger(__name__)

# Página principal de bienvenida
def landingView(request):
    logger.info(f"Acceso a landingView por usuario {request.user}")
    return render(request, 'landing.html')

# Página de inicio/Sobre nosotros
def inicioView(request):
    logger.info(f"Acceso a inicioView por usuario {request.user}")
    return render(request, 'inicio.html')

# Vista para registrar un nuevo propietario
def registrar_propietario(request):
    if request.method == 'POST':
        form = PropietarioForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info(f"Propietario registrado por usuario {request.user}")
            return redirect('lista_propietarios')
    else:
        form = PropietarioForm()
    return render(request, 'registrar_propietario.html', {'form': form})

# Vista para mostrar la lista de propietarios registrados
def lista_propietarios(request):
    logger.info(f"Acceso a lista_propietarios por usuario {request.user}")
    from .models import Propietario
    propietarios = Propietario.objects.all()
    return render(request, 'lista_propietarios.html', {'propietarios': propietarios})

# Vista para registrar una nueva mascota
def registrar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info(f"Mascota registrada por usuario {request.user}")
            return redirect('lista_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'registrar_mascota.html', {'form': form})

# Vista para mostrar la lista de mascotas registradas
def lista_mascotas(request):
    logger.info(f"Acceso a lista_mascotas por usuario {request.user}")
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

def registrar_bitacora(request):
    if request.method == 'POST':
        form = BitacoraConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_bitacoras')
    else:
        form = BitacoraConsultaForm()
    return render(request, 'registrar_bitacora.html', {'form': form})

def lista_bitacoras(request):
    bitacoras = BitacoraConsulta.objects.select_related('mascota', 'mascota__propietario').all()
    return render(request, 'lista_bitacoras.html', {'bitacoras': bitacoras})

def editar_bitacora(request, pk):
    bitacora = get_object_or_404(BitacoraConsulta, pk=pk)
    if request.method == 'POST':
        form = BitacoraConsultaForm(request.POST, instance=bitacora)
        if form.is_valid():
            form.save()
            return redirect('lista_bitacoras')
    else:
        form = BitacoraConsultaForm(instance=bitacora)
    return render(request, 'editar_bitacora.html', {'form': form, 'bitacora': bitacora})

def eliminar_bitacora(request, pk):
    bitacora = get_object_or_404(BitacoraConsulta, pk=pk)
    if request.method == 'POST':
        bitacora.delete()
        return redirect('lista_bitacoras')
    return render(request, 'eliminar_bitacora.html', {'bitacora': bitacora})

def historia_clinica(request):
    mascotas = Mascota.objects.prefetch_related('bitacoras', 'propietario').all()
    return render(request, 'historia_clinica.html', {'mascotas': mascotas})

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

# Listar cirugías
def lista_cirugias(request):
    cirugias = Cirugia.objects.select_related('mascota', 'veterinario').all()
    return render(request, 'lista_cirugias.html', {'cirugias': cirugias})

# Registrar cirugía
def registrar_cirugia(request):
    if request.method == 'POST':
        form = CirugiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cirugias')
    else:
        form = CirugiaForm()
    return render(request, 'registrar_cirugia.html', {'form': form})

# Editar cirugía
def editar_cirugia(request, pk):
    cirugia = get_object_or_404(Cirugia, pk=pk)
    if request.method == 'POST':
        form = CirugiaForm(request.POST, instance=cirugia)
        if form.is_valid():
            form.save()
            return redirect('lista_cirugias')
    else:
        form = CirugiaForm(instance=cirugia)
    return render(request, 'editar_cirugia.html', {'form': form, 'cirugia': cirugia})

# Eliminar cirugía
def eliminar_cirugia(request, pk):
    cirugia = get_object_or_404(Cirugia, pk=pk)
    if request.method == 'POST':
        cirugia.delete()
        return redirect('lista_cirugias')
    return render(request, 'eliminar_cirugia.html', {'cirugia': cirugia})

# Registrar veterinario
def registrar_veterinario(request):
    if request.method == 'POST':
        form = VeterinarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_veterinarios')
    else:
        form = VeterinarioForm()
    return render(request, 'registrar_veterinario.html', {'form': form})

# Listar veterinarios
def lista_veterinarios(request):
    veterinarios = Veterinario.objects.all()
    return render(request, 'lista_veterinarios.html', {'veterinarios': veterinarios})

# Editar veterinario
def editar_veterinario(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == 'POST':
        form = VeterinarioForm(request.POST, instance=veterinario)
        if form.is_valid():
            form.save()
            return redirect('lista_veterinarios')
    else:
        form = VeterinarioForm(instance=veterinario)
    return render(request, 'editar_veterinario.html', {'form': form, 'veterinario': veterinario})

# Eliminar veterinario
def eliminar_veterinario(request, pk):
    from .models import Veterinario
    try:
        veterinario = get_object_or_404(Veterinario, pk=pk)
    except Exception as e:
        logger.warning(f"Intento de eliminar veterinario inexistente (id={pk}) por usuario {request.user}")
        return HttpResponse('Veterinario no encontrado.', status=404)
    if request.method == 'POST':
        veterinario.delete()
        logger.info(f"Veterinario eliminado (id={pk}) por usuario {request.user}")
        return redirect('lista_veterinarios')
    return render(request, 'eliminar_veterinario.html', {'veterinario': veterinario})

def exportar_propietarios_csv(request):
    try:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="propietarios.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Nombre', 'Teléfono', 'Email'])
        from .models import Propietario
        propietarios = Propietario.objects.all()
        logger.debug(f"Se encontraron {propietarios.count()} propietarios para exportar.")
        for propietario in propietarios:
            writer.writerow([propietario.id, propietario.nombre, getattr(propietario, 'telefono', ''), getattr(propietario, 'email', '')])
        logger.info(f"Exportación de propietarios realizada por el usuario {request.user}")
        return response
    except Exception as e:
        logger.error(f"Error exportando propietarios: {e}")
        return HttpResponse('Ocurrió un error al exportar propietarios.', status=500)

def exportar_mascotas_csv(request):
    try:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="mascotas.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID', 'Nombre', 'Especie', 'Edad', 'Propietario'])
        for mascota in Mascota.objects.select_related('propietario').all():
            writer.writerow([
                mascota.id,
                mascota.nombre,
                mascota.especie,
                mascota.edad,
                mascota.propietario.nombre if mascota.propietario else ''
            ])
        logger.info(f"Exportación de mascotas realizada por el usuario {request.user}")
        return response
    except Exception as e:
        logger.error(f"Error exportando mascotas: {e}")
        return HttpResponse('Ocurrió un error al exportar mascotas.', status=500)

def exportar_todo_zip(request):
    try:
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            # Propietarios
            propietarios_io = io.StringIO()
            writer = csv.writer(propietarios_io)
            writer.writerow(['ID', 'Nombre', 'Teléfono', 'Email'])
            from .models import Propietario
            for p in Propietario.objects.all():
                writer.writerow([p.id, p.nombre, getattr(p, 'telefono', ''), getattr(p, 'email', '')])
            zip_file.writestr('propietarios.csv', propietarios_io.getvalue())
            # Mascotas
            mascotas_io = io.StringIO()
            writer = csv.writer(mascotas_io)
            writer.writerow(['ID', 'Nombre', 'Especie', 'Edad', 'Propietario'])
            for m in Mascota.objects.select_related('propietario').all():
                writer.writerow([m.id, m.nombre, m.especie, m.edad, m.propietario.nombre if m.propietario else ''])
            zip_file.writestr('mascotas.csv', mascotas_io.getvalue())
            # Veterinarios
            veterinarios_io = io.StringIO()
            writer = csv.writer(veterinarios_io)
            writer.writerow(['ID', 'Nombre', 'Apellido', 'Especialidad', 'Teléfono', 'Email'])
            for v in Veterinario.objects.all():
                writer.writerow([v.id, v.nombre, v.apellido, v.especialidad, v.telefono, v.email])
            zip_file.writestr('veterinarios.csv', veterinarios_io.getvalue())
            # Citas
            citas_io = io.StringIO()
            writer = csv.writer(citas_io)
            writer.writerow(['ID', 'Mascota', 'Fecha y hora', 'Motivo', 'Notas'])
            from .models import Cita
            for c in Cita.objects.select_related('mascota').all():
                writer.writerow([c.id, c.mascota.nombre if c.mascota else '', c.fecha_hora, c.motivo, c.notas])
            zip_file.writestr('citas.csv', citas_io.getvalue())
            # Cirugías
            cirugias_io = io.StringIO()
            writer = csv.writer(cirugias_io)
            writer.writerow(['ID', 'Mascota', 'Veterinario', 'Fecha', 'Tipo', 'Descripción', 'Estado'])
            for cir in Cirugia.objects.select_related('mascota', 'veterinario').all():
                writer.writerow([
                    cir.id,
                    cir.mascota.nombre if cir.mascota else '',
                    cir.veterinario.nombre_completo if cir.veterinario else '',
                    cir.fecha,
                    cir.tipo,
                    cir.descripcion,
                    cir.estado
                ])
            zip_file.writestr('cirugias.csv', cirugias_io.getvalue())
            # Medicamentos
            medicamentos_io = io.StringIO()
            writer = csv.writer(medicamentos_io)
            writer.writerow(['ID', 'Nombre', 'Descripción', 'Cantidad disponible', 'Fecha vencimiento'])
            for med in Medicamento.objects.all():
                writer.writerow([med.id, med.nombre, med.descripcion, med.cantidad_disponible, med.fecha_vencimiento])
            zip_file.writestr('medicamentos.csv', medicamentos_io.getvalue())
            # Bitácoras
            bitacoras_io = io.StringIO()
            writer = csv.writer(bitacoras_io)
            writer.writerow(['ID', 'Mascota', 'Fecha consulta', 'Observaciones', 'Diagnóstico', 'Tratamiento', 'Próxima revisión'])
            from .models import BitacoraConsulta
            for b in BitacoraConsulta.objects.select_related('mascota').all():
                writer.writerow([
                    b.id,
                    b.mascota.nombre if b.mascota else '',
                    b.fecha_consulta,
                    b.observaciones,
                    b.diagnostico,
                    b.tratamiento,
                    b.proxima_revision
                ])
            zip_file.writestr('bitacoras.csv', bitacoras_io.getvalue())
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="exportacion_veterinaria.zip"'
        logger.info(f"Exportación ZIP completa realizada por el usuario {request.user}")
        return response
    except Exception as e:
        logger.error(f"Error exportando ZIP completo: {e}")
        return HttpResponse('Ocurrió un error al exportar toda la base de datos.', status=500)