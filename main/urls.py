from django.urls import path

from main.apps import MainConfig
from main.views import ClientCreateView, ClientDeleteView, ClientDetailView, ClientListView, ClientUpdateView, MailingDeleteView, MailingDetailView, MailingListView, MailingUpdateView, MessageCreateView, MessageDeleteView, MessageListView, MessageUpdateView, index, toggle_client_active, toggle_mailing_active, MailingCreateView

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='main'),

    # Маршруты Client
    path('listclient/', ClientListView.as_view(), name='list_client'),
    path('clientactive/<int:pk>/', toggle_client_active, name='active_client'),
    path('client/<int:pk>', ClientDetailView.as_view(), name='detail_client'),
    path('createclient/', ClientCreateView.as_view(), name='create_client'),
    path('updateclient/<int:pk>', ClientUpdateView.as_view(), name='update_client'),
    path('deleteclient/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),

    # Маршруты Message
    path('listmessage/', MessageListView.as_view(), name='list_message'),
    # path('client/<int:pk>', ClientDetailView.as_view(), name='view_client'),
    path('createmessage/', MessageCreateView.as_view(), name='create_message'),
    path('updatemessage/<int:pk>', MessageUpdateView.as_view(), name='update_message'),
    path('deletemessage/<int:pk>', MessageDeleteView.as_view(), name='delete_message'),

    # Маршруты Mailing
    path('listmailing/', MailingListView.as_view(), name='list_mailing'),
    path('activemailing/<int:pk>/', toggle_mailing_active, name='active_mailing'),
    path('detailmailing/<int:pk>', MailingDetailView.as_view(), name='detail_mailing'),
    path('createmailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('updatemailing/<int:pk>', MailingUpdateView.as_view(), name='update_mailing'),
    path('deletemailing/<int:pk>', MailingDeleteView.as_view(), name='delete_mailing'),
]
