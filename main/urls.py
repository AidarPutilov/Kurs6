from django.urls import path

from main.apps import MainConfig
from main.views import ClientCreateView, ClientDeleteView, ClientListView, ClientUpdateView, index

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='main'),

    # Маршруты Client
    path('clientlist/', ClientListView.as_view(), name='clientlist'),
    # path('client/<int:pk>', ClientDetailView.as_view(), name='view_client'),
    path('createclient/', ClientCreateView.as_view(), name='create_client'),
    path('updateclient/<int:pk>', ClientUpdateView.as_view(), name='update_client'),
    path('deleteclient/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),

    # Маршруты Massage
    # path('listmessage/', MessageListView.as_view(), name='listmessage'),
    # path('client/<int:pk>', ClientDetailView.as_view(), name='view_client'),
    # path('createclient/', ClientCreateView.as_view(), name='create_client'),
    # path('updateclient/<int:pk>', ClientUpdateView.as_view(), name='update_client'),
    # path('deleteclient/<int:pk>', ClientDeleteView.as_view(), name='delete_client'),

]
