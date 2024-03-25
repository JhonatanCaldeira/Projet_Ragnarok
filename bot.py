from dotenv import load_dotenv
import os
from brave_api_2 import brave_request
import json 
import gpt

import discord
from discord.ext import commands
import openai
import requests
from gpt import openai_request

# Définissez les intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Initialisez le bot avec le nouveau préfixe '/'
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():   
    print(f'Connecté en tant que {bot.user}')

@bot.command(name='bot')
async def qwery_command(ctx, *, query: str):
    try:
        braveResult = brave_request(query)
        last_response = openai_request(query, braveResult)

        await ctx.send(last_response)
    except Exception as e:
        await ctx.send(f"Une erreur est survenue : {e}")

bot.run(os.environ.get("discord_key"))
