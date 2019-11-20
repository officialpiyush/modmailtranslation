import asyncio
from discord.ext import commands
from modmailtranslation import Translator

loop = asyncio.get_event_loop()

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.i18n = Translator("https://raw.githubusercontent.com/officialpiyush/modmailtranslation/master/examples/example.json")

    @commands.command()
    async def say_hi(self, ctx):
        resp = await loop.run_in_executor(None, self.i18n.get, "hi")
        await ctx.send(resp)


def setup(bot):
    bot.add_cog(MyCog(bot))
