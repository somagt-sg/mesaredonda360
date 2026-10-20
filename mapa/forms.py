from django import forms
from .models import Negocio


class NegocioForm(forms.ModelForm):

    # Los selectores se llenan desde los archivos JSON mediante JavaScript.
    # Por eso se validan como texto y no con una lista fija de choices.

    region = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.Select(
            attrs={"id": "id_region"}
        ),
        error_messages={
            "required": "Selecciona una región."
        },
    )

    provincia = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.Select(
            attrs={"id": "id_provincia"}
        ),
        error_messages={
            "required": "Selecciona una provincia."
        },
    )

    distrito = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.Select(
            attrs={"id": "id_distrito"}
        ),
        error_messages={
            "required": "Selecciona un distrito."
        },
    )

    
    zona_sector = forms.ChoiceField(
        required=False,
        label="Zona / Sector / Urbanización / Asociación / Asentamiento humano / Otro",
        choices=[
            ("", "Selecciona una opción"),
            ("Zona", "Zona"),
            ("Sector", "Sector"),
            ("Urbanización", "Urbanización"),
            ("Asociación", "Asociación"),
            ("Asentamiento humano", "Asentamiento humano"),
            ("Otro", "Otro"),
        ],
        widget=forms.Select(
            attrs={"id": "id_zona_sector"}
        ),
    )

    nombre_zona = forms.CharField(
        required=False,
        max_length=150,
        label="Nombre de la ubicación",
        widget=forms.TextInput(
            attrs={
                "id": "id_nombre_zona",
                "placeholder": "Ej.: Urbanización Las Flores",
                "maxlength": "150",
            }
        ),
    )

    piso = forms.TypedChoiceField(
        required=False,
        coerce=int,
        empty_value=None,
        choices=[
            ("", "No aplica"),
            *[(i, str(i)) for i in range(1, 21)],
        ],
        widget=forms.Select(
            attrs={"id": "id_piso"}
        ),
    )

    puesto = forms.CharField(
        required=False,
        max_length=50,
        label="Puesto / Stand",
        widget=forms.TextInput(
            attrs={
                "id": "id_puesto",
                "placeholder": "Ej. 125 o A-12",
            }
        ),
    )

    direccion = forms.CharField(
        required=False,
        max_length=500,
        widget=forms.TextInput(
            attrs={
                "id": "id_direccion",
                "readonly": "readonly",
                "placeholder": "Se genera automáticamente",
            }
        ),
    )

    # RUC opcional. Si se ingresa, debe tener exactamente 11 dígitos.
    ruc = forms.CharField(
        required=False,
        max_length=11,
        widget=forms.TextInput(
            attrs={
                "id": "id_ruc",
                "type": "text",
                "maxlength": "11",
                "inputmode": "numeric",
                "pattern": "[0-9]{11}",
                "placeholder": "Ingresa los 11 dígitos del RUC",
                "oninput": "this.value = this.value.replace(/[^0-9]/g, '').slice(0, 11)",
            }
        ),
        error_messages={
            "max_length": "El RUC debe contener exactamente 11 dígitos.",
        },
    )

    # Teléfono principal.
    telefono = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "id": "id_telefono",
                "type": "tel",
                "placeholder": "Teléfono principal o WhatsApp",
            }
        ),
    )

    # Teléfonos adicionales opcionales.
    telefono_2 = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "id": "id_telefono_2",
                "type": "tel",
                "placeholder": "Segundo teléfono (opcional)",
            }
        ),
    )

    telefono_3 = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "id": "id_telefono_3",
                "type": "tel",
                "placeholder": "Tercer teléfono (opcional)",
            }
        ),
    )

    class Meta:
        model = Negocio

        fields = [
            "nombre",
            "imagen",
            "ruc",
            "categoria",

            "telefono",
            "telefono_2",
            "telefono_3",

            "region",
            "provincia",
            "distrito",
            "zona_sector",

            "tipo_via",
            "nombre_via",
            "numero",
            "etapa",
            "piso",
            "puesto",
            "direccion",
            "referencia",

            "productos",
            "descripcion",
            "latitud",
            "longitud",

            "plan",
            "estado_membresia",
            "fecha_inicio_membresia",
            "fecha_fin_membresia",

            "tiktok_url",
            "facebook_url",
            "instagram_url",
            "whatsapp_url",

            "activo",
        ]

        widgets = {
            "tipo_via": forms.Select(
                attrs={"id": "id_tipo_via"}
            ),

            "nombre_via": forms.TextInput(
                attrs={
                    "id": "id_nombre_via",
                    "placeholder": "Ej. Argentina",
                }
            ),

            "numero": forms.TextInput(
                attrs={
                    "id": "id_numero",
                    "placeholder": "Ej. 123",
                }
            ),

            "etapa": forms.TextInput(
                attrs={
                    "id": "id_etapa",
                    "placeholder": "Galería, centro comercial o etapa",
                }
            ),

            "referencia": forms.TextInput(
                attrs={
                    "id": "id_referencia",
                    "placeholder": "Ej. frente al mercado",
                }
            ),

            "productos": forms.Textarea(
                attrs={"rows": 3}
            ),

            "descripcion": forms.Textarea(
                attrs={"rows": 3}
            ),

            "imagen": forms.ClearableFileInput(
                attrs={"accept": "image/*"}
            ),

            "latitud": forms.NumberInput(
                attrs={
                    "step": "0.0000001",
                    "id": "id_latitud",
                    "placeholder": "-12.0464",
                }
            ),

            "longitud": forms.NumberInput(
                attrs={
                    "step": "0.0000001",
                    "id": "id_longitud",
                    "placeholder": "-77.0428",
                }
            ),

            "fecha_inicio_membresia": forms.DateInput(
                attrs={"type": "date"}
            ),

            "fecha_fin_membresia": forms.DateInput(
                attrs={"type": "date"}
            ),
        }

        labels = {
            "direccion": "Dirección definitiva",
            "etapa": "Galería, centro comercial o etapa",
            "piso": "Piso (del 1 al 20)",
            "puesto": "Puesto / Stand",
            "telefono": "Teléfono principal o WhatsApp",
            "telefono_2": "Segundo teléfono",
            "telefono_3": "Tercer teléfono",
        }

    def clean_region(self):
        return self.cleaned_data["region"].strip()

    def clean_provincia(self):
        return self.cleaned_data["provincia"].strip()

    def clean_distrito(self):
        return self.cleaned_data["distrito"].strip()

    def clean_ruc(self):
        ruc = (self.cleaned_data.get("ruc") or "").strip()

        if ruc and (len(ruc) != 11 or not ruc.isdigit()):
            raise forms.ValidationError(
                "El RUC debe contener exactamente 11 dígitos numéricos."
            )

        return ruc