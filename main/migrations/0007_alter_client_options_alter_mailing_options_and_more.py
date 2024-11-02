# Generated by Django 5.1.1 on 2024-10-13 21:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_mailing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('fio',), 'permissions': [('can_edit_is_active_client', 'can edit active clients')], 'verbose_name': 'клиент', 'verbose_name_plural': 'клиенты'},
        ),
        migrations.AlterModelOptions(
            name='mailing',
            options={'ordering': ('period',), 'permissions': [('can_edit_is_active_mailing', 'can edit active mailing')], 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('subject',), 'verbose_name': 'сообщение', 'verbose_name_plural': 'сообщения'},
        ),
        migrations.AddField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mailing',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания рассылки'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='period',
            field=models.CharField(choices=[('day', 'день'), ('week', 'неделя'), ('mon', 'месяц')], default='day', help_text='Выберите периодичность', max_length=20, verbose_name='периодичность'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('created', 'создана'), ('started', 'запущена'), ('completed', 'завершена')], default='created', max_length=20, verbose_name='статус'),
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_try', models.DateField(auto_now_add=True, verbose_name='Дата последней попытки рассылки')),
                ('status', models.CharField(choices=[('success', 'success'), ('fail', 'fail')], default='success', verbose_name='Статус')),
                ('response', models.TextField(blank=True, null=True, verbose_name='Ответ')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mailings', to='main.mailing', verbose_name='Рассылка')),
            ],
            options={
                'verbose_name': 'попытка рассылки',
                'verbose_name_plural': 'попытки рассылки',
                'ordering': ('last_try',),
            },
        ),
    ]
