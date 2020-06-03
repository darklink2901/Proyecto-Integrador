from django.shortcuts import render, redirect
from login.models import usuarios


def login(request):

    try:
        if request.session["sesion"]==True:
            return redirect("/control_escolar/")
    except:
        pass

    if request.method == "POST":
        user=request.POST["user"]
        password=request.POST["password"]
        try:
            user = usuarios.objects.get(usuario__exact=request.POST["user"])
            if user.contraseña == request.POST["password"]:
                request.session["nombre"] = user.nombre+" "+user.apellido
                request.session["area"] = user.area
                request.session["tipo"] = user.tipo
                request.session["sesion"] = True
                return redirect("/validar/")
            else:
                mensaje="Usuario o contraseña incorrectos"
                return render(request, "login.html",{'mensaje':mensaje})
        except usuarios.DoesNotExist:
            mensaje="Usuario o contraseña incorrectos"
            return render(request, "login.html",{'mensaje':mensaje})
    else:
        return render(request, "login.html")


def logout(request):

    try:
        del request.session["sesion"]
        print("Sesion destruida")
        return redirect("/login/")
    except KeyError:
        return redirect("/login/")


def validar(request):

    try:
        if request.session["sesion"]==True:
            pass
    except:
        return redirect("/login/")


    if request.session["tipo"] == "escolares":
        return redirect("/control_escolar/")
    elif request.session["tipo"] == "laboratorios":
        print("lol")
        return redirect("/administrador/")

    return render(request, "index.html")
