from django.shortcuts import render, redirect
from administradores.models import alumnos



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
                print(semestre)
                return render(request, "administrador/visualizar.html",{"numero_control":numeroControl,"session":request.session,"semestre":semestre,"numero_control":numeroControl,"nombre_alumno":nombre,"carrera":carrera})
            else:
                return redirect("/login/")
        except alumnos.DoesNotExist:
            return render(request, "administrador/index.html",{"session":request.session, "numero_control":numeroControl,"error":True})

def buscar_articulo(request):
    print("lol")

    return render(request, "administrador/generar_prestamo.html",{"session":request.session})
