
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.http import JsonResponse

import json
from pathlib import Path

from django.conf import settings

from .models import Negocio
from .forms import NegocioForm


def assetlinks(request):
    return JsonResponse([
        {
            "relation": [
                "delegate_permission/common.handle_all_urls"
            ],
            "target": {
                "namespace": "android_app",
                "package_name": "com.somagt.mesaredonda360",
                "sha256_cert_fingerprints": [
                    "0C:0D:86:F8:EA:6D:DD:C0:0F:38:A3:8E:9A:C9:8B:FE:35:39:EB:ED:4D:43:A1:6D:27:2B:08:3B:FB:F1:8C:ED"
                ],
            },
        }
    ], safe=False)


def mapa_publico(request):
    negocios = Negocio.objects.filter(
        activo=True,
        latitud__isnull=False,
        longitud__isnull=False,
    ).prefetch_related("productos_catalogo")

    puntos_mapa = []

    for negocio in negocios:
        datos = {
            "id": negocio.id,
            "nombre": negocio.nombre,
            "categoria": negocio.get_categoria_display(),
            "direccion": negocio.direccion,
            "referencia": negocio.referencia,
            "productos": negocio.productos,
            "descripcion": negocio.descripcion,
            "telefono": negocio.telefono,
            "latitud": float(negocio.latitud),
            "longitud": float(negocio.longitud),
            "plan": negocio.plan,
            "imagen": (
                negocio.imagen.url
                if negocio.imagen
                else ""
            ),
            "redes": {},
            "catalogo": [],
        }

        if (
            negocio.plan in ("premium", "catalogo")
            and negocio.estado_membresia == "activa"
        ):
            datos["redes"] = {
                "TikTok": negocio.tiktok_url,
                "Facebook": negocio.facebook_url,
                "Instagram": negocio.instagram_url,
                "WhatsApp": negocio.whatsapp_url,
            }

        if (
            negocio.plan == "catalogo"
            and negocio.estado_membresia == "activa"
        ):
            for producto in negocio.productos_catalogo.filter(
                activo=True
            ):
                datos["catalogo"].append({
                    "nombre": producto.nombre,
                    "codigo": producto.codigo,
                    "descripcion": producto.descripcion,
                    "precio": (
                        str(producto.precio_referencial)
                        if producto.precio_referencial is not None
                        else ""
                    ),
                    "imagen": (
                        producto.imagen.url
                        if producto.imagen
                        else ""
                    ),
                })

        puntos_mapa.append(datos)

    return render(
        request,
        "mapa/mapa.html",
        {
            "puntos_mapa": puntos_mapa,
            "es_superusuario": (
                request.user.is_authenticated
                and request.user.is_superuser
            ),
        },
    )


@login_required(login_url="/admin/login/")
def registrar_negocio(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    latitud = request.GET.get("lat", "")
    longitud = request.GET.get("lon", "")

    if request.method == "POST":
        form = NegocioForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            negocio = form.save()

            messages.success(
                request,
                f"El negocio «{negocio.nombre}» se registró correctamente.",
            )

            return redirect("mapa_publico")

    else:
        form = NegocioForm(
            initial={
                "latitud": latitud,
                "longitud": longitud,
                "plan": "gratis",
                "estado_membresia": "no_aplica",
            }
        )

    ruta = Path(settings.BASE_DIR) / "ubigeos"

    with open(
        ruta / "departamentos.json",
        encoding="utf-8",
    ) as f:
        departamentos = json.load(f)

    with open(
        ruta / "provincias.json",
        encoding="utf-8",
    ) as f:
        provincias = json.load(f)

    with open(
        ruta / "distritos.json",
        encoding="utf-8",
    ) as f:
        distritos = json.load(f)

    return render(
        request,
        "mapa/registrar_negocio.html",
        {
            "form": form,
            "departamentos_json": departamentos,
            "provincias_json": provincias,
            "distritos_json": distritos,
        },
    )


@login_required(login_url="/admin/login/")
def editar_negocio(request, id):
    if not request.user.is_superuser:
        raise PermissionDenied

    negocio = get_object_or_404(
        Negocio,
        pk=id,
    )

    if request.method == "POST":
        form = NegocioForm(
            request.POST,
            request.FILES,
            instance=negocio,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                f"El negocio «{negocio.nombre}» se actualizó correctamente.",
            )

            return redirect("mapa_publico")

    else:
        form = NegocioForm(
            instance=negocio,
        )

    ruta = Path(settings.BASE_DIR) / "ubigeos"

    with open(
        ruta / "departamentos.json",
        encoding="utf-8",
    ) as f:
        departamentos = json.load(f)

    with open(
        ruta / "provincias.json",
        encoding="utf-8",
    ) as f:
        provincias = json.load(f)

    with open(
        ruta / "distritos.json",
        encoding="utf-8",
    ) as f:
        distritos = json.load(f)

    return render(
        request,
        "mapa/registrar_negocio.html",
        {
            "form": form,
            "departamentos_json": departamentos,
            "provincias_json": provincias,
            "distritos_json": distritos,
            "es_edicion": True,
            "negocio": negocio,
        },
    )


def politica_privacidad(request):
    return render(
        request,
        "mapa/privacidad.html",
    )
