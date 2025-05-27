'''

'''
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .forms import MessageForm
from channels.db import database_sync_to_async
from .models import ChatGroup, ChatMessage


class ChatConsumer(AsyncWebsocketConsumer):
    '''
    
    '''

    async def connect(self):
        '''

        '''
        self.chat_group_pk = self.scope["url_route"]["kwargs"]["chat_group_pk"]
        #
        self.group_name = str(self.chat_group_pk)
        #
        await self.channel_layer.group_add(
            #
            self.group_name,
            #
            self.channel_name 
        )
        #
        await self.accept()
        print('Підключення успішне')

    async def receive(self, text_data):
        '''
        
        '''
        
        self.user = self.scope["user"]
        username = self.user.username
        saved_message = await self.save_message(message = json.loads(text_data)['message'])
        #
        await self.channel_layer.group_send(
            #
            self.group_name,
            {
                #
                "type": "send_message_to_chat",
                #
                "text_data": text_data,
                "username": username,
                "date_time": saved_message.date_time
            }
        )

    async def send_message_to_chat(self, event):
        '''
        
        '''
        
        #
        text_data_dict = json.loads(event["text_data"])
        username = event["username"]
        text_data_dict['username'] = username
        text_data_dict["date_time"] = event["date_time"].isoformat()

        # text_data_dict['username']
        #
        form = MessageForm(text_data_dict)
        #
        if form.is_valid():
            #
            await self.send(json.dumps(text_data_dict))
        else:
            print('error')
            
    @database_sync_to_async
    def save_message(self, message):
        author = self.scope['user']
        message = message
        group = ChatGroup.objects.get(pk = self.group_name)
        return ChatMessage.objects.create(author = author, content = message, chat_group = group)
          