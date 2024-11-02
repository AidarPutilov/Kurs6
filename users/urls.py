from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

from main.views import ClientUpdateView
from users.apps import UsersConfig
from users.views import (
    ProfileView,
    UserCreateView,
    UserDeleteView,
    UserDetailView,
    UserListView,
    UserUpdateView,
    email_verification,
    password_reset,
    toggle_user_active,
)


app_name = UsersConfig.name

urlpatterns = [
    path("", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path("password_reset/", password_reset, name="reset_password"),
    path("listusers/", UserListView.as_view(), name="list_users"),
    path("activeusers/<int:pk>/", toggle_user_active, name="active_users"),
    path('detailusers/<int:pk>', UserDetailView.as_view(), name='detail_users'),
    path('updateusers/<int:pk>', UserUpdateView.as_view(), name='update_users'),
    path('deleteusers/<int:pk>', UserDeleteView.as_view(), name='delete_users'),
]
