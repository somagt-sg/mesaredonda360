
from django.db import models
from django.core.validators import RegexValidator


class Negocio(models.Model):

    CATEGORIAS = [
        ("galeria", "Galería comercial"),
        ("importadora", "Importadora"),
        ("tienda", "Tienda"),
        ("puesto", "Puesto comercial"),
        ("mayorista", "Mayorista"),
        ("otros", "Otros"),
    ]

    PLANES = [
        ("gratis", "Gratuito"),
        ("premium", "Premium"),
        ("catalogo", "Catálogo"),
    ]

    ESTADOS_MEMBRESIA = [
        ("no_aplica", "No aplica"),
        ("pendiente", "Pendiente"),
        ("activa", "Activa"),
        ("vencida", "Vencida"),
    ]

    TIPOS_VIA = [
        ("avenida", "Avenida"),
        ("jirón", "Jirón"),
        ("calle", "Calle"),
        ("pasaje", "Pasaje"),
        ("prolongacion", "Prolongación"),
        ("carretera", "Carretera"),
        ("otro", "Otro"),
    ]

    PISOS = [
        (i, str(i))
        for i in range(1, 21)
    ]

    # =====================================================
    # DATOS GENERALES
    # =====================================================

    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre de la empresa, tienda o negocio",
    )

    imagen = models.ImageField(
        upload_to="negocios/",
        blank=True,
        null=True,
        verbose_name="Imagen o logo del negocio",
    )

    ruc = models.CharField(
        max_length=11,
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^\d{11}$",
                message="El RUC debe contener exactamente 11 dígitos.",
            )
        ],
        verbose_name="RUC",
    )

    categoria = models.CharField(
        max_length=30,
        choices=CATEGORIAS,
        default="tienda",
        verbose_name="Categoría",
    )

    # =====================================================
    # DIRECCIÓN ESTRUCTURADA
    # =====================================================

    region = models.CharField(
        max_length=100,
        default="Lima",
        verbose_name="Región",
    )

    provincia = models.CharField(
        max_length=100,
        default="Lima",
        verbose_name="Provincia",
    )

    distrito = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Distrito",
    )

    tipo_via = models.CharField(
        max_length=20,
        choices=TIPOS_VIA,
        blank=True,
        verbose_name="Tipo de vía",
    )

    nombre_via = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Nombre de la vía",
    )

    numero = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="Número de la vía",
    )

    etapa = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Galería, centro comercial, etapa o sector",
    )

    piso = models.PositiveSmallIntegerField(
        choices=PISOS,
        null=True,
        blank=True,
        verbose_name="Piso",
    )

    puesto = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Número o identificación del puesto",
    )

    direccion = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="Dirección definitiva",
    )

    referencia = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Referencia de ubicación",
    )

    # =====================================================
    # INFORMACIÓN COMERCIAL
    # =====================================================

    productos = models.TextField(
        blank=True,
        verbose_name="Productos que vende",
    )

    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción del negocio",
    )

    telefono = models.CharField(
        max_length=30,
        blank=True,
        verbose_name="Teléfono o WhatsApp",
    )

    # =====================================================
    # COORDENADAS
    # =====================================================

    latitud = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True,
        verbose_name="Latitud",
    )

    longitud = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        null=True,
        blank=True,
        verbose_name="Longitud",
    )

    # =====================================================
    # REDES SOCIALES Y CONTACTO
    # =====================================================

    tiktok_url = models.URLField(
        blank=True,
        verbose_name="Enlace de TikTok",
    )

    facebook_url = models.URLField(
        blank=True,
        verbose_name="Enlace de Facebook",
    )

    instagram_url = models.URLField(
        blank=True,
        verbose_name="Enlace de Instagram",
    )

    whatsapp_url = models.URLField(
        blank=True,
        verbose_name="Enlace directo a WhatsApp",
    )

    # =====================================================
    # PLANES COMERCIALES
    # =====================================================

    plan = models.CharField(
        max_length=20,
        choices=PLANES,
        default="gratis",
        verbose_name="Plan comercial",
    )

    estado_membresia = models.CharField(
        max_length=20,
        choices=ESTADOS_MEMBRESIA,
        default="no_aplica",
        verbose_name="Estado de membresía",
    )

    fecha_inicio_membresia = models.DateField(
        null=True,
        blank=True,
        verbose_name="Inicio de membresía",
    )

    fecha_fin_membresia = models.DateField(
        null=True,
        blank=True,
        verbose_name="Fin de membresía",
    )

    activo = models.BooleanField(
        default=True,
        verbose_name="Visible en el mapa",
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de registro",
    )

    # =====================================================
    # CONSTRUIR DIRECCIÓN DEFINITIVA
    # =====================================================

    def construir_direccion(self):
        partes = []

        if self.tipo_via:
            tipo = dict(self.TIPOS_VIA).get(
                self.tipo_via,
                self.tipo_via,
            )
            partes.append(tipo)

        if self.nombre_via:
            partes.append(self.nombre_via)

        if self.numero:
            partes.append(f"N.° {self.numero}")

        if self.etapa:
            partes.append(self.etapa)

        if self.piso is not None:
            partes.append(f"piso {self.piso}")

        if self.puesto.strip():
            partes.append(f"puesto {self.puesto.strip()}")

        if self.distrito:
            partes.append(f"distrito de {self.distrito}")

        if self.provincia:
            partes.append(f"provincia de {self.provincia}")

        if self.region:
            partes.append(f"región {self.region}")

        if self.referencia:
            partes.append(f"Referencia: {self.referencia}")

        return ", ".join(partes)

    @property
    def direccion_completa(self):
        return self.construir_direccion() or self.direccion

    def save(self, *args, **kwargs):
        direccion_generada = self.construir_direccion()

        if direccion_generada:
            self.direccion = direccion_generada

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Negocio"
        verbose_name_plural = "Negocios"
        ordering = ["nombre"]


class Producto(models.Model):

    negocio = models.ForeignKey(
        Negocio,
        on_delete=models.CASCADE,
        related_name="productos_catalogo",
        verbose_name="Negocio",
    )

    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre del producto",
    )

    codigo = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Código del producto",
    )

    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción del producto",
    )

    precio_referencial = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Precio referencial",
    )

    imagen = models.ImageField(
        upload_to="catalogo/",
        blank=True,
        null=True,
        verbose_name="Fotografía del producto",
    )

    activo = models.BooleanField(
        default=True,
        verbose_name="Visible en el catálogo",
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de registro",
    )

    def __str__(self):
        return f"{self.nombre} - {self.negocio.nombre}"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos del catálogo"
        ordering = ["nombre"]