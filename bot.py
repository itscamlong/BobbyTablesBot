import os
from discord.ext import commands
from discord import Game, Status
from logic import find

token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command()
async def xkcd(ctx, keyword="latest"):
    try:
        await ctx.trigger_typing()
        result = find(keyword)
        await ctx.send(result)
    except TypeError:
        await ctx.send("Couldn't find anything. Try again!")


@bot.event
async def on_ready():
    await bot.change_presence(status=Status.online, activity=Game(name="Quarantine"))

    print(f'{bot.user.name} has connected to Discord!')
    print(f'{bot.user.name} is connected to the following guild(s): \n')

    for guild in bot.guilds:
        print(f'{guild.name} (id: {guild.id})')

bot.run(token)
