'''

'''
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .forms import MessageForm



class ChatConsumer(AsyncWebsocketConsumer):
    '''
    
    '''

    async def connect(self):
        '''

        '''
        #
        self.group_name = 'test_group'
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
        #
        await self.channel_layer.group_send(
            #
            self.group_name,
            {
                #
                "type": "send_message_to_chat",
                #
                "text_data": text_data,
            }
        )

    async def send_message_to_chat(self, event):
        '''
        
        '''
        #
        text_data_dict = json.loads(event["text_data"])
        #
        form = MessageForm(text_data_dict)
        #
        if form.is_valid():
            #
            await self.send(json.dumps(text_data_dict))
        else:
            print('error')
            
          