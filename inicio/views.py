from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

# def indice(request):
#     return HttpResponse("Hola 😺 Estás en la app 'inicio'.")

def indice(request):
    variable = "Python + Django"
    contexto = {
        "ahora" : timezone.localtime(),
        "frutas" : ["Manzana","pera","naranja","plátano"],
        # estado : ["rechazado", "pendiente", "proceso", "completado"]
        "estado" : "pendiente",
        "variable" : variable,
    }

    # return HttpResponse("Hola 😺 Estás en la app 'inicio'.")
    # render(peticion, DONDE, QUE) 
    # DONDE es la ubicación de la plantilla html
    # QUE, son los datos que se enviara a la plantilla y utiliza dentro de si
    return render(request, "inicio/inicio.html", contexto)

def acerca(request):
    return render(request, "inicio/acerca.html")

def temario(request):
    return render(request, "inicio/temario.html")

def pato(request):
    return HttpResponse("Cuack 🦆")

def vaca(request):
    return HttpResponse("Muuu 🐮")

def perro(request):
    return HttpResponse("Wauu 🐶")

