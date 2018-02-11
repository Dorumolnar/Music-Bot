import asyncio
import discord
from discord.ext import commands
import random
from random import randint
from random import choice

class Fun:

    def __init__(self, bot):
        self.bot = bot
        self.ball = ["As I see it, yes", "It is certain", "It is decidedly so", "Most likely", "Outlook good",
                     "Signs point to yes", "Without a doubt", "Yes", "Yes – definitely", "You may rely on it", "Reply hazy, try again",
                     "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                     "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

    @commands.command(name="8", aliases=["8ball"])
    async def _8ball(self, *, question : str):
        """Asks 8 ball a question

        Question must end with a question mark.
        """
        if question.endswith("?") and question != "?":
            await self.bot.say("`" + choice(self.ball) + "`")
        else:
            await self.bot.say("That dosen't looks like a question")

    @commands.command(pass_context=True)
    async def flip(self, ctx, user : discord.Member=None):
        """Flips a coin..."""
        if user != None:
            msg = ""
            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = "Nice try. You think this is funny? How about *this* instead:\n\n"
            char = "abcdefghijklmnopqrstuvwxyz"
            tran = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz"
            table = str.maketrans(char, tran)
            name = user.display_name.translate(table)
            char = char.upper()
            tran = "∀qƆpƎℲפHIſʞ˥WNOԀQᴚS┴∩ΛMX⅄Z"
            table = str.maketrans(char, tran)
            name = name.translate(table)
            await self.bot.say(msg + "(╯°□°）╯︵ " + name[::-1])
        else:
            await self.bot.say("*flips a coin and... " + choice(["HEADS!*", "TAILS!*"]))

    @commands.command(pass_context=True)
    async def ship(self):
        await self.bot.say(random.choice(["100% **OMG VERY GOOD**",
                                          "90% **VERY GOOD**",
                                          "80% **VERY GOOD**",
                                          "70% **GOOD**",
                                          "60% **GOOD**",
                                          "50% **GOOD**",
                                          "40% **BAD**",
                                          "30% **BAD**",
                                          "20% **VERY BAD**",
                                          "10% **VERY BAD**",
                                          "0% **WOW O_O**"]))

    @commands.command(pass_context=True)
    async def rolldice(self, ctx):
        """Roll the dice"""
        await self.bot.say("You rolled a {}!".format(random.randint(1, 6)))

    @commands.command(pass_context=True)
    async def uppercase(self, ctx, *, msg:str):
        """Uppercase the message"""
        await self.bot.say(msg.upper())

    @commands.command(pass_context=True)
    async def lowercase(self, ctx, *, msg:str):
        """Lowercase the message"""
        await self.bot.say(msg.lower())

def setup(bot):
    bot.add_cog(Fun(bot))
    print('Fun loaded!')
