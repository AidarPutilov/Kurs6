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


# class Massage(models.Model):
#     fio = models.CharField(
#         verbose_name='ФИО',
#         max_length=100,
#         help_text='Введите ФИО клиента'
#     )


#     user = models.ForeignKey(
#         AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         verbose_name='пользователь',
#         null=True, blank=True
#     )


# class Mailing(models.Model):
#     pass


# class Attempt(models.Model):
#     pass
