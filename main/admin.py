from django.contrib import admin

from main.models import Client, Mailing, Message

@admin.register(Client)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'fio', 'comment', 'user')
    # list_filter = ('fio',)
    # search_fields = ('name', 'description')


@admin.register(Message)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'text', 'user')
    # list_filter = ('fio',)
    # search_fields = ('name', 'description')


@admin.register(Mailing)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'date_start', 'time_start', 'period', 'message', 'status', 'user')
#     list_display = ('pk', 'name', 'date_start', 'time_start', 'period', 'message', 'clients', 'status', 'user')
#     list_filter = ('fio',)
#     search_fields = ('name', 'description')
