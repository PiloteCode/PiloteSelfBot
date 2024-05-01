import discord
from discord.ext import commands
import asyncio
import os
import json
import random
import tasks
import datetime

bot = commands.Bot(command_prefix='pilote.', self_bot=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(status=discord.Status.dnd)
    while True:
        server_id = 1103936072989278279
        server = bot.get_guild(server_id)
        if server is not None:
            member_count = server.member_count
            bot_user = await bot.fetch_user(bot.user.id)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{member_count} membres'))
            await asyncio.sleep(60)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'.gg/PILOTE'))
            await asyncio.sleep(60)
    
from discord.ext import tasks

loops = {}

@bot.command()
async def sendloop(ctx, time_loop: int, *, message: str):
    if ctx.author.id == 97285029289275392:
        if ctx.channel.id not in loops:
            loops[ctx.channel.id] = send_message_loop(time_loop)
            loops[ctx.channel.id].start(ctx, message)
            await ctx.send(f"Ok.")
        else:
            await ctx.send("Non.")
    else:
        return

def send_message_loop(time_loop):
    @tasks.loop(seconds=time_loop)
    async def inner(ctx, message):
        await ctx.send(message)
    return inner

@bot.command()
async def stoploop(ctx):
    if ctx.author.id == 97285029289275392:
        if ctx.channel.id in loops and loops[ctx.channel.id].is_running():
            loops[ctx.channel.id].cancel()
            del loops[ctx.channel.id]
            await ctx.send("Ok.")
        else:
            await ctx.send("Non jsp.")
    else:
        return
        
#####################################################################################################################
#                                                                                                                   #
#                                                                                                                   #
#                                                  TOKEN DU BOT                                                     #
#                                               PAR PILOTE PRODUCTION                                               #
#                                                                                                                   #
#####################################################################################################################

bot.run("YOUR TOKEN HERE", bot=False)

