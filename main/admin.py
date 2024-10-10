from django.contrib import admin

from main.models import Client

@admin.register(Client)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'fio', 'comment', 'user')
    # list_filter = ('fio',)
    # search_fields = ('name', 'description')
