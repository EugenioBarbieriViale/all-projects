#!/usr/bin/python3

import discord
import random
from discord.ext import commands
import dict_latin
import encourage_list
import hello_all_languages

bot = commands.Bot(command_prefix="£")
TOKEN = discord_token!

possible_encourage = encourage_list.list
possible_hellos = hello_all_languages.list
paradigms = dict_latin.dict

# get help
@bot.command(name="h")
async def get_help(ctx):
    await ctx.channel.send("```£hello: greetings in all the languages!\n£support: encouraging messages\n£guess £number>: guess a number from 0 to 20\n£par <verb>: returns the (latin) paradigm\n£join/leave: bot joins the voice channel```")

# greeting in all the languages
@bot.command()
async def hello(ctx):
    greeting = random.choice(possible_hellos)
    await ctx.channel.send(greeting)

# encouraging messages
@bot.command()
async def support(ctx):
    encourage = random.choice(possible_encourage)
    await ctx.channel.send(encourage)

# guess the number game
@bot.command()
async def guess(ctx, user_number:int):
    number = random.randrange(20)
    if user_number == number:
        await ctx.channel.send("Right!")
    else:
        await ctx.channel.send("Wrong!\nThe number was "+str(number))

# paradigms in latin
@bot.command(name="par")
async def paradigm(ctx, verb):
    try:
        await ctx.channel.send(paradigms[verb])
    except KeyError:
        await ctx.channel.send(f"Error: {verb} not found")

# voice channels
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run(TOKEN)
