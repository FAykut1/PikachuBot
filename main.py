import discord
from discord.ext import commands
import config
import os 

token=config.token


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix='+', pm_help=None, description="Discord Bot")
        self.add_command(self.ping)
        self.mypath=os.listdir("./komutlar")
        self.myfile=[]
        for dosya in self.mypath:
            if '.py' in dosya:
                lenght = len(dosya)
                fls = dosya[:lenght -3]
                self.myfile.append(fls)

        for x in self.myfile:
            try:
                self.load_extension("komutlar"+x)
            except:
                print("Hatalı dosya:"+x)
    
    async def on_ready(self):
        print("Babam Lovecraftian")
        print(self.user.name)
        print(self.user.id)

    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content == "sa":
            await message.channel.send("as")

        await self.process_commands(message) ##

    async def on_command_error(self,ctx,error):
        channel=ctx.channel
        if isinstance(error, commands.MissingRequiredArgument):
            await channel.send("```'{0.prefix}help {0.command.name}' yazarak doğru komudu öğrenebilirsiniz.```".format(ctx))
        if isinstance(error, commands.CommandNotFound):
            await channel.send("```Komut bulunamadı.'{0.prefix}help' yazarak geçerli komutları öğrenebilirsiniz.")



    @commands.command()
    async def ping(self,ctx):
        await ctx.send("Pong <3")
    

bot = Bot()
bot.run(token)

