from django.contrib import admin

# Register your models here.

from administradores.models import alumnos, articulos, adeudos, historial

admin.site.register(alumnos)
admin.site.register(articulos)
admin.site.register(adeudos)
admin.site.register(historial)
