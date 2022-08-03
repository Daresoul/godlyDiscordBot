from tokenize import String
import discord
from discord.ext import commands

TOKEN = "MTAwMjU3ODMzMjg5NTk1NzA1Mg.GaBcf4.D_bY29oRD8KWfMwsdOjNh_vr8TeWiDyrmAOxss"

discord_bot = commands.Bot(command_prefix='ohPleaseAdmin ')

@discord_bot.command(name='nick')
async def change_name(ctx, member : discord.Member, arg):
    await member.edit(nick=arg)
    await ctx.send("Name has been changed to: " + arg)

discord_bot.run(TOKEN)