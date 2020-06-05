from django.shortcuts import render, redirect
from django.db.models import Q
from administradores.models import alumnos,historial,adeudos,articulos
from django.views.generic import View
from django.http import HttpResponse
from controlEscolar.utils import render_to_pdf
# import pdfkit

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
            contexto = {
            'alum':alum
            }
            return render(request, "contEscolar/lib.html",contexto)
        else:
            num= alum.id
            adeud = adeudos.objects.filter(numeroControl = num)
            contexto = {
                'alum':alum,
                'adeud':adeud
            }
            return render(request, "contEscolar/cont.html",contexto)
#Andres joto
def elim_pago(request, ad,num):
    eliminarAdeudo = adeudos.objects.filter(numeroAdeudo = ad).delete()
    alum = alumnos.objects.get(id = num)
    if alum.totalAdeudos != 0:
        alum.totalAdeudos = alum.totalAdeudos - 1
        alum.save()
    return redirect("/login/")

def documento(request,id):
    alum = alumnos.objects.get(id = id)
    contexto = {
        'alum': alum
    }
    pdf = render_to_pdf('contEscolar/lista.html', contexto)
    return HttpResponse(pdf, content_type='application/pdf')
