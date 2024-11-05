# Generated by Django 5.1.1 on 2024-10-13 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_alter_mailing_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={
                "ordering": ("fio",),
                "permissions": [
                    ("can_edit_is_active_client", "Can edit active clients")
                ],
                "verbose_name": "клиент",
                "verbose_name_plural": "клиенты",
            },
        ),
        migrations.AlterModelOptions(
            name="mailing",
            options={
                "ordering": ("period",),
                "permissions": [
                    ("can_edit_is_active_mailing", "Can edit active mailing"),
                    ("can_change_clients_mailing", "Can change clients mailing"),
                    ("can_view_clients_mailing", "Can view clients mailing"),
                ],
                "verbose_name": "рассылка",
                "verbose_name_plural": "рассылки",
            },
        ),
    ]
