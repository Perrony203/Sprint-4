"""
URL configuration for veterinaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from veterinariapp.views import landingView, inicioView, registrar_propietario, lista_propietarios, registrar_mascota, lista_mascotas, registrar_cita, lista_citas, registrar_bitacora, lista_bitacoras, editar_bitacora, eliminar_bitacora, historia_clinica, lista_medicamentos, agregar_medicamento, editar_medicamento, eliminar_medicamento, lista_cirugias, registrar_cirugia, editar_cirugia, eliminar_cirugia, registrar_veterinario, lista_veterinarios, editar_veterinario, eliminar_veterinario, exportar_todo_zip

urlpatterns = [
    path('admin/', admin.site.urls),  # Acceso al panel de administración
    path('', landingView, name='Landing'),  # Página principal
    path('inicio/', inicioView, name='inicio'),  # Página de inicio/Sobre nosotros
    path('registrar-propietario/', registrar_propietario, name='registrar_propietario'),  # Formulario de propietario
    path('lista-propietarios/', lista_propietarios, name='lista_propietarios'),  # Listado de propietarios
    path('registrar-mascota/', registrar_mascota, name='registrar_mascota'),  # Formulario de mascota
    path('lista-mascotas/', lista_mascotas, name='lista_mascotas'),  # Listado de mascotas
    path('registrar-cita/', registrar_cita, name='registrar_cita'),  # Formulario de cita
    path('lista-citas/', lista_citas, name='lista_citas'),  # Listado de citas
    path('registrar-bitacora/', registrar_bitacora, name='registrar_bitacora'),  # Formulario de bitácora
    path('lista-bitacoras/', lista_bitacoras, name='lista_bitacoras'),  # Listado de bitácoras
    path('editar-bitacora/<int:pk>/', editar_bitacora, name='editar_bitacora'),  # Editar bitácora
    path('eliminar-bitacora/<int:pk>/', eliminar_bitacora, name='eliminar_bitacora'),  # Eliminar bitácora
    path('historia-clinica/', historia_clinica, name='historia_clinica'),  # Historia clínica
    path('medicamentos/', lista_medicamentos, name = 'lista_medicamentos'),  # URL para medicamentos
    path('agregar-medicamento/', agregar_medicamento, name='agregar_medicamento'),  # URL para agregar medicamento
    path('editar-medicamento/<str:nombre>/', editar_medicamento, name='editar_medicamento'),  # URL para editar medicamento
    path('eliminar-medicamento/<str:nombre>/', eliminar_medicamento, name='eliminar_medicamento'),
    path('cirugias/', lista_cirugias, name='lista_cirugias'),  # Listar cirugías
    path('registrar-cirugia/', registrar_cirugia, name='registrar_cirugia'),  # Registrar cirugía
    path('editar-cirugia/<int:pk>/', editar_cirugia, name='editar_cirugia'),  # Editar cirugía
    path('eliminar-cirugia/<int:pk>/', eliminar_cirugia, name='eliminar_cirugia'),
    path('veterinarios/', lista_veterinarios, name='lista_veterinarios'),  # Listar veterinarios
    path('registrar-veterinario/', registrar_veterinario, name='registrar_veterinario'),  # Registrar veterinario
    path('editar-veterinario/<int:pk>/', editar_veterinario, name='editar_veterinario'),  # Editar veterinario
    path('eliminar-veterinario/<int:pk>/', eliminar_veterinario, name='eliminar_veterinario'),  # Eliminar veterinario
    path('exportar-todo/', exportar_todo_zip, name='exportar_todo_zip'),
]
