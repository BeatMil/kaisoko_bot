import discord
from discord import app_commands
from discord.ext import commands
from secrets import secrets 


client = commands.Bot(command_prefix='!', intents=discord.Intents.default())


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


@client.tree.command(name="yooyoo")
async def yooyoo(interaction: discord.Interaction):
    await interaction.response.send_message(
            f"Yooyoo {interaction.user.mention}", ephemeral=True)


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
    # await interaction.response.send_message(
    #         f"{interaction.user.name} said: {thing_to_say}", ephemeral=True)


client.run(secrets.get("TOKEN"))
