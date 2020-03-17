import os
from discord.ext import commands
from search import search
from latest import latest

token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command()
async def xkcd(ctx, keyword="latest"):
    try:
        if keyword.isnumeric():
            url = "https://xkcd.com/" + keyword
        elif keyword == "latest":
            url = latest()
        else:
            await ctx.send("Let me take a guess...")
            url = "https://" + search(keyword)
        await ctx.send(url)
    except TypeError:
        await ctx.send("Couldn't find anything. Try again!")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print(f'{bot.user.name} is connected to the following guild(s): \n')

    for guild in bot.guilds:
        print(f'{guild.name} (id: {guild.id})')

bot.run(token)
