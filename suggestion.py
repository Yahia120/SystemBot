# تعريفات py-cord
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="")

# امر الاقتراحات
@bot.slash_command(name = "suggestion", description="Give a Suggestion for Server !")
async def sugg1(ctx, content, user : discord.Member):
    name = user.display_name
    av = user.display_avatar
    em = discord.Embed(title="has been sent suggestion", color=discord.Color.green())
    em.set_thumbnail(url=av)
    em.set_author(name=name, icon_url=f"{av}")
    em.add_field(name="The Suggestion :", value=f"\n\n||``{content}``||")
    em.set_footer(text=f"user id : {user.id}")
    await ctx.respond(embed=em)
bot.run("التوكن")