from tokenize import String
import discord
import math
from discord.ext import commands

import settings
import OnJoinBot

discord_bot = commands.Bot(command_prefix='ohPleaseAdmin ')

@discord_bot.command(name='write')
async def write(ctx, arg):
    text = OnJoinBot.CreateSentences(arg, "❤", "🎶")
    i = 0
    iterations = math.ceil(len(text[0]) / modifier)
    for i in range(0, iterations):
        await ctx.send(text[0][i*modifier : (i + 1) * modifier] + "\n" + text[1][i*modifier : (i + 1) * modifier] + "\n" + text[2][i*modifier : (i + 1) * modifier] + "\n" + text[3][i*modifier : (i + 1) * modifier] + "\n" + text[4][i*modifier : (i + 1) * modifier] + "\n" + text[5][i*modifier : (i + 1) * modifier] + "\n" + text[6][i*modifier : (i + 1) * modifier])
    #25
    
@discord_bot.command(name='ping')
async def ping(ctx):
    await ctx.send("PONG")

@discord_bot.command(name='nick')
async def change_name(ctx, member : discord.Member, arg):
    await member.edit(nick=arg)
    await ctx.send("Name has been changed to: " + arg)

@change_name.error
async def change_name_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send('Luls, can\'t change the members nickname...')
    if isinstance(error, commands.MemberNotFound):
        await ctx.send('Cannot find the Member you are speaking of...')
    if isinstance(error, commands.TooManyArguments):
        await ctx.send('Ummm, have u looked in the help command?')

discord_bot.run(settings.TOKEN)