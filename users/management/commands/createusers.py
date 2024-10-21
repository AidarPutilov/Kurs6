from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # Список пользователей ('эл.адрес', 'название', 'пароль')
        users_list = [
            ("admin@sky.pro", "Admin", "123"),
            ("user@sky.pro", "User", "123"),
            ("man@sky.pro", "Manager", "123"),
        ]

        # Список групп [('название', ('пользователи',), ('разрешения',))]
        groups_list = [
            ("Manager",
                ("Manager",),
                ("can_view_users_list",
                 "can_edit_is_active_user",
                 "can_edit_is_active_mailing",
                 "view_mailing",
                 )
            )
        ]

        # Создание групп
        for group_item in groups_list:
            if not Group.objects.filter(name=group_item[0]).exists():
                group = Group.objects.create(name=group_item[0])
            else:
                group = Group.objects.get(name=group_item[0])

            # Назначение разрешений
            for group_perm in group_item[2]:
                # perms = Permission.objects.get(codename="can_view_users_list")
                perms = Permission.objects.get(codename=group_perm)
                group.permissions.add(perms)


        # Создание пользователей
        for user_item in users_list:

            # Проверка наличия пользователя, иначе создание
            if not User.objects.filter(email=user_item[0]).exists():
                user = User.objects.create(email=user_item[0])
            else:
                user = User.objects.get(email=user_item[0])

            # Установка параметров
            user.set_password(user_item[2])
            user.name = user_item[1]
            user.is_active = True

            # Особые параметры для администратора
            if user_item[1] == "Admin":
                user.is_staff = True
                user.is_superuser = True
            user.save()

        # Добавление пользователей в группы
        for group_item in groups_list:
            group = Group.objects.get(name=group_item[0])
            for user_item in group_item[1]:
                user = User.objects.get(name=user_item)
                user.groups.add(group)
