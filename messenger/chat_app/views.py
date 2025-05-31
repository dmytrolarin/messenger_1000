from django.shortcuts import redirect
from .forms import MessageForm
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .models import ChatGroup, ChatMessage


class ChatView(FormView):
    '''
    Клас, який відповідає за відображення конкретної чат-групи    
    '''
    template_name = "chat_app/chat.html"
    form_class = MessageForm

    def dispatch(self, request, *args, **kwargs):
        '''
        Метод, який першим приймає запит від веб-сервера, та з'ясовує який це тип запиту. 
        '''
        # Отримуємо об'єкт авторизованого користувача.
        user = request.user
        # Отримуємо pk групи з динамічної url адреси.
        chat_group_pk = self.kwargs['chat_group_pk']
        # Отримуємо об'єкт групи за її pk.
        chat_group = ChatGroup.objects.get(pk=chat_group_pk)
        # Якщо користувач є у списку учасників групи
        if user in chat_group.users.all():
            # Продовжуємо обробку запиту.
            return super().dispatch(request, *args, **kwargs)
        # Перенаправляємо користувача на головну сторінку.
        return redirect("group_list")
    
    def get_context_data(self, **kwargs):
        '''
        
        '''
        context = super().get_context_data(**kwargs)
        chat_group_pk = self.kwargs['chat_group_pk']
        context['chat_group'] = ChatGroup.objects.get(pk=chat_group_pk)
        context['chat_messages'] =  ChatMessage.objects.filter(chat_group_id = chat_group_pk)
        return context
    
    
class GroupsView(ListView):
    '''
    Клас, який відповідає за відображення всіх груп
    '''
    # Вказуємо модель, з якої беремо усі об'єкти груп
    model = ChatGroup
    template_name = "chat_app/group_list.html"