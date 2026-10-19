
import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Crea el administrador inicial si no existe."

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not username or not email or not password:
            raise CommandError(
                "Configura DJANGO_SUPERUSER_USERNAME, "
                "DJANGO_SUPERUSER_EMAIL y DJANGO_SUPERUSER_PASSWORD "
                "en las variables de entorno de Render."
            )

        user = User.objects.filter(username=username).first()

        if user:
            if not user.is_superuser:
                raise CommandError(
                    "El usuario configurado ya existe y no es administrador."
                )

            self.stdout.write(
                self.style.SUCCESS(
                    "El administrador ya existe. No se creó otro."
                )
            )
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS("Administrador creado correctamente.")
        )