from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        emails = [
            "admin@sky.pro",
            "user@sky.pro",
            "man@sky.pro"
        ]
        for email_str in emails:
            #User.objects.filter(email=email_str).exists()
            if not User.objects.filter(email=email_str).exists():
                user = User.objects.create(email=email_str)
                user.set_password("123qwe")
                user.is_active = True
                if 'admin' in email_str:
                    user.is_staff = True
                    user.is_superuser = True
                user.save()
