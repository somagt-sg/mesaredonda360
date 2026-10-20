import os
from pathlib import Path

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent


# =====================================================
# SEGURIDAD
# =====================================================

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
<<<<<<< HEAD
    "django-insecure-mesaredonda360-clave-local"
)

DEBUG = os.environ.get("DEBUG", "False").lower() in (
    "true",
    "1",
    "yes",
)
=======
    "django-insecure-mesaredonda360-clave-local-desarrollo"
)

DEBUG = os.environ.get("DEBUG", "False").lower() in ("true", "1", "yes")
>>>>>>> f0f4d1b (Corrige edicion de negocios y elimina Cloudinary)

ALLOWED_HOSTS = [
    "mesaredonda360.onrender.com",
    "localhost",
    "127.0.0.1",
]

<<<<<<< HEAD
=======
# Permite hosts adicionales configurados en Render.
>>>>>>> f0f4d1b (Corrige edicion de negocios y elimina Cloudinary)
hosts_extra = os.environ.get("ALLOWED_HOSTS", "")
if hosts_extra:
    ALLOWED_HOSTS.extend(
        host.strip()
        for host in hosts_extra.split(",")
        if host.strip()
    )


# =====================================================
# APLICACIONES
# =====================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "mapa",
]


# =====================================================
# MIDDLEWARE
# =====================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


<<<<<<< HEAD
# =====================================================
# URLS Y PLANTILLAS
# =====================================================
=======
# =========================================================
# URLS Y APLICACIÓN
# =========================================================
>>>>>>> f0f4d1b (Corrige edicion de negocios y elimina Cloudinary)

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# =====================================================
# BASE DE DATOS
<<<<<<< HEAD
# PostgreSQL en Render y SQLite local
# =====================================================
=======
# PostgreSQL en Render y SQLite como alternativa local.
# =========================================================
>>>>>>> f0f4d1b (Corrige edicion de negocios y elimina Cloudinary)

DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=DATABASE_URL.startswith("postgres"),
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# =====================================================
# VALIDACIÓN DE CONTRASEÑAS
# =====================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


<<<<<<< HEAD
# =====================================================
# IDIOMA Y ZONA HORARIA
# =====================================================
=======
# =========================================================
# IDIOMA, ZONA HORARIA Y FECHAS
# =========================================================
>>>>>>> f0f4d1b (Corrige edicion de negocios y elimina Cloudinary)

LANGUAGE_CODE = "es-pe"

TIME_ZONE = "America/Lima"

USE_I18N = True

USE_TZ = True


<<<<<<< HEAD
# =====================================================
# ARCHIVOS ESTÁTICOS
# =====================================================
=======
# =========================================================
# ARCHIVOS ESTÁTICOS
# CSS, JavaScript e imágenes propias del diseño.
# =========================================================
>>>>>>> f0f4d1b (Corrige edicion de negocios y elimina Cloudinary)

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage.CompressedManifestStaticFilesStorage"
        ),
    },
}


<<<<<<< HEAD
# =====================================================
# IMÁGENES Y ARCHIVOS SUBIDOS
# =====================================================
=======
# =========================================================
# ARCHIVOS SUBIDOS POR LOS USUARIOS
# =========================================================
>>>>>>> f0f4d1b (Corrige edicion de negocios y elimina Cloudinary)

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


<<<<<<< HEAD
# =====================================================
# CONFIGURACIÓN GENERAL
# =====================================================
=======
# =========================================================
# CLAVE PRIMARIA PREDETERMINADA
# =========================================================
>>>>>>> f0f4d1b (Corrige edicion de negocios y elimina Cloudinary)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


<<<<<<< HEAD
# =====================================================
# CORREO
# =====================================================

EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"
)
```
=======
# =========================================================
# CORREO ELECTRÓNICO
# =========================================================

EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"
)
>>>>>>> f0f4d1b (Corrige edicion de negocios y elimina Cloudinary)
