# Generated by Django 5.1.1 on 2024-11-05 01:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("main", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="пользователь",
            ),
        ),
        migrations.AddField(
            model_name="mailing",
            name="clients",
            field=models.ManyToManyField(
                related_name="clients", to="main.client", verbose_name="клиенты"
            ),
        ),
        migrations.AddField(
            model_name="mailing",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="пользователь",
            ),
        ),
        migrations.AddField(
            model_name="log",
            name="mailing",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mailings",
                to="main.mailing",
                verbose_name="Рассылка",
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="пользователь",
            ),
        ),
        migrations.AddField(
            model_name="mailing",
            name="message",
            field=models.ForeignKey(
                help_text="Выберите сообщение",
                on_delete=django.db.models.deletion.CASCADE,
                to="main.message",
                verbose_name="сообщение",
            ),
        ),
    ]
