import discord
import SimpleEconomy as Seco
import asyncio
import json
from discord.ext import commands

Seco.Database_dir = ".main.db"
Seco.default_balance = 999
bot = commands.Bot(command_prefix='+', case_insensitive=True, description="Mumoso Discord Bot")

@bot.event
async def on_ready():
    print("Database Ready!")
    bot.load_extension('cogs.eco')
    bot.load_extension('cogs.staff')
    bot.load_extension('cogs.public')
    bot.load_extension('cogs.store')
    bot.load_extension('cogs.youtube')
    print("Everything Loaded!")
    print("Ready!")
    await bot.change_presence(activity=discord.Streaming(name= "This Code", url= "https://www.twitch.tv/mumoso"))

@bot.command()
async def reloadforeva(ctx):
    await ctx.send("sent it lil pig")
    while True:
        await asyncio.sleep(60)
        bot.unload_extension('cogs.public')
        bot.load_extension('cogs.public')

bot.run("NzMxNTk1NzY5NTU5Mzg0MDc0.XwoVpw.S0xrJgPCn0sXMfsokRsfI4OCGKA")