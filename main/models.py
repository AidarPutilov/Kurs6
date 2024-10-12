from django.db import models

from config.settings import AUTH_USER_MODEL

class Client(models.Model):
    email = models.EmailField(
        verbose_name='электронная почта',
        unique=True,
        help_text='Введите электронный адрес клиента'
    )
    fio = models.CharField(
        verbose_name='ФИО',
        max_length=100,
        help_text='Введите ФИО клиента'
    )
    comment = models.TextField(
        verbose_name='комментарий',
        help_text='Введите комментарий',
        null=True, blank=True
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
        null=True, blank=True
    )

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    subject = models.CharField(
        verbose_name='тема сообщения',
        max_length=100,
        help_text='Введите тему'
    )
    text = models.TextField(
        verbose_name='текст сообщения',
        help_text='Введите текст'
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
        null=True, blank=True
    )

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    PERIODS = (
        ('day', 'день'),
        ('week', 'неделя'),
        ('mon', 'месяц'),
    )
    STATUSES = (
        ('created', 'создана'),
        ('started', 'запущена'),
        ('completed', 'завершена'),
    )
    name = models.CharField(
        max_length=100,
        verbose_name='название',
        help_text='Введите название рассылки',
    )
    time_start = models.TimeField(
        verbose_name='время отправки',
        help_text='Введите время (ЧЧ:ММ)',
    )
    date_start = models.DateField(
        verbose_name="дата отправки",
        help_text='Введите дату (ДД.ММ.ГГ)',
    )
    period = models.CharField(
        max_length=20,
        choices=PERIODS,
        verbose_name='периодичность',
        help_text='Выберите периодичность',
    )
    message = models.ForeignKey(
        Message,
        on_delete = models.CASCADE,
        verbose_name='сообщение',
        help_text='Выберите сообщение',
    )
    clients = models.ManyToManyField(
        Client,
        related_name='clients',
        verbose_name='клиенты'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUSES,
        verbose_name='статус',
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
        null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


# class Log(models.Model):
#     pass
