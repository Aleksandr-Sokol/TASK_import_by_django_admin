from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
# pip install python-decouple
from decouple import config as decouple_config


class Command(BaseCommand):
    """
    Create new admin user
    username, email, password from .env file
    """

    def handle(self, *args, **options):
        admin_username = decouple_config('ADMIN_USERNAME')
        admin_email = decouple_config('ADMIN_EMAIL')
        admin_password = decouple_config('ADMIN_PASSWORD')
        if not len(User.objects.filter(username='root').all()):
            User.objects.create_superuser(admin_username, admin_email, admin_password)
            print(f'New admin user {admin_username} has been created')
