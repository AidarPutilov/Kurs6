from django import forms

from main.models import Client, Mailing, Message


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        # fields = '__all__'
        fields = ('email', 'fio', 'comment', 'is_active')
        # exclude = ('user',)


class ClientModeratorForm(forms.ModelForm):
    class Meta:
        model = Client
        # fields = '__all__'
        fields = ('is_active',)
        # exclude = ('user', )


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # fields = '__all__'
        fields = ('subject', 'text',)
        # exclude = ('in_stock',)


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        # fields = '__all__'
        fields = ('name', 'message', 'date_start', 'end_date', 'time_start', 'period', 'is_active',)
        # exclude = ('in_stock',)