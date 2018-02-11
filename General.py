import asyncio
import discord
from random import randint
from random import choice
from enum import Enum
from discord.ext import commands
import datetime
import time
import aiohttp

settings = {"POLL_DURATION" : 60}

class RPS(Enum):
    rock     = "\N{MOYAI}"
    paper    = "\N{PAGE FACING UP}"
    scissors = "\N{BLACK SCISSORS}"

class RPSParser:
    def __init__(self, argument):
        argument = argument.lower()
        if argument == "rock":
            self.choice = RPS.rock
        elif argument == "paper":
            self.choice = RPS.paper
        elif argument == "scissors":
            self.choice = RPS.scissors
        else:
            raise

class General:
    """General commands"""
    def __init__(self, bot):
        self.bot = bot
        self.stopwatchest = {}

    @commands.command(hidden=True)
    async def ping(self):
        """Pong."""
        await self.bot.say("Pong.")

    @commands.command(hidden=True)
    async def choose(self, *choices):
        """Chooses between multiple choices."""
        choices = [escape_mass_mentions(c) for c in choices]
        if len(choices)  < 2:
            await self.bot.say('Not enough choices to pick from.')
        else:
            await self.bot.say(choice(choices))

    @commands.command(pass_context=True)
    async def roll(self, ctx, number : int = 100):
        """Rolls random number (between 1 and user choice)"""
        author = ctx.message.author
        if number > 1:
            n = randint(1, number)
            await self.bot.say("Your rolled number is:")
            await asyncio.sleep(0.6)
            await self.bot.say("{}".format(n))
        else:
            await self.bot.say("{} Maybe higher than 1? ;P".format(author.mention))

    @commands.command(pass_context=True)
    async def rps(self, ctx, your_choice : RPSParser):
        """Play rock paper scissors with the bot"""
        author = ctx.message.author
        player_choice = your_choice.choice
        music_choice = choice((RPS.rock, RPS.paper, RPS.scissors))
        cond = {
                (RPS.rock,     RPS.paper)    : False,
                (RPS.rock,     RPS.scissors) : True,
                (RPS.paper,    RPS.rock)     : True,
                (RPS.paper,    RPS.scissors) : False,
                (RPS.scissors, RPS.rock)     : False,
                (RPS.scissors, RPS.paper)    : True
               }

        if music_choice  == player_choice:
            outcome = None
        else:
            outcome = cont[(player_choice, music_choice)]

        if outcome is True:
            await self.bot.say("{} You win {}"
                               "".format(music_choice.value, author.mention))

        elif outcome is False:
            await self.bot.say("{} You lose {}"
                               "".format(music_choice.value, author.mention))

        else:
            await self.bot.say("{} We're square {}"
                               "".format(music_choice.value, author.mention))

    @commands.command(pass_context=True, no_pm=False)
    async def info(self, ctx):
        """Says the info about bot."""
        await self.bot.say('```The bot was created in Python \n'
                           '-------- \n'
                           'The bot was created by Diru#1601 \n'
                           'Support Channel: https://discord.gg/tdDytsE```')

    @commands.command(pass_context=True, no_pm=True)
    async def serverinfo(self, ctx):
        """Shows server's informations"""
        server = ctx.message.server
        online = len([m.status for m in server.members
                      if m.status == discord.Status.online or
                      m.status == discord.Status.idle])
        total_users = len(server.members)
        text_channels = len([x for x in server.channels
                             if x.type == discord.ChannelType.text])
        voice_channels = len([x for x in server.channels
                             if x.type == discord.ChannelType.voice])
        passed = (ctx.message.timestamp - server.created_at).days
        created_at = ("Since {}. That's over {} days ago!"
                      "".format(server.created_at.strftime("%d %b %Y %H:%M"),
                                passed))

        colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
        colour = int(colour, 16)

        data = discord.Embed(
            description=created_at,
            colour=discord.Colour(value=colour))
        data.add_field(name="Region", value=str(server.region))
        data.add_field(name="Users", value="{}/{}".format(online, total_users))
        data.add_field(name="Text Channels", value=text_channels)
        data.add_field(name="Voice Channels", value=voice_channels)
        data.add_field(name="Roles", value=len(server.roles))
        data.add_field(name="Owner", value=str(server.owner))
        data.set_footer(text="Server ID: " + server.id)

        if server.icon_url:
            data.set_author(name=server.name, url=server.icon_url)
            data.set_thumbnail(url=server.icon_url)
        else:
            data.set_author(name=server.name)

        try:
            await self.bot.say(embed=data)
        except discord.HTTPException:
            await self.bot.say("I need the `Embed links` permission "
                               "to send this")

def setup(bot):
    bot.add_cog(General(bot))
    print('General is loaded')
