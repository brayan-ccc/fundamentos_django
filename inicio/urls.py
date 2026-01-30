from django.urls import path
from . import views

urlpatterns = [
    # path("", views.indice, name="indice"),
    path("", views.indice, name="inicio"),
    path("acerca/", views.acerca, name="acerca"),
    path("temario/", views.temario, name="temario"),

    path("vaca", views.vaca, name="vaca"),
    path("patito",views.pato, name="duck"),
    path("dog",views.perro,name="perro")
]