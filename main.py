import discord
from discord import app_commands
import pytube as pt

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "conect", description = "conects to vc", guild=discord.Object(id="your guild id here with no quotes"))
async def first_command(interaction):
    voice_channel = client.get_channel("your voice channel id here with no quotes")
    await voice_channel.connect()


@tree.command(name = "play", description = "plays a song", guild=discord.Object(id="your guild id here with no quotes"))
@app_commands.describe(
    song_name='the url of the song you want to play'
)
async def first_command(interaction, song_name: str):
    yt = pt.YouTube(song_name)
    t = yt.streams.filter(only_audio=True)
    t[0].download()
    print(t[0].default_filename)
    voice_client = discord.utils.get(client.voice_clients, guild=interaction.guild)
    voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=t[0].default_filename))


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id="your guild id here"))
    print("Ready!")

client.run("your bot token")