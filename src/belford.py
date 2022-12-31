import json
import discord
import os
import random
import subprocess
import yfinance as yahooFinance

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.command(name='fb', help='Tells you errythang you need to know about Facebook.')
async def fb(ctx):
    GetFacebookInformation = yahooFinance.Ticker("META")
    fb_data = GetFacebookInformation.history(period="6mo")
    response = fb_data
    await ctx.send(response)

bot.run(TOKEN)
