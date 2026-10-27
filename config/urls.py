
from django.contrib import admin
from django.urls import path, include
from mapa import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        ".well-known/assetlinks.json",
        views.assetlinks,
        name="assetlinks",
    ),
    path("", include("mapa.urls")),
]