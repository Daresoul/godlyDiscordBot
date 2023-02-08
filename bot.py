from tokenize import String
import discord
import math
from discord.ext import commands
import hikari
import lightbulb

import settings
import OnJoinBot

discord_bot = lightbulb.BotApp(token=settings.TOKEN) #commands.Bot(command_prefix='ohPleaseAdmin ')


@discord_bot.command
@lightbulb.command('write', 'write something with emojis')
async def write(ctx, arg):
    text = OnJoinBot.CreateSentences(arg.lower(), "❤", "🎶")
    i = 0
    for i in range(0, len(text)):
        await ctx.send(text[i][0] + "\n" + text[i][1] + "\n" + text[i][2] + "\n" + text[i][3] + "\n" + text[i][4] + "\n" + text[i][5] + "\n" + text[i][6])
    
@discord_bot.command
@lightbulb.command('ping', 'pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("pong")


'''
@discord_bot.command
@lightbulb.command('group', 'this is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass
'''

@discord_bot.command
@lightbulb.option("member", "member to change name of", type=hikari.User)
@lightbulb.option("name", "new name of user")
@lightbulb.command('nick', 'give new nickname')
@lightbulb.implements(lightbulb.SlashCommand)
async def nick(ctx: lightbulb.SlashContext):
    await ctx.app.rest.edit_member(ctx.get_guild(), ctx.options.member.id, nickname=ctx.options.name)
    await ctx.respond("Name has been changed to: " + ctx.options.name)
    print("Changed name.")

'''@change_name.error
async def change_name_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...')
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send('Luls, can\'t change the members nickname...')
    if isinstance(error, commands.MemberNotFound):
        await ctx.send('Cannot find the Member you are speaking of...')
    if isinstance(error, commands.TooManyArguments):
        await ctx.send('Ummm, have u looked in the help command?')
'''


discord_bot.run()