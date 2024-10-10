from dataclasses import field
from django import forms
from django.db.models import BooleanField

from main.models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        # fields = '__all__'
        fields = ('email', 'fio', 'comment',)
        # exclude = ('in_stock',)