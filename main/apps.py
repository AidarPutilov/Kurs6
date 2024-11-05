from time import sleep
from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

    def ready(self) -> None:
        from main.task import send_mailings

        sleep(2)
        try:
            send_mailings()
        except:
            pass
