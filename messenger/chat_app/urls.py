from .views import *
from django.urls import path

urlpatterns = [
    path('', ChatView.as_view(), name="chat")
]