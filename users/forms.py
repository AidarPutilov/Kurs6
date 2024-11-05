from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "name", "password1", "password2")


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("name",)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields["password"].widget = forms.HiddenInput()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ("name", "is_active")
        # exclude = ('user',)
