import os
import discord
from secrets import secrets 
from database import *
import random
# from replit import db
# from asmr_vtuber_list import ASMR_VTUBER_LIST
# from anime_api.apis import NekosAPI
# from discord.ext import commands



# Initials
client = discord.Client(intents=discord.Intents.default())
# api = NekosAPI()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    connect_to_database()


# @bot.command()
# async def foo(ctx, arg):
#     await ctx.send(arg)


# def get_random_asmr_vtuber() -> str:
#   asmr_list = ASMR_VTUBER_LIST
#   random.shuffle(asmr_list)
#   return asmr_list[0]


# def get_all_db_keys():
#   return db.keys()


# def update_asmr_list(asmr_channel_name: str):
#   if "asmr_channel_name" in db.keys() :
#     asmr_channels = db["asmr_channel_name"]
#     asmr_channels.append(asmr_channel_name)
#     db["asmr_channel_name"] = asmr_channels
#   else:
#     db["asmr_channel_name"] = [asmr_channel_name]


# def get_all_asmr_list():
#   return db.get("asmr_channel_name")


@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    if message.content.startswith('!K hello'):
        await message.channel.send('Eyyy ヽ(*・ω・)ﾉ')
        await message.channel.send('Checkout Noel chan! XD \nhttps://www.youtube.com/@ShiroganeNoel')
  # elif message.content.startswith('!K random pic'):
  #   image = api.get_random_image(categories=["kemonomimi"])
  #   await message.channel.send("Here is a random animu pic Nyaaa (´• ω •`)")
  #   await message.channel.send(image.url)
  # elif message.content.startswith('!K cate'):
  #   categories = api.get_categories(limit=10, offset=0)
  #   for cat in categories:
  #     await message.channel.send(cat.name)
  #     await message.channel.send(cat.description)
  # elif message.content.startswith('!K asmr'):
  #   await message.channel.send(get_random_asmr_vtuber())
  #   print(message.content)
  # elif message.content.startswith('!K all db keys'):
  #   await message.channel.send(get_all_db_keys())
  # elif message.content.startswith('!K add'):
  #   new_asmr_channel_name = message.content.split()[-1]
  #   print(new_asmr_channel_name)
  #   update_asmr_list(new_asmr_channel_name)
  # elif message.content.startswith('!K list'):
  #   await message.channel.send(get_all_asmr_list())
    elif message.content.startswith('!K data'):
        await message.channel.send('==Connect to database!==')
        connect_to_database()
    elif message.content.startswith('!K print'):
        await message.channel.send('==Printing table!==')
        print_from_a_table()
    elif message.content.startswith('!K list'):
        await message.channel.send('==List all tables!==')
        list_all_tables()
    elif message.content.startswith('!K insert'):
        await message.channel.send('==insert nano into tables!==')
        insert_into_asmr("nano", "jp")
    else:
        await message.channel.send("Type: '!K hello' to start :)")


client.run(secrets.get("TOKEN"))
