from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users_list = [
            ("admin@sky.pro", "Admin"),
            ("user@sky.pro", "User"),
            ("man@sky.pro", "Manager"),
        ]
        for item in users_list:
            #User.objects.filter(email=email_str).exists()

            if not User.objects.filter(email=item[0]).exists():
                user = User.objects.create(email=item[0])
            else:
                user = User.objects.get(email=item[0])

            user.set_password("123qwe")
            user.name = item[1]
            user.is_active = True
            if item[1] == "Admin":
                user.is_staff = True
                user.is_superuser = True
            user.save()
