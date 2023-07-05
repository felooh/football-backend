from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser using email as username'

    def handle(self, *args, **options):
        User = get_user_model()
        email = 'myblog@gmail.com'
        password = 'felixmwendia29'
        User.objects.create_superuser(email=email, password=password)
