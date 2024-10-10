from django.contrib.auth.views import LoginView
from django.urls import include, path

from users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
    path("", LoginView.as_view(template_name="login.html"), name="login"),
]
