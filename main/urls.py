from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views import (
    MailingHome,
    ClientCreateView,
    ClientDeleteView,
    ClientDetailView,
    ClientListView,
    ClientUpdateView,
    LogListView,
    MailingDeleteView,
    MailingDetailView,
    MailingListView,
    MailingUpdateView,
    MessageCreateView,
    MessageDeleteView,
    MessageListView,
    MessageUpdateView,
    # index,
    toggle_client_active,
    toggle_mailing_active,
    MailingCreateView,
    toggle_mailing_client,
    toggle_mailing_run,
)

app_name = MainConfig.name

urlpatterns = [
    path("", cache_page(60)(MailingHome.as_view()), name="main"),
    # Маршруты Client
    path("listclient/", ClientListView.as_view(), name="list_client"),
    path("clientactive/<int:pk>/", toggle_client_active, name="active_client"),
    path("client/<int:pk>", ClientDetailView.as_view(), name="detail_client"),
    path("createclient/", ClientCreateView.as_view(), name="create_client"),
    path("updateclient/<int:pk>", ClientUpdateView.as_view(), name="update_client"),
    path("deleteclient/<int:pk>", ClientDeleteView.as_view(), name="delete_client"),
    # Маршруты Message
    path("listmessage/", MessageListView.as_view(), name="list_message"),
    # path('client/<int:pk>', ClientDetailView.as_view(), name='view_client'),
    path("createmessage/", MessageCreateView.as_view(), name="create_message"),
    path("updatemessage/<int:pk>", MessageUpdateView.as_view(), name="update_message"),
    path("deletemessage/<int:pk>", MessageDeleteView.as_view(), name="delete_message"),
    # Маршруты Mailing
    path("listmailing/", MailingListView.as_view(), name="list_mailing"),
    path("activemailing/<int:pk>/", toggle_mailing_active, name="active_mailing"),
    path("runmailing/<int:pk>/", toggle_mailing_run, name="run_mailing"),
    path("detailmailing/<int:pk>", MailingDetailView.as_view(), name="detail_mailing"),
    path("createmailing/", MailingCreateView.as_view(), name="create_mailing"),
    path("updatemailing/<int:pk>", MailingUpdateView.as_view(), name="update_mailing"),
    path("deletemailing/<int:pk>", MailingDeleteView.as_view(), name="delete_mailing"),
    path(
        "clientmailing/<int:mailing_pk>&<int:client_pk>/",
        toggle_mailing_client,
        name="client_mailing",
    ),
    # Маршруты Log
    path("listlog/", LogListView.as_view(), name="list_log"),
]
