import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="")

class Ticket(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label = "create Ticket!", style = discord.ButtonStyle.blurple)
    async def uwu(self, button : discord.ui.Button, interaction : discord.Interaction):
        
        
        overwrite = {

            
            interaction.guild.default_role : discord.PermissionOverwrite(view_channel=False),
            interaction.user : discord.PermissionOverwrite(view_channel = True , send_messages = True),
            interaction.guild.me : discord.PermissionOverwrite(view_channel=True, send_messages = True)
        }
        ticket = await interaction.guild.create_text_channel(name = f"ticket-for-{interaction.user.name}", overwrites=overwrite)
        await interaction.response.send_message(f"hi {ticket.mention}", ephemeral=True)
        em = discord.Embed(title="الرسالة <@&>" , color=discord.Color.green())
        await ticket.send(embed=em, view=TicketS())
# لو حبيت تمنشن رتبة او رول مع الرسالة 
# <@&ايدي الرتبة>


class TicketS(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label = "close Ticket!", style = discord.ButtonStyle.red)
    async def uwu(self, button : discord.ui.Button, interaction : discord.Interaction):
        await interaction.user.send(f"ticket has been closed by")
        await interaction.channel.delete()

# امر يضيف اعضاء الى التكت
@bot.slash_command(name = "add_members")
async def asda(ctx, member:discord.Member):
    if "ticket-for-"in ctx.channel.name:
        await ctx.channel.set_permissions(member , view_channel = True, send_messages=True)
        await ctx.respond(f"Member {member.mention} has been added to Ticket By {ctx.author}")

# ايفنت لما يشتغل البوت بيرسل زر في قناة او روم معين زر لو ضغطته بيفتح التكت
@bot.event
async def on_ready():
    channel = bot.get_channel(هنا ايدي الروم)
    await channel.send(view=view)
bot.run("توكن البوت")