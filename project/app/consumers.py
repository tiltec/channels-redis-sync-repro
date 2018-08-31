from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

channel_name = None


class Consumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)('test_room',
                                                    self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)('test_room',
                                                        self.channel_name)

    def receive(self, text_data):
        pass

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({'message': message}))
