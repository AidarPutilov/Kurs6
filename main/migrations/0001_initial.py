# Generated by Django 5.1.1 on 2024-11-05 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Введите электронный адрес клиента",
                        max_length=254,
                        unique=True,
                        verbose_name="электронная почта",
                    ),
                ),
                (
                    "fio",
                    models.CharField(
                        help_text="Введите ФИО клиента",
                        max_length=100,
                        verbose_name="ФИО",
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        help_text="Введите комментарий",
                        null=True,
                        verbose_name="комментарий",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="активен"),
                ),
            ],
            options={
                "verbose_name": "клиент",
                "verbose_name_plural": "клиенты",
                "ordering": ["fio"],
                "permissions": [
                    ("can_edit_is_active_client", "Can edit active clients")
                ],
            },
        ),
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_try",
                    models.DateField(
                        auto_now_add=True,
                        verbose_name="Дата последней попытки рассылки",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("success", "Успешно"), ("fail", "Ошибка")],
                        default="success",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "response",
                    models.TextField(blank=True, null=True, verbose_name="Ответ"),
                ),
                (
                    "client",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="Клиент"
                    ),
                ),
            ],
            options={
                "verbose_name": "попытка рассылки",
                "verbose_name_plural": "попытки рассылки",
                "ordering": ["-last_try"],
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите название рассылки",
                        max_length=100,
                        verbose_name="название",
                    ),
                ),
                (
                    "time_start",
                    models.TimeField(
                        help_text="Введите время (ЧЧ:ММ)", verbose_name="время отправки"
                    ),
                ),
                (
                    "date_start",
                    models.DateField(
                        help_text="Введите дату (ДД.ММ.ГГ)",
                        verbose_name="дата отправки",
                    ),
                ),
                (
                    "end_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Дата окончания рассылки"
                    ),
                ),
                (
                    "period",
                    models.CharField(
                        choices=[("day", "день"), ("week", "неделя"), ("mon", "месяц")],
                        default="day",
                        help_text="Выберите периодичность",
                        max_length=20,
                        verbose_name="периодичность",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("created", "создана"),
                            ("started", "запущена"),
                            ("completed", "завершена"),
                        ],
                        default="created",
                        max_length=20,
                        verbose_name="статус",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="активен"),
                ),
            ],
            options={
                "verbose_name": "рассылка",
                "verbose_name_plural": "рассылки",
                "ordering": ["date_start", "time_start"],
                "permissions": [
                    ("can_edit_is_active_mailing", "Can edit active mailing"),
                    ("can_change_clients_mailing", "Can change clients mailing"),
                ],
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subject",
                    models.CharField(
                        help_text="Введите тему",
                        max_length=100,
                        verbose_name="тема сообщения",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        help_text="Введите текст", verbose_name="текст сообщения"
                    ),
                ),
            ],
            options={
                "verbose_name": "сообщение",
                "verbose_name_plural": "сообщения",
                "ordering": ["subject"],
            },
        ),
    ]
