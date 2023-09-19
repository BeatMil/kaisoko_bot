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


@client.command()
async def yoo(ctx):
    await ctx.send("Yoo ready for some asmr? XD")


@client.tree.command(name="yooyoo")
async def yooyoo(interaction: discord.Interaction):
    await interaction.response.send_message(
            f"Yooyoo {interaction.user.mention}", ephemeral=True)


@client.tree.command(name="say")
@app_commands.describe(thing_to_say = "What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(
            f"{interaction.user.name} said: {thing_to_say}", ephemeral=True)


client.run(secrets.get("TOKEN"))
