from tokenize import String
import discord
from discord.ext import commands

import settings

discord_bot = commands.Bot(command_prefix='ohPleaseAdmin ')

@discord_bot.command(name='ping')
async def ping(ctx):
    await ctx.send("PONG")

@discord_bot.command(name='nick')
async def change_name(ctx, member : discord.Member, arg):
    await member.edit(nick=arg)
    await ctx.send("Name has been changed to: " + arg)

discord_bot.run(settings.TOKEN)