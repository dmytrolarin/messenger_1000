from django.db import models
from django.contrib.auth.models import User


class ChatGroup(models.Model):
    '''
    Модель ChatGroup, в якій зберігаються Chat-групи
    '''
    name = models.CharField(max_length = 255)
    users = models.ManyToManyField(User)
    
    
class ChatMessage(models.Model):
    '''
    Модель для повідомлень
    '''
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)