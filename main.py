import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="+", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def تحذير(ctx, member: discord.Member, *, reason="بدون سبب"):
    embed = discord.Embed(
        title="⚠️ تحذير إداري",
        color=discord.Color.orange()
    )
    embed.add_field(name="العضو", value=member.mention, inline=False)
    embed.add_field(name="السبب", value=reason, inline=False)
    embed.set_footer(text=f"بواسطة {ctx.author}")

    await ctx.send(embed=embed)

    try:
        await member.send(
            f"⚠️ تم تحذيرك في سيرفر **{ctx.guild.name}**\n"
            f"📄 السبب: {reason}"
        )
    except:
        pass

bot.run(os.getenv("TOKEN"))

