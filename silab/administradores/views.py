from django.shortcuts import render, redirect
from administradores.models import alumnos, articulos, adeudos, historial
import datetime

class Alumno():
    def __init__(self,numero_control,nombre,carrera,semestre):
        self.numero_control = numero_control
        self.nombre = nombre
        self.carrera = carrera
        self.semestre = semestre

class Articulo():
    def __init__(self,id,nombre,precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio


def administrador(request):

    try:
        if request.session["sesion"]==True and request.session["tipo"]=="laboratorios":
            pass
        else:
            return redirect("/validar/")
    except:
        return redirect("/login/")


    return render(request, "administrador/index.html",{"session":request.session})

def buscar_alumno(request):

    try:
        if request.session["sesion"]==True and request.session["tipo"]=="laboratorios":
            pass
        else:
            return redirect("/validar/")
    except:
        return redirect("/login/")

    if request.method == "GET":
        numeroControl=request.GET["numero_control"]
        str(numeroControl)
        try:
            user = alumnos.objects.get(id__exact=numeroControl)

            if user.id == numeroControl:
                nombre=user.nombre
                carrera=user.carrera
                semestre=user.semestre
                alumno = Alumno(numeroControl, nombre, carrera, semestre)
                print(semestre)
                return render(request, "administrador/visualizar.html",{"session":request.session,"alumno":alumno})
            else:
                return redirect("/login/")
        except alumnos.DoesNotExist:
            return render(request, "administrador/index.html",{"session":request.session, "numero_control":numeroControl,"error":True})

def buscar_articulo(request):

    try:
        if request.session["sesion"]==True and request.session["tipo"]=="laboratorios":
            pass

        else:
            return redirect("/validar/")
    except:
        return redirect("/login/")

    if request.method == "GET":

        id_articulo=request.GET["id_articulo"]
        nombre=request.GET["nombre_alumno"]
        carrera=request.GET["carrera"]
        semestre=request.GET["semestre"]
        numeroControl=request.GET["numero_control"]
        try:
            art = articulos.objects.get(id__exact=id_articulo)

            if art.id == id_articulo:
                print("Lo esta")
                alumno = Alumno(numeroControl, nombre, carrera, semestre)

                id=art.id
                nombre=art.nombre
                precio=art.precio

                articulo = Articulo(id, nombre, precio)

                return render(request, "administrador/generar_prestamo.html",{"session":request.session, "alumno":alumno, "articulo":articulo  })
            else:
                return redirect("/login/")
        except articulos.DoesNotExist:
            return render(request, "administrador/index.html",{"session":request.session, "numero_control":numeroControl,"error":True})


def generar_prestamo(request):

    try:
        if request.session["sesion"]==True and request.session["tipo"]=="laboratorios":
            pass

        else:
            return redirect("/validar/")
    except:
        return redirect("/login/")

    if request.method == "POST":

        numeroControl=request.POST["numero_control"]
        articulo=request.POST["nombre_articulo"]
        id_articulo=request.POST["nombre_articulo"]


        fecha=datetime.datetime.now()

        aa=alumnos.objects.get(id=17231573)

        fecha_alta=str(fecha.day)+"/"+str(fecha.month)+"/"+str(fecha.year)


        alta=adeudos(numeroControl=aa, articulo=articulo, cantidad=1)
        alta.save()

        return redirect("/administrador/")
    else:
        return redirect("/validar/")
