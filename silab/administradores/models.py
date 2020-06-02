from django.db import models

# Create your models here.
class alumnos(models.Model):
    id=models.CharField(primary_key = True, max_length=20, verbose_name="Numero de control")
    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    carrera=models.CharField(max_length=30, verbose_name="carrera")
    semestre=models.IntegerField(verbose_name="Semestre")
    TotalPrestamos=models.IntegerField(verbose_name="Total de prestamos")
    totalAdeudos=models.IntegerField(verbose_name="Total de adeudos")

class articulos(models.Model):
    id=models.CharField(primary_key = True, max_length=50, verbose_name="ID")
    nombre=models.CharField(max_length=50, verbose_name="Nombre Articulo")
    area=models.CharField(max_length=30, verbose_name="Area")
    precio=models.FloatField(verbose_name="Precio")
    status=models.BooleanField(default=False, verbose_name="Status")

class adeudos(models.Model):
    numeroControl=models.ForeignKey(alumnos, on_delete = models.CASCADE, verbose_name="Numero de control")
    articulo=models.ForeignKey(articulos, on_delete = models.CASCADE, verbose_name="Articulo")
    cantidad=models.IntegerField(verbose_name="Cantidad")



class historial(models.Model):
    numeroControl=models.ForeignKey(alumnos, on_delete = models.CASCADE, verbose_name="Numero de control")
    articulo=models.ForeignKey(articulos, on_delete = models.CASCADE, verbose_name="Numero de control")
    cantidad=models.IntegerField(verbose_name="Cantidad")
    fecha=models.DateField(verbose_name="Fecha")
