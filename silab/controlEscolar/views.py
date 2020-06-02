from django.shortcuts import render, redirect


# def validar_sesion(request):
#     try:
#         if request.session["sesion"]==True:
#             print("Hay sesion")
#             pass
#
#     except:
#         return redirect("/ddd/")
#         print("No hay sesion")


def control_escolar(request):

    try:
        if request.session["sesion"]==True and request.session["tipo"]=="escolares":
            pass
        else:
            return redirect("/validar/")
    except:
        return redirect("/login/")


    return render(request, "administrador/index.html")
