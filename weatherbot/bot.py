import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import string
import re
from dotenv import load_dotenv
import os


load_dotenv()
client = commands.Bot(command_prefix = 'w-')

# turns the discord bot on
@client.event
async def on_ready():
    print('Bot has entered the text-chat room')

# discord command for displaying weather forecast
@client.command()
async def forecast(ctx, location):
    weburl = 'http://wttr.in/'
    url = weburl + location
    soup = BeautifulSoup(requests.get(f'http://www.wttr.in/{location}').content, "html.parser")
    soup = soup.get_text().split('┌')[0]
    t = re.sub('\[.*?m', '', soup)
    print(t)
    await ctx.send('```' + t + '```')

#put discord bot token
client.run(os.getenv('DISCORD_TOKEN'))

