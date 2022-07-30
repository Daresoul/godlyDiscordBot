from multiprocessing import context
import discord
from discord.ext import commands
import heler_function

import settings

intents = discord.Intents.default()

bot = commands.Bot(command_prefix=settings.Prefix)
client = commands.Bot(command_prefix=settings.Prefix, help_command=None, intents=intents)


@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(settings.BotStatus))

async def writeHelp(channel):
    await channel.send('''
    Helper functions:
    ohPleaseAdmin nick @user <nick name>
    ''')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('ohPleaseAdmin'):
        content = message.content.split()

        print(content)

        if content[1] == "help":
            print("sending helper")
            await writeHelp(message.channel)

        if content[1] == "nick":
            member = message.mentions[0]
            await member.edit(nick=context[3])
    print('Message from {0.author}: {0.content}'.format(message))

client.run(settings.TOKEN)