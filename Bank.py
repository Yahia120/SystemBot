# تعريفات py-cord:

import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="")
# امر البنك يبدا من هنا

@bot.slash_command(name = "your_bank", description = "To see Your Credits or Money !")
async def whew(ctx):
    await op(ctx.author)
    members = await gtbd()
    member = ctx.author
    

    amt = members[str(member.id)]["عندك"]
    amt2 = members[str(member.id)]["المبلغ اللي جمعته"]
    em = discord.Embed(title="البنك :")
    em.set_author(name= f"{member}")
    em.add_field(name="المبلغ اللي عندك", value=amt)
    em.add_field(name = "المبلغ اللي قد جمعته", value=amt2)
    await ctx.respond(embed=em)

# امر اعطاء مبلغ يومي
@bot.slash_command(name = "daily", description="Bot will give you from 0 to 50 !")
@commands.cooldown(1, 60)
async def whew(ctx):
    await op(ctx.author)
    members = await gtbd()
    deal = random.randrange(50)
    member = ctx.author
    
    members[str(member.id)]["عندك"] += deal
    with open(".json", "w") as f:
        json.dump(members, f)
    await ctx.respond(f"You have now {deal}")
# هنا في open() يجب ان تنشأ ملف يحمل صيغة جيسون json

@bot.slash_command(name = "give_from_bank", description="Give members Money")
async def whew(ctx , member : discord.Member, المبلغ = None):
    
    await op(ctx.author)
    await op(member)
    
    cre = await ub(ctx.author)
    المبلغ = int(المبلغ)

    await ub(ctx.author,-1*المبلغ,"عندك")
    await ub(member,المبلغ,"عندك")
    await ctx.respond(f"تم اعطاء {member.mention} {المبلغ}")


@bot.slash_command(name = "bank_member", description="to see members bank")
async def whew(ctx, user : discord.Member):
    await op(user)
    members = await gtbd()
    

    amt = members[str(user.id)]["عندك"]
    amt2 = members[str(user.id)]["المبلغ اللي جمعته"]
    em = discord.Embed(title="البنك :")
    em.set_author(name= f"{user.name}")
    em.add_field(name="المبلغ اللي عندك", value=amt)
    em.add_field(name = "المبلغ اللي قد جمعته", value=amt2)
    await ctx.respond(embed=em)
    
    


# فنكشن تقوم بفتح قائمة جديدة
async def op(member):
    members = await gtbd()

    if str(member.id) in members:
        return Fa1lse
    else:
        members[str(member.id)] = {}
        members[str(member.id)]["عندك"] = 0
        members[str(member.id)]["المبلغ اللي جمعته"] = 0

    
    with open("", "w") as f:
        json.dump(members, f)
    return True
# .jsonقم بانشاء ملف في فيجوال ستوديو كود وتاكد في اخر الملف 
# ثم قم بوضعه في with open("مسار الملف")
async def gtbd():
    with open("", "r") as f:
        members = json.load(f)

    return members

# قم بوضعه في with open("مسار الملف")

async def ub(member, change = 0, mode = "عندك"):
    members = await gtbd()
    members[str(member.id)][mode] += change
    with open(".json", "w") as f:
        json.dump(members, f)
    cre = [members[str(member.id)]["عندك"],members[str(member.id)]["المبلغ اللي جمعته"]]
    return member


bot.run("توكن البوت")