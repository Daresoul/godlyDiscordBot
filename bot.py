from tokenize import String
import discord
from discord.ext import commands

import settings
import OnJoinBot

discord_bot = commands.Bot(command_prefix='ohPleaseAdmin ')

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