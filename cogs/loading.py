import discord
from discord.ext import commands
from cogs.BaseCog import BaseCog


class Loading(BaseCog):

    @commands.command()
    async def load(self, ctx, extension):
        await self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded {extension} done.")

    @commands.command()
    async def unload(self, ctx, extension):
        await self.bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"UnLoaded {extension} done.")

    @commands.command()
    async def reload(self, ctx, extension):
        await self.bot.reload_extension(f"cogs.{extension}")
        await ctx.send(f"ReLoaded {extension} done.")

async def setup(bot):
    await bot.add_cog(Loading(bot))