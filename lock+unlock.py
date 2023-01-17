# تعريفات py-cord
import discord
from discord.ext import commands
# datetime هو تعريف خاص في time stamp
import datetime

bot = commands.Bot(command_prefix="")

# امر قفل الروم او التشانل او القناة
@bot.slash_command(name = "lock", description = "To Lock Channels!")
async def test(ctx):
    await ctx.set_permissions(ctx.guild.default_roles, send_messages=False)
    # em = متغير
    em = discord.Embed(title="Channel has been Locked", timestamp=datetime.datetime.now())
    em.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.display_avatar}")
    em.set_footer(text=f"by/{ctx.author.id}")
    await ctx.respond(embed=em)


# امر الغاء قفل الروم او التشانل او القناة

@bot.slash_command(name = "unlock", description="To Unlock Channels!")
async def test(ctx):
    await ctx.set_permissions(ctx.guild.default_roles, send_messages=True)
    em = discord.Embed(title="Channel has been Unlocked", timestamp=datetime.datetime.now())
    em.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.display_avatar}")
    em.set_footer(text=f"by/{ctx.author.id}")
    await ctx.respond(embed=em)

# لو حبيت تسوي log للامر
# channel = bot.get_channel(ايدي الروم المطلوب)

bot.run("توكن البوت")