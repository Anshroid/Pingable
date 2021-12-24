import threading
import asyncio
import requests

import bot
import pinger


class ControlThread(threading.Thread):
    def __init__(self, state_event: pinger.ChangeState, client: bot.Bot):
        super(ControlThread, self).__init__()
        self.state_event = state_event
        self.client = client

    def run(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        while True:
            self.state_event.wait()
            requests.post(
                b"https://discord.com/api/webhooks/923900149300854804/Khxi6oJTvFw87JYYtmdiZk5z8BN7qJV6cNac3nSaWhoHGFpJXrRlNBoB6YSvFKFQxzRL",
                json={"content": "notify"}
            )
            self.state_event.clear()
