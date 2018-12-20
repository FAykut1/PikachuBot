from discord.ext import commands
import discord


class Kullanıcı:
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def kullanıcı(self, ctx, member:discord.Member):
        myembed = discord.Embed(title=member.name)
        myembed.add_field(name="Durum", value=member.status)
        myembed.add_field(name="Kullandığı nick", value=member.nick)
        myembed.add_field(name="Rol", value = member.top_role)
        myembed.add_field(name="ID", value=member.id)
        myembed.add_field(name="Level / Tecrübe", value=None)
        myembed.add_field(name="Discord'a katıldığı tarih",value=member.created_at)
        myembed.add_field(name="Sunucuya katıldığı tarih", value=member.joined_at)
        myembed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=myembed)


    async def on_message(self,msg):
        pass

def setup(bot):
    bot.add_cog(Kullanıcı(bot))
