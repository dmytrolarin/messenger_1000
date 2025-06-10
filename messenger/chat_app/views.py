from django.shortcuts import redirect
from .forms import MessageForm
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .models import ChatGroup, ChatMessage
from django.contrib.auth.models import User


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
            # Отримпуємо усі повідомлення, що знаходяться у цій групі
            all_messages = ChatMessage.objects.filter(chat_group = chat_group)
            # Перебараємо усі повідомлення
            for message in all_messages:
                # Додаємо корисстувача у поле views за зв'язком ManyToMany
                message.views.add(user)
                # Збрегіаємо зв'язок з користувачем у БД
                message.save()
            # Продовжуємо обробку запиту.
            return super().dispatch(request, *args, **kwargs)
        # Перенаправляємо користувача на головну сторінку.
        return redirect("group_list")
    
    def get_context_data(self, **kwargs):
        '''
            Метод для додавання у контекст для класів відображення
        '''

        # Отримуємо об'єкт контексту з батьківського класу FormView 
        context = super().get_context_data(**kwargs)
        # Отримуємо pk групи з kwargs (Тобто з дінамічного url адрессу)
        chat_group_pk = self.kwargs['chat_group_pk']
        # Додаємо у контекст групу
        context['chat_group'] = ChatGroup.objects.get(pk=chat_group_pk)
        # Додаємо у контекст усі повідомлення групи
        context['chat_messages'] =  ChatMessage.objects.filter(chat_group_id = chat_group_pk)
        # повертаємо контекст зі змінами
        return context
    
    
class GroupsView(ListView):
    '''
    Клас, який відповідає за відображення всіх груп
    '''

    template_name = "chat_app/group_list.html"

    def get_queryset(self):
        '''
        Метод, який повертає список об'єктів, що передадуться у шаблон
        '''
        #Повертає усі групи, які не є персональними чатами
        return ChatGroup.objects.filter(personal_chat = False)

class PersonalChatsView(ListView):
    '''
    Класс відображення для особистих чатів
    '''
    template_name = 'chat_app/personal_chat.html'

    def get_queryset(self):
        #Повертаємо усіх користувачів, окрім авторизованого користувача
        return User.objects.exclude(pk = self.request.user.pk)
    
def create_chat(request, user_pk):
    '''
    Функція, яка отримує або створює персональний чат
    '''

    # Отримуємо користувача, до якого під'єднуєтья поточний користувач
    user_to_connect = User.objects.get(pk=user_pk)
    # Отримуємо поточного користувача
    current_user = User.objects.get(pk=request.user.pk)
    # Персональні чати, до яких до яких під'єднан користувач, з яким ми створюємо зв'язок
    groups_of_user_to_connect = ChatGroup.objects.filter(users=user_to_connect,personal_chat=True)
    # Отримуємо песрональний чат, до якої під'єднані обидва користувачі
    group_personal_chat = groups_of_user_to_connect.filter(users = current_user).first()
    # Перевіряємо чи є цей чат у БД
    if not group_personal_chat:
        # Створюємо персональний чат з користувачами
        group_personal_chat = ChatGroup.objects.create(
            name=f'personal, users: {current_user}-{user_to_connect}',
            personal_chat=True
        )
        # Зберігаємо користувачів у персональний чат
        group_personal_chat.users.set([current_user,user_to_connect])
        # Зберігаємо зміни у персональному чаті
        group_personal_chat.save()
    # Перенаправляємо користувача на сторінку цього чату
    return redirect("chat_group",group_personal_chat.pk)