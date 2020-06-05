from django.db import models

# Create your models here.

class usuarios(models.Model):

    AREA = (
        ('biblioteca', 'Biblioteca'),
        ('laboratorio de computo', 'Laboratorio de computo'),
        ('laboratorio de quimica', 'Laboratorio de quimica'),
        ('laller de electronica', 'Taller de electronica'),
        ('taller de industrial', 'Taller de industrial'),
    )

    TIPO = (
        ('escolares', 'Control Escolar'),
        ('laboratorios', 'Laboratorios'),
    )

    nombre=models.CharField(max_length=50, verbose_name="Nombre")
    apellido=models.CharField(max_length=50, verbose_name="Apellido")
    usuario=models.CharField(max_length=50, verbose_name="Usuario")
    contraseña=models.CharField(max_length=50, verbose_name="Contraseña")
    tipo=models.CharField(max_length=50, verbose_name="Tipo", choices=TIPO)
    area=models.CharField(max_length=50, verbose_name="Area", choices=AREA)
    email=models.EmailField(verbose_name="E-mail")
    img=models.CharField(max_length=50, verbose_name="Foto")

    def __str__(self):
        return self.usuario
