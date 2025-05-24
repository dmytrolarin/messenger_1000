from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ChatGroup(models.Model):
    name = models.CharField(max_length = 255)
    users = models.ManyToManyField(User)
    
    
class ChatMessage(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)