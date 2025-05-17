from django.shortcuts import render
from .forms import MessageForm
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .models import ChatGroup

class ChatView(FormView):
    template_name = "chat_app/chat.html"
    form_class = MessageForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        chat_group_pk = self.kwargs['chat_group_pk']
        context['chat_group'] = ChatGroup.objects.get(pk=chat_group_pk)
        return context
    
    
class GroupsView(ListView):
    model = ChatGroup
    template_name = "chat_app/group_list.html"