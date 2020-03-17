import os
from discord.ext import commands

token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command()
async def xkcd(ctx, num):
    try: 
        num = int(num)
        url = "https://xkcd.com/" + str(num)
        await ctx.send(url)
    except ValueError:
        await ctx.send("Strings are not yet supported.")


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    print(f'{bot.user.name} is connected to the following guild(s): \n')

    for guild in bot.guilds:
        print(f'{guild.name} (id: {guild.id})')

bot.run(token)
