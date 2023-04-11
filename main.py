from configs import get_token
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOKEN = get_token()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_massage(massage):
    if message.author == client.user:
        return

    if massage.content.startswith("!hello"):
        await massage.channel.send("Hello")



client.run(TOKEN)
