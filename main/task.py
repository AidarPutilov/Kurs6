from datetime import datetime, date, time, timedelta

from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from main.models import Mailing, Log, Client


def mailing_for_send():
    """Возвращает рассылки для отправки на текущий момент"""

    selected_mailings = []

    # Текущие дата и время
    current_datetime = datetime.now()

    # Список активных рассылок
    mailings = Mailing.objects.filter(is_active=True)

    for item in mailings:

        # Дата окончания рассылки
        end_date = item.end_date

        # Дата и время отправки
        mailing_datetime = datetime.combine(item.date_start, item.time_start)

        # Если указана дата окончания рассылки
        if end_date:
            end_datetime = datetime.combine(item.end_date, time(23, 59, 59))
            if mailing_datetime < current_datetime < end_datetime:
                selected_mailings.append(item)

        # Если не указана дата окончания рассылки
        else:
            if mailing_datetime < current_datetime:
                selected_mailings.append(item)

    return selected_mailings


def send_mailing(mailing: Mailing):
    """Отправка рассылки"""

    subject = mailing.message.subject
    text = mailing.message.text
    emails = mailing.clients.filter(is_active=True).values_list("email", flat=True)

    # Отправка писем по одному
    for email in emails:
        client_str = f"{Client.objects.get(email=email)} ({email})"
        try:
            print(f"Send mail '{subject}' to {email}")
            send_mail(
                subject=subject,
                message=text,
                from_email=EMAIL_HOST_USER,
                recipient_list=[email],
            )
        except:
            Log.objects.create(mailing=mailing, status="fail", client=client_str)
        else:
            Log.objects.create(mailing=mailing, client=client_str)


def send_mailings():
    """Отправка рассылок"""

    #
    mailings = mailing_for_send()

    for mailing in mailings:

        # Смена статуса
        mailing.status = "started"

        # Отправка писем
        send_mailing(mailing)

        # Смена статуса
        mailing.status = "completed"

        # Обновление даты отправки
        if mailing.period == "week":
            tdelta = timedelta(days=7)
        elif mailing.period == "mon":
            tdelta = timedelta(days=30)
        else:
            tdelta = timedelta(days=1)
        mailing.date_start = date.today() + tdelta
        mailing.save()
