import discord
import asyncio
import os
import json
import discord
from discord.ext import commands
from myserver import server_on

intents = discord.Intents.default()
intents.messages = True  # เปิดใช้งานการจับข้อความ

class xesonz_bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix='/', intents=intents, *args, **kwargs)

bot = xesonz_bot(owner_id=784027820367020042, case_insensitive=True)

@bot.event
async def on_ready():
    print(f'{bot.user} is ready')
    print('\nCogs Loaded\n----------\n')

if __name__ == "__main__":
    for file in os.listdir('./cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            bot.load_extension(f'cogs.{file[:-3]}')

server_on()

bot.run(os.getenv('TOKEN'))