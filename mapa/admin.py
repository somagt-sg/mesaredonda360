
from django.contrib import admin
from .models import Negocio, Producto


class ProductoInline(admin.TabularInline):
    model = Producto
    extra = 1
    fields = (
        "nombre",
        "codigo",
        "descripcion",
        "precio_referencial",
        "imagen",
        "activo",
    )


@admin.register(Negocio)
class NegocioAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "ruc",
        "categoria",
        "plan",
        "estado_membresia",
        "telefono",
        "activo",
    )

    list_filter = (
        "categoria",
        "plan",
        "estado_membresia",
        "activo",
    )

    search_fields = (
        "nombre",
        "ruc",
        "direccion",
        "productos",
        "telefono",
    )

    list_editable = (
        "plan",
        "estado_membresia",
        "activo",
    )

    ordering = ("nombre",)

    readonly_fields = ("fecha_registro",)

    fieldsets = (
        (
            "Información del negocio",
            {
                "fields": (
                    "nombre",
                    "ruc",
                    "categoria",
                    "telefono",
                    "direccion",
                    "referencia",
                )
            },
        ),
        (
            "Información comercial",
            {
                "fields": (
                    "productos",
                    "descripcion",
                )
            },
        ),
        (
            "Ubicación en el mapa",
            {
                "fields": (
                    "latitud",
                    "longitud",
                )
            },
        ),
        (
            "Plan y membresía",
            {
                "fields": (
                    "plan",
                    "estado_membresia",
                    "fecha_inicio_membresia",
                    "fecha_fin_membresia",
                )
            },
        ),
        (
            "Redes sociales y contacto",
            {
                "fields": (
                    "tiktok_url",
                    "facebook_url",
                    "instagram_url",
                    "whatsapp_url",
                )
            },
        ),
        (
            "Publicación",
            {
                "fields": (
                    "activo",
                    "fecha_registro",
                )
            },
        ),
    )

    inlines = [ProductoInline]


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "negocio",
        "codigo",
        "precio_referencial",
        "activo",
    )

    list_filter = (
        "activo",
        "negocio__plan",
    )

    search_fields = (
        "nombre",
        "codigo",
        "negocio__nombre",
    )

    list_editable = ("activo",)

    ordering = ("nombre",)