from discord.ext import commands
import discord


class Yönetim:
    def __init__(self, bot):
        self.bot =bot
    
    @commands.command(hidden=True)
    async def kapat(self,ctx):
        if ctx.author.id == 367046851276308490:
            await self.bot.close()
        else:
            await ctx.send("Bu komudu kullanma yetkiniz yok.")

    @commands.command(hidden=True)
    async def yenile(self,ctx,value:str):

        source = "komutlar."
        try:
            self.bot.unload_extension(source+value)
            self.bot.load_extension(source+value)
        except ImportError as e:
            print(e)


def setup(bot):
    bot.add_cog(Yönetim(bot))