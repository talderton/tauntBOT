import discord
from discord.ext import commands
import asyncio
import time

client = commands.Bot(command_prefix = '!')

def __init__(self, bot, guild):
    self.bot = bot
    self.guild_id = guild_id
    self.guild = guild
    self.player = None

@property
def voice(self):
    return self.guild.voice_client

@property
def voice_channel(self):
    if self.voice is None:
        return None
    else:
        return self.voice.channel

@client.command(pass_context = True)
async def taunt(context):

    voice_channel = None
    voice_channel = context.author.voice.channel

    if voice_channel != None:
        print(voice_channel.id)
        await voice_channel.connect()

        #create StreamPlayer
        channel = context.voice_client
        player = channel.play(discord.FFmpegPCMAudio("0001.mp3"), after = lambda: print("Done"))
        #player.start()

        while not player.is_done():
            await asyncio.sleep(1)
        #disconnect after player is finished
        player.stop()
        await voice_channel.disconnect()

    else:
        await client.say("User is not in a channel.")

@client.command()
async def ping(context):
    await context.send(f"Pong! {round(client.latency*1000)}ms")

@client.event
async def on_ready():
    print("Start the game already!")

client.run('NzE1MzQxNzM1OTk5NDM4ODk5.Xs719w.j23fXuTFy2KUnAw6_TE7ha6J_Hc')
