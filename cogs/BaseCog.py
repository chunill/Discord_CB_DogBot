from discord.ext import commands

class BaseCog(commands.Cog):
    def __init__(self, bot :commands.bot):
        self.bot = bot

async def setup(bot: commands.Bot):
    await bot.add_cog(BaseCog(bot))