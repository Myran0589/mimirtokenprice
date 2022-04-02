import discord
from datetime import datetime
from discord.ext import commands
import aiohttp
from aiohttp import request

bot=commands.Bot(command_prefix='-')
bot.remove_command("help")

@bot.event
async def on_ready():
    print(f"{bot.user.name}")

@bot.command()
async def price(ctx, mimir:float = None):
        url = "https://api.coingecko.com/api/v3/coins/mimir-token"
        async with aiohttp.ClientSession() as session:
            async with session.get(url = url) as response:
                if response.status != 200:
                    return await ctx.send("Error while fetching data from mimir token url")
                if not mimir: mimir = 1.0
                data = await response.json()
                price = data.get("market_data").get("current_price").get("usd")
                usd = float("{:.2f}".format(price*mimir))
                price = data.get("market_data").get("current_price").get("inr")
                inr = float("{:.2f}".format(price*mimir))
                embed = discord.Embed(color=0x808080)
                embed.set_author(name="Mimir Token (MIMIR)", icon_url="https://images-ext-1.discordapp.net/external/nqcXP9AhDgn1FqN3TJdFQxTqylMXGOLuqV6wk99GKvw/%3F1635401626/https/assets.coingecko.com/coins/images/19551/large/xaq5Xlzg_400x400.jpg")
                embed.set_thumbnail(url=ctx.guild.icon_url)
                embed.add_field(name="Calculation Process", value=f"ᛗ {mimir}", inline=False)
                embed.add_field(name="Realtime India :-", value=f"₹ {inr}", inline=False)
                embed.add_field(name="Realtime Usa :-", value=f"$ {usd}", inline=False)
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed = embed)

bot.run('Bot token here')
