"""silab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from login.views import *
from controlEscolar.views import *
from administradores.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('logout/', logout),
    path('validar/', validar),
    path('control_escolar/', control_escolar, name='control_escolar'),
    path('detalles_alumno/<str:id>/',detalles_alumno,name='detalles_alumno'),

    path('administrador/', administrador),
    path('administrador/buscar/', buscar_alumno),
    path('administrador/buscar/articulo/', buscar_articulo),
    path('administrador/buscar/articulo/generar_prestamo/', generar_prestamo),

]
