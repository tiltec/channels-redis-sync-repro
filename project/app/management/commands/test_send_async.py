import asyncio
import json
import datetime
import os

from channels.layers import get_channel_layer
from django.core.management.base import BaseCommand

from app import consumers


class Command(BaseCommand):
    """Test sending with async"""

    async def main(self):
        channel_layer = get_channel_layer()

        while True:
            await channel_layer.group_send(
                'test_room', {
                    'type': 'chat_message',
                    'message': datetime.datetime.now().isoformat()
                })
            print('number of open handles', len(os.listdir('/proc/self/fd')))
            await asyncio.sleep(0.1)

    def handle(self, *args, **options):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.main())
