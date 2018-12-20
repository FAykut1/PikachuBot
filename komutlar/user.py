from discord.ext import commands
import discord
from veriler import veriler


class Kullanıcı:
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def kullanıcı(self, ctx, member:discord.Member):
        myembed = discord.Embed(title=member.name, color=0xff0000)
        myembed.add_field(name="Durum", value=member.status)
        myembed.add_field(name="Rol", value = member.top_role)
        myembed.add_field(name="ID", value=member.id)
        myembed.add_field(name="Level/Exp", value=str(veriler.level_getir(member)) + "/" + str(veriler.xp_getir(member)))
        myembed.add_field(name="Oluşturulma tarihi",value=member.created_at)
        myembed.add_field(name="Katılım tarihi", value=member.joined_at)
        myembed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=myembed)


    async def on_message(self,msg):
        if msg.author.bot:
            return
        if not msg.guild:
            return

        veriler.xp_ekle(msg.author, 2)
def setup(bot):
    bot.add_cog(Kullanıcı(bot))
