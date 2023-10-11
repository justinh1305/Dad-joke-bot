import discord
from discord.ext import commands
from dadjokes import Dadjoke
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
client = commands.Bot(command_prefix='$', intents = discord.Intents.all())

@client.event
async def on_ready():
    print("Dadbot is ready!")
    print("----------------")

@client.command()
async def joke(ctx):
    dadjoke = Dadjoke()
    await ctx.send(dadjoke.joke)

client.run(token)