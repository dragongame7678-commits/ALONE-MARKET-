import discord, os
from discord.ext import commands

TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online: {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "discord.gg/" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} Promo links are not allowed!")
    await bot.process_commands(message)

bot.run(TOKEN)
