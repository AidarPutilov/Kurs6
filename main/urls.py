from django.urls import path

from main.apps import MainConfig
from main.views import ClientCreateView, ClientDeleteView, ClientDetailView, ClientListView, ClientUpdateView, MailingListView, MessageCreateView, MessageDeleteView, MessageListView, MessageUpdateView, index, toggle_client_active

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='main'),

    # Маршруты Client
    path('clientlist/', ClientListView.as_view(), name='clientlist'),
    path('client_active/<int:pk>/', toggle_client_active, name='active_client'),
    path('client/<int:pk>', ClientDetailView.as_view(), name='detail_client'),
    path('createclient/', ClientCreateView.as_view(), name='create_client'),
    path('updateclient/<int:pk>', ClientUpdateView.as_view(), name='update_client'),
    path('deleteclient/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),

    # Маршруты Message
    path('listmessage/', MessageListView.as_view(), name='listmessage'),
    # path('client/<int:pk>', ClientDetailView.as_view(), name='view_client'),
    path('createmessage/', MessageCreateView.as_view(), name='create_message'),
    path('updatemessage/<int:pk>', MessageUpdateView.as_view(), name='update_message'),
    path('deletemessage/<int:pk>', MessageDeleteView.as_view(), name='delete_message'),

    # Маршруты Mailing
    path('listmailing/', MailingListView.as_view(), name='listmailing'),
    # path('client/<int:pk>', ClientDetailView.as_view(), name='view_client'),
    # path('createmessage/', MailingCreateView.as_view(), name='create_mailing'),
    # path('updatemessage/<int:pk>', MailingUpdateView.as_view(), name='update_mailing'),
    # path('deletemessage/<int:pk>', MailingDeleteView.as_view(), name='delete_mailing'),
]
