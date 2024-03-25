import discord
from discord.ext import commands
import openai

# Configurez votre clé API OpenAI ici
openai.api_key = '...'

# Définissez les intents
intents = discord.Intents.default()
intents.messages = True  # Autoriser le bot à recevoir des messages
intents.message_content = True  # Nécessaire pour accéder au contenu des messages

# Initialisez le bot avec les intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')

@bot.command()
async def gpt(ctx, *, prompt: str):
    try:
        # Préparer les messages pour la conversation
        messages = [
            {"role": "system", "content": "Vous discutez avec un assistant AI très utile."},
            {"role": "user", "content": prompt}
        ]

        # Envoie le prompt à l'API OpenAI et récupère la réponse
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Assurez-vous d'utiliser un modèle de chat valide
            messages=messages
        )
        
        # Envoie la réponse générée dans le canal Discord
        last_response = response.choices[0].message['content'] if response.choices else 'Désolé, je ne peux pas répondre à cela.'
        await ctx.send(last_response)
    except Exception as e:
        await ctx.send(f"Une erreur est survenue lors de la génération de la réponse : {e}")

# Remplacez '...' par le token de votre bot Discord
bot.run('...')
