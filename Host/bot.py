import asyncio

import discord
from typing import List
import os

import pinger


def start_loop(loop, gen):
    loop.run_until_complete(gen)


class Bot(discord.Client):
    def __init__(self, loop, state_event, **kwargs):
        super().__init__(**kwargs)
        asyncio.set_event_loop(loop)
        try:
            self.secret = open("secret", "r").readline().strip("\n")
        except FileNotFoundError:
            self.secret = os.environ['BOT_TOKEN']
        self.subscribed_channels: List[discord.DMChannel] = []
        self.state_event = state_event

    async def on_message(self, message: discord.Message):
        if message.content == "!connect":
            if message.channel.type == discord.ChannelType.private:
                if message.channel in self.subscribed_channels:
                    await message.channel.send("Already Connected!")
                    return
                self.subscribed_channels.append(message.channel)
                await message.channel.send("Connected!")
        if message.channel.id == 683637393412456456 and message.author.id == 923900149300854804:
            await self.broadcast_change(self.state_event)

    async def broadcast_change(self, event: pinger.ChangeState):
        for channel in self.subscribed_channels:
            await channel.send("My WiFi is now " + event.new_state), asyncio.get_event_loop()
            event.clear()
