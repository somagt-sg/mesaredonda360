
from django.urls import path
from . import views

urlpatterns = [
    path("", views.mapa_publico, name="mapa_publico"),

    path(
        "privacidad/",
        views.politica_privacidad,
        name="politica_privacidad",
    ),

    path(
        "negocios/nuevo/",
        views.registrar_negocio,
        name="registrar_negocio",
    ),

    path(
        "negocios/<int:id>/editar/",
        views.editar_negocio,
        name="editar_negocio",
    ),
]