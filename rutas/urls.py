from django.urls import path
from . import views

urlpatterns = [
    path("", views.indice, name="rutas_indice"),
    path("ayuda/",views.ayuda, name="rutas_ayuda"),
    path("hora/",views.hora_actual, name="rutas_hora"),
    path("tarea1/",views.hola_mundo),
    # Avance hasta 28/01/2026
    path("hola/", views.hola, name="rutas_hola"),
    path("hola/<str:nombre>/", views.hola_nombre, name="rutas_hola_nombre"),
    path("suma/<int:a>/<int:b>/", views.suma, name="rutas_suma"), 
    path("buscar/",views.buscar, name="rutas_buscar"),
    path("metodo/", views.metodo, name="rutas_metodo"),
    path("api/estado/", views.api_estado, name="rutas_api_estado"),
    path("edad/<int:edad>/", views.edad, name="rutas_edad"),
]

# urlpatterns += [
#     path("hola/", views.hola, name="rutas_hola"),
#     path("hola//", views.hola_nombre, name="rutas_hola_nombre"),
#     path("suma///", views.suma, name="rutas_suma"),
# ]