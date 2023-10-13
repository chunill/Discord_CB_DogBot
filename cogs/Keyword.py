import discord
from discord.ext import commands
from cogs.BaseCog import BaseCog

class KeywordResponse(BaseCog):
    def __init__(self, bot :commands.bot):
        super().__init__(bot)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if  '狗勾' in message.content:
            await message.channel.send('汪！')

async def setup(bot: commands.Bot):
    await bot.add_cog(KeywordResponse(bot))