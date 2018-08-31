import json
import time
import datetime
import os

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.management.base import BaseCommand

from app import consumers


class Command(BaseCommand):
    """Test sending with async_to_sync"""

    def handle(self, *args, **options):
        channel_layer = get_channel_layer()

        while True:
            async_to_sync(channel_layer.group_send)(
                'test_room', {
                    'type': 'chat_message',
                    'message': datetime.datetime.now().isoformat()
                })
            print('number of open handles', len(os.listdir('/proc/self/fd')))
            time.sleep(0.1)
