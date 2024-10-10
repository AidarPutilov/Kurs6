from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

from users.apps import UsersConfig
from users.views import ProfileView, UserCreateView, email_verification, password_reset


app_name = UsersConfig.name

urlpatterns = [
    path("", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path('password_reset/', password_reset, name='reset_password'),
]
