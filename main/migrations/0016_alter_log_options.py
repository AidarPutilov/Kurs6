# Generated by Django 5.1.1 on 2024-10-30 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0015_alter_client_options_alter_log_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="log",
            options={
                "ordering": ["-last_try"],
                "verbose_name": "попытка рассылки",
                "verbose_name_plural": "попытки рассылки",
            },
        ),
    ]
