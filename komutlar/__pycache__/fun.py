from discord.ext import commands
import discord

class Eğlence:
    
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def kimlik(self,ctx, member:discord.Member):

        await ctx.send("Kullanıcı adı : {0.mention}".format(member))
    
def setup(bot):
    bot.add_cog(Eğlence(bot))