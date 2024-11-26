import discord
from discord.ext import commands
from discord.commands import slash_command, Option, user_command, message_command

class Myview(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Get Script", style=discord.ButtonStyle.green)
    async def button_1(self, button: discord.ui.Button, interation: discord.Interaction):

        await interation.response.send_message('```loadstring(game:HttpGet("https://raw.githubusercontent.com/x2Kalimakx/Xesonz-Free/refs/heads/main/Crackmai"))()```', ephemeral=True)

class basic_bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(self.__class__.__name__)

    @slash_command(guild_ids=[1244170335117377626])
    async def setup_getscript(self, ctx):
        embed = discord.Embed(
            title='Xesonz Hub - Free Script',
            color=0xB983FF,
            description="\n",
        )
        
        channel_id = 1309553968581447762  # ใส่ Channel ID ที่ต้องการ
        channel = ctx.guild.get_channel(channel_id)

        embed.add_field(
            name=">>> Get Script - Xesonz\n1 Script - All Map\n",
            value=f"",
            inline=False,
        )
        
        embed.add_field(
            name="📈 ดูแมพที่มีทั้งหมดได้ที่ห้อง",
            value=f"{channel.mention} | Status Map",
            inline=False,
        )
        
        embed.set_image(url='https://cdn.discordapp.com/attachments/1286940074197389404/1309548879473283253/standard.gif?ex=6741fbef&is=6740aa6f&hm=9bfc3eccbd6b688b791cb8ab9efbca8ae75a2c32dd83b7c706c8253ff5b1af8e&')

        embed.set_footer(text="❤️ Xesonz Hub 🌙")

        view = Myview()
        await ctx.respond(embed=embed, view=view)

def setup(bot):
    bot.add_cog(basic_bot(bot)) 