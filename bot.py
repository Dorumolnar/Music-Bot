import discord
import os
from discord.ext import commands
from discord.voice_client import VoiceClient


startup_extensions = ["Music", "General", "Fun"]
bot = commands.Bot("?")

@bot.event
async def on_ready():
    print("Bot is on")

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("Hi :wave:")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load extension {}\n{}".format(extension, exc))


bot.run("your bot token")
