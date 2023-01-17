# تعريفات py-cord
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="")

# امر اعطاء رتب للاعضاء
@bot.slash_command(name = "add_role", description = "add role for members by this command!")
async def whew(ctx, role:discord.Role, member:discord.Member, reason):
    
    await member.add_roles(role)
    em = discord.Embed(title="Has Given a Role", color=discord.Color.green())
    em.add_field(name="``member to give``", value=f"{member}")
    em.add_field(name="``by``", value=f"{ctx.author.mention}")
    em.add_field(name = "reason : ", value=f"{reason}")
    pfp = member.display_avatar
    name = member.display_name
    
    em.set_author(name=f"{name}", icon_url=f"{pfp}")
    await ctx.respond(embed=em)

bot.run("توكن البوت")