from django.db import models

from config.settings import AUTH_USER_MODEL

class Client(models.Model):
    email = models.EmailField(
        verbose_name='электронная почта',
        unique=True
    )
    fio = models.CharField(
        max_length=100,
        verbose_name='ФИО'
    )
    comment = models.TextField(
        verbose_name='комментарий',
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


# class MailingList(models.Model):
#     pass


# class Massage(models.Model):
#     pass


# class Attempt(models.Model):
#     pass
