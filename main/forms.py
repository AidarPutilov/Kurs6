from django import forms

from main.models import Client, Message


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        # fields = '__all__'
        fields = ('email', 'fio', 'comment', 'is_active')
        # exclude = ('in_stock',)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # fields = '__all__'
        fields = ('subject', 'text',)
        # exclude = ('in_stock',)