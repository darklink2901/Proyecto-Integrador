from django.shortcuts import render, redirect
from django.db.models import Q
from administradores.models import alumnos,historial,adeudos,articulos

def control_escolar(request):

    try:
        if request.session["sesion"]==True and request.session["tipo"]=="escolares":
            alum = alumnos.objects.all()
            queryset = request.GET.get("numero_control")
            if queryset:
                alum =alumnos.objects.filter(
                 Q(id__icontains = queryset) |
                 Q(nombre__icontains = queryset)|
                 Q(carrera__icontains = queryset)
                ).distinct()
            return render(request, "contEscolar/index0.html",{'alum': alum})

        else:
            return redirect("/validar/")
    except:
        return redirect("/login/")


    return render(request, "contEscolar/index0.html")

def detalles_alumno(request,id):
    if request.user.is_authenticated:
        alum = alumnos.objects.get(id = id)
        if  (alum.totalAdeudos == 0 and alum.TotalPrestamos == 0):
            return render(request, "contEscolar/lib.html")
        else:
            num= alum.id
            adeud = adeudos.objects.filter(numeroControl = num)
            contexto = {
                'alum':alum,
                'adeud':adeud
            }
            return render(request, "contEscolar/cont.html",contexto)

def elim_pago(request, id,num):
    eliminarAdeudo =adeudos.objects.filter(articulo = id).delete()
    alum = alumnos.objects.get(id = num)
    alum.totalAdeudos = 0
    alum.save()
    return redirect("/login/")
