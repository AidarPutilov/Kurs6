
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
        fields = ("name", )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
