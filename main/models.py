from django.db import models

from config.settings import AUTH_USER_MODEL


class Client(models.Model):
    email = models.EmailField(
        verbose_name="электронная почта",
        unique=True,
        help_text="Введите электронный адрес клиента",
    )
    fio = models.CharField(
        verbose_name="ФИО", max_length=100, help_text="Введите ФИО клиента"
    )
    comment = models.TextField(
        verbose_name="комментарий",
        help_text="Введите комментарий",
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"
        ordering = ("fio",)
        permissions = [
            ("can_edit_is_active_client", "Can edit active clients"),
            ("can_view_client_list", "Can view client list"),
        ]


class Message(models.Model):
    subject = models.CharField(
        verbose_name="тема сообщения", max_length=100, help_text="Введите тему"
    )
    text = models.TextField(verbose_name="текст сообщения", help_text="Введите текст")
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"
        ordering = ("subject",)


class Mailing(models.Model):
    PERIODS = (
        ("day", "день"),
        ("week", "неделя"),
        ("mon", "месяц"),
    )
    STATUSES = (
        ("created", "создана"),
        ("started", "запущена"),
        ("completed", "завершена"),
    )
    name = models.CharField(
        max_length=100,
        verbose_name="название",
        help_text="Введите название рассылки",
    )
    time_start = models.TimeField(
        verbose_name="время отправки",
        help_text="Введите время (ЧЧ:ММ)",
    )
    date_start = models.DateField(
        verbose_name="дата отправки",
        help_text="Введите дату (ДД.ММ.ГГ)",
    )
    end_date = models.DateField(
        verbose_name="Дата окончания рассылки", null=True, blank=True
    )
    period = models.CharField(
        max_length=20,
        choices=PERIODS,
        default="day",
        verbose_name="периодичность",
        help_text="Выберите периодичность",
    )
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        verbose_name="сообщение",
        help_text="Выберите сообщение",
    )
    clients = models.ManyToManyField(
        Client, related_name="clients", verbose_name="клиенты"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUSES,
        default="created",
        verbose_name="статус",
    )
    user = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"
        ordering = ("period",)
        permissions = [
            ("can_edit_is_active_mailing", "Can edit active mailing"),
            ("can_change_clients_mailing", "Can change clients mailing"),
        ]


class Log(models.Model):
    STATUSES = (
        ("success", "success"),
        ("fail", "fail"),
    )
    last_try = models.DateField(
        auto_now_add=True, verbose_name="Дата последней попытки рассылки"
    )
    status = models.CharField(
        choices=STATUSES, default="success", verbose_name="Статус"
    )
    response = models.TextField(
        verbose_name="Ответ",
        null=True,
        blank=True,
    )
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        related_name="mailings",
        verbose_name="Рассылка",
    )

    class Meta:
        verbose_name = "попытка рассылки"
        verbose_name_plural = "попытки рассылки"
        ordering = ("last_try",)

    def __str__(self):
        return f"{self.mailing}: {self.status}"
