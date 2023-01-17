import discord
from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix="")

# امر ban
@bot.slash_command(name = "ban", description="To Ban Members !")
async def asda(ctx, member : discord.Member):
    await member.ban()
    em = discord.Embed(

        title="member has been banned",
        color=discord.Color.green()
    )
    em.add_field(name="``member``", value=member)
    em.add_field(name = "``by``", value=ctx.author.mention)
    await ctx.respond(embed = em)
# امر kick
@bot.slash_command(name = "kick", description="To Kick Members !")
async def asdas(ctx, member : discord.Member, reason):
    await member.kick()
    await ctx.respond(f"member {member.mention} has been kicked by {ctx.author} reason:\n\n {reason}")

# mute
@bot.slash_command(name = "mute", description = "To mute Member")
async def uwu(ctx, member : discord.Member, reason):
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    em = discord.Embed(title="Member has been muted !", color=discord.Color.green(), timestamp=datetime.datetime.now())
    em.add_field(name= "member :", value=member)
    em.add_field(name="reason :", value=reason)
    em.set_author(name=member.name, icon_url=member.display_avatar)
    await ctx.respond(embed = em)