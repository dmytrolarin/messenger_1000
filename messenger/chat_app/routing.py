'''

'''
from django.urls import path
from .consumers import ChatConsumer

#
websocket_urlpatterns = [
    #
    path("chat_group/<int:chat_group_pk>", ChatConsumer.as_asgi())
]

