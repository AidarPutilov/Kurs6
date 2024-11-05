from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Введите Email",
    )
    name = models.CharField(
        max_length=20,
        verbose_name="имя",
        help_text="Введите имя",
        blank=True,
        null=True,
    )
    token = models.CharField(
        max_length=100, verbose_name="токен", blank=True, null=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="активен",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering = ("name",)
        permissions = [
            ("can_view_users_list", "Can view users list"),
            ("can_edit_is_active_user", "Can edit active user"),
        ]

    def __str__(self):
        return self.name
