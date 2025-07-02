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

from veterinariapp.views import landingView, inicioView, registrar_propietario, lista_propietarios, registrar_mascota, lista_mascotas, registrar_cita, lista_citas

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
]
