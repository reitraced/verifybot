import discord
from discord.ext import commands
from discord.utils import get
from asyncio import sleep

f = open('token.txt', 'r')
token = f.read()
f.seek(0)
f.close()

p="v!"
bot = commands.Bot(command_prefix=p)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(game=discord.Game(name='by verifying you'))

@bot.command(pass_context=True)
async def verify(ctx, arg):
    member = ctx.message.author
    role = get(member.server.roles, name="verified")
    correct = "scams"
    fail = "wrong input, read the rules again"
    channel = bot.get_channel("550847713202405398")
    if arg == correct:
        await bot.delete_message(ctx.message)
        await bot.add_roles(member, role)
    else:
        await bot.delete_message(ctx.message)
        await bot.say(fail)
        await sleep(4) 
        await bot.delete_message(fail)

bot.run(token)