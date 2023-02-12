import hikari
import lightbulb

import firebase_admin
from firebase_admin import db

import settings
import OnJoinBot

discord_bot = lightbulb.BotApp(prefix='!', token=settings.TOKEN, intents=hikari.Intents.GUILD_MEMBERS)


@discord_bot.listen(hikari.ShardReadyEvent)
async def ready_listener(event: hikari.ShardReadyEvent):
    print("The bot is ready!")
    cred = firebase_admin.credentials.Certificate("firebase.json")
    app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://godlydiscordbot-7f469-default-rtdb.europe-west1.firebasedatabase.app/'
    })
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
@lightbulb.option("count", "the counter u wanna add to", type=str)
@lightbulb.option("member", "member to change name of", type=hikari.User)
@lightbulb.command('count', 'Adds to a count')
@lightbulb.implements(lightbulb.SlashCommand)
async def add_count(ctx: lightbulb.SlashContext):
    ref = db.reference('/Counter/' + ctx.options.count)

    if ref.get() == None:
        await ctx.respond("Use one already exisitng")
        return

    value = ref.child(str(ctx.options.member.id)).get()

    if value == None:
        value = 0

    ref.update({
        ctx.options.member.id: int(value) + 1
    })

    await ctx.respond(f"A counter for {ctx.options.count} has been added. Current {ctx.options.count} is {int(value) + 1} for <@{ctx.options.member.id}>")

'''@discord_bot.command
@lightbulb.option("count", "the counter u want a leaderboard for", type=str)
@lightbulb.command('leaderboard', 'Adds to a count')
@lightbulb.implements(lightbulb.SlashCommand)
async def leaderboard(ctx: lightbulb.SlashContext):
    ref = db.reference('/Counter/' + ctx.options.count)

    values = ref.get()

    if values == None:
        await ctx.respond("Use one already exisitng")
        return

    json_string = str(values)

    a = json.dumps("{'name':1, ex: []}")

    print(a)
    b = json.loads(a)

    print(b)
    print(type(b))

    #j = sorted(j.items(), key=lambda item: item[1])

    #print(j)

    await ctx.respond("nothing")
'''


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
    if not ctx.guild_id:
        await ctx.respond("Can only be invoked on a guild.")
        return

    await ctx.app.rest.edit_member(ctx.guild_id, ctx.options.member.id, nickname=ctx.options.name)
    await ctx.respond("Name has been changed to: " + ctx.options.name)
    print("Changed name.")


@discord_bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(f"Something went wrong during invocation of command `{event.context.command.name}`.\nThe error message is:\n`{event.exception.__cause__}`")
        raise event.exception

    # Unwrap the exception to get the original cause
    exception = event.exception.__cause__ or event.exception

    if isinstance(exception, lightbulb.NotOwner):
        await event.context.respond("You are not the owner of this bot.")
    elif isinstance(exception, lightbulb.CommandIsOnCooldown):
        await event.context.respond(f"This command is on cooldown. Retry in `{exception.retry_after:.2f}` seconds.")
    else:
        raise exception

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
