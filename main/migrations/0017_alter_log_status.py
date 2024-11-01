# Generated by Django 5.1.1 on 2024-10-30 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_log_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='status',
            field=models.CharField(choices=[('success', 'Успешно'), ('fail', 'Ошибка')], default='success', verbose_name='Статус'),
        ),
    ]