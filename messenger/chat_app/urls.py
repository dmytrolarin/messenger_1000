from .views import *
from django.urls import path

urlpatterns = [
    # У кожної групи є своя динамічна url адреса, що містить її pk
    path('chat_group/<int:chat_group_pk>', ChatView.as_view(), name="chat_group"),
    path('', GroupsView.as_view(), name="group_list"),
    path('personal_chats/',PersonalChatsView.as_view(), name="personal_chats")
]