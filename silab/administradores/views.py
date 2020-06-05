from django.shortcuts import render, redirect
from administradores.models import alumnos, articulos, adeudos, historial
import datetime
import random

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



    art=articulos.objects.filter(area=request.session["area"])



    return render(request, "administrador/index.html",{"session":request.session, "articulo":art})

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
                alum = alumnos.objects.get(id = numeroControl)
                adeud = adeudos.objects.filter(numeroControl = numeroControl)

                ade=adeudos.objects.filter(numeroControl_id=numeroControl)


                info_adeudo=[]

                info_articulo=[]

                titulo=[]
                print(ade)

                for ades in ade:

                    art=articulos.objects.get(id=ades.articulo_id)

                    info_articulo.append(art)



                    titulo.append(ades.articulo)


                    info_adeudo.append(ades)





                # for info in info_adeudo:
                #     print(info)









                return render(request, "administrador/visualizar.html",{"session":request.session,"alumno":alumno,"adeudos":info_adeudo, "articulo":info_articulo,'alum':alum,'adeud':adeud })
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
        id_articulo=request.POST["id_articulo"]
        str(id_articulo)

        fecha_actual=datetime.datetime.now()

        alumno=alumnos.objects.get(id=numeroControl)
        articulo=articulos.objects.get(id=id_articulo)

        forio=random.randrange(10000)


        # fecha_actual=str(fecha_actual.day)+"/"+str(fecha_actual.month)+"/"+str(fecha_actual.year)

        registrar_adeudo=adeudos(numeroAdeudo=forio,numeroControl=alumno, articulo=articulo, cantidad=1)
        registrar_adeudo.save()

        registrar_historial=historial(numeroControl=alumno, articulo=articulo, cantidad=1, fecha=fecha_actual )
        registrar_historial.save()




        articulo.status=True;
        articulo.save()
        # return redirect("/administrador/")
        return redirect("/validar/")
    else:
        return redirect("/validar/")






def generar_devolucion(request):
    try:
        if request.session["sesion"]==True and request.session["tipo"]=="laboratorios":
            pass

        else:
            return redirect("/validar/")
    except:
        return redirect("/login/")

    if request.method == "GET":
        print("entro")
        id_articulo=request.GET["id"]
        art=adeudos.objects.get(articulo_id=id_articulo)
        art.delete()

        articulo=articulos.objects.get(id=id_articulo)
        articulo.status=False;
        articulo.save()
        return redirect("/validar/")
    else:
        return redirect("/validar/")

def agregar_articulo(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    area=request.POST["area"]
    precio=request.POST["precio"]
    float(precio)

    articulo=articulos(id=id, nombre=nombre, area=area, precio=precio, status=False)
    articulo.save()
    return redirect("/validar/")
