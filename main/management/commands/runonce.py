from django.core.management import BaseCommand

from main.task import send_mailings


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        send_mailings()
