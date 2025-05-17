from .views import *
from django.urls import path

urlpatterns = [
    path('chat_group/<int:chat_group_pk>', ChatView.as_view(), name="chat_group"),
    path('', GroupsView.as_view(), name="group_list")
]