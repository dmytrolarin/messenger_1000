from django.shortcuts import render
from .forms import MessageForm
from django.views.generic.edit import FormView
# Create your views here.
class ChatView(FormView):
    template_name = "chat_app/chat.html"
    form_class = MessageForm