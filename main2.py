import discord
import random
from discord import app_commands
from discord.ext import commands
from secrets import secrets 


client = commands.Bot(command_prefix='!', intents=discord.Intents.default())

choice_to_emoji = {
    "rock": "🪨",
    "paper": "🧻",
    "scissor": "✂️",
}


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@client.event
async def on_message(message):
    # don't reply to it's own message
    if message.author == client.user:
        return 

    await message.channel.send('Eyyy ヽ(*・ω・)ﾉ')
    await message.channel.send('Try "/" commands! ( ^▽^)ψ__')


@client.command()
async def yoo(ctx):
    await ctx.send("Yoo ready for some asmr? XD")


@client.tree.command(name="rockpaperscissor")
@app_commands.choices(choices=[
    app_commands.Choice(name="Rock", value="rock"),
    app_commands.Choice(name="Paper", value="paper"),
    app_commands.Choice(name="Scissor", value="scissor"),
    ])
@app_commands.describe(choices = "Play rock paper scissor with me!")
async def rockpaperscissor(
        interaction: discord.Interaction,
        choices: app_commands.Choice[str]
        ):
    bot_choose = random.choices(['rock', 'paper', 'scissor'])[0]
    player = choices.value
    text = ""
    if bot_choose == player:
        text += "Draw!\n"
    elif (bot_choose == "rock" and player == "paper") or \
         (bot_choose == "paper" and player == "scissor") or \
         (bot_choose == "scissor" and player == "rock"):
        text += "You win! 🎉🎉*clap* *clap*"
    else:
        text += "You lose! XD 💥💥💥"

    await interaction.response.send_message(
            f"{text}\nYou: {choice_to_emoji.get(player)}\nMe: {choice_to_emoji.get(bot_choose)}")


@client.tree.command(name="gimme")
@app_commands.choices(choices=[
    app_commands.Choice(name="ENG", value="eng"),
    app_commands.Choice(name="JAP", value="jap"),
    app_commands.Choice(name="All", value="all"),
    ])
@app_commands.describe(choices = "Give random asmr vtuber")
async def gimme(
        interaction: discord.Interaction,
        choices: app_commands.Choice[str]):
    if choices.value == "eng":
        await interaction.response.send_message(
                f"Smuggy smol\nhttps://www.youtube.com/@fallenshadow")
    elif choices.value == "jap":
        await interaction.response.send_message(
                f"Onee-chan typePu\nhttps://www.youtube.com/@YuuRi_Channel_")
    elif choices.value == "all":
        await interaction.response.send_message(
                f"My secret fav one XD\nhttps://www.youtube.com/@yuchorinchan")


client.run(secrets.get("TOKEN"))
