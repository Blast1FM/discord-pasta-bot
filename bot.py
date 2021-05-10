#bot

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import ban_check

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
PASTE = os.getenv('PASTE_NAME')

bot = commands.Bot(command_prefix="\\")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="Spam @BlastFM#3955 if something doesn't work"))
    print(f'{bot.user.name} ready')

@bot.command(name="check_bans", help="Checks etf2l bans for a given user")
async def check_etf2l(ctx,*,player_steam):
    checker = ban_check.BanChecker()
    await ctx.send(checker.checkBan(player_steam))
    
@bot.command(name="paste", help="Super secret admin paste tool,you see")
@commands.has_any_role('Administrator')
async def paster(ctx):
    with open(PASTE,"r+") as source:
        for line in source:
            if line.strip() != "":
                await ctx.send(line)
        source.truncate(0)
        print(f"Paste request by {ctx.author} in {ctx.guild} in #{ctx.channel} complete - file cleared")
        await ctx.send("Done")

@paster.error
async def paster_role_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("No pasta for you!")
        print(f"Attempted paste by {ctx.author} in {ctx.guild} in #{ctx.channel} with no required roles")
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("```CommandInvokeError - your paste source file does not exist```")
        print("CommandInvokeError, missing paste source/incorrect name")

bot.run(TOKEN)
