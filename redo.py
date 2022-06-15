import discord
from discord.ext import commands
import asyncio
import time

client = commands.Bot(command_prefix = "!")

class def Audio_Player:

    def __init__(self, bot, guild):
        self.bot = bot
        self.guild_id = guild
        self.guild = guild
        self.player = None

    @property
    def voice(self):
        return self.guild.voice_client

    @property
    def voice_channel(self):
        if self.voice is None
            return None
        else:
            return self.voice.channel

    def update_guild(self):
        self.guild = await self.bot.fetch_guild(self.guild.id)

    async def connect(self, channel):
        if not is_instance(channel, discord.VoiceChannel):
            channel = self.bot.get_channel(channel)

            voice = self.voice

            if voice is None:
                print(f"Attempting to connect to: {channel.id}")
                await channel.connect()
                print(f"Finished connecting to: {channel.id}")
            elif voice.channel and voice.channel.id == channel.id:
                print(f"Disconnecting and reconnecting to: {channel.id}")
                await voice.disconnect(force = True)
                await asyncio.sleep(1)
                await channel.connect()
                print(f"Finished reconnecting to: {channel.id}")
            else:
                print(f"Attempting to move to: {channel.id}")
                await voice.move_to(channel.id)
                print(f"Finished move to: {channel.id}")