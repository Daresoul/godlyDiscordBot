import hikari
import lightbulb

import settings
import OnJoinBot

discord_bot = lightbulb.BotApp(prefix='!', token=settings.TOKEN, intents=hikari.Intents.GUILD_MEMBERS)


@discord_bot.listen(hikari.ShardReadyEvent)
async def ready_listener(_):
    print("The bot is ready!")


@discord_bot.listen(hikari.events.member_events.MemberCreateEvent)
async def member_created(event: hikari.MemberCreateEvent):
    print("person joined")
    text = OnJoinBot.CreateSentences(event.member.username, "🍅", "⬛")
    i = 0
    for i in range(0, len(text)):
        content = text[i][0] + "\n" + text[i][1] + "\n" + text[i][2] + "\n" + text[i][3] + "\n" + text[i][4] + "\n" + \
                  text[i][5] + "\n" + text[i][6]
        await event.app.rest.create_message(811074963464912896, content)


@discord_bot.command
@lightbulb.option("text", "text displayed in emojis", type=str)
@lightbulb.option("fill_emoji", "the fill emoji", type=hikari.Emoji)
@lightbulb.option("text_emoji", "the text emoji", type=hikari.Emoji)
@lightbulb.command('write', 'write something with emojis')
@lightbulb.implements(lightbulb.SlashCommand)
async def write(ctx: lightbulb.SlashContext):
    text = OnJoinBot.CreateSentences(ctx.options.text.lower(), ctx.options.text_emoji, ctx.options.fill_emoji)
    i = 0
    for i in range(0, len(text)):
        content = text[i][0] + "\n" + text[i][1] + "\n" + text[i][2] + "\n" + text[i][3] + "\n" + text[i][4] + "\n" + \
                  text[i][5] + "\n" + text[i][6]
        await ctx.app.rest.create_message(ctx.channel_id, content)
    await ctx.respond("Made the text!")


@discord_bot.command
@lightbulb.command('ping', 'pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.SlashContext):
    await ctx.respond("pong")


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
