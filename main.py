import random
from configs import get_token
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOKEN = get_token()

responses = [
    "첫 번째 답변",
    "두 번째 답변",
    "세 번째 답변",
    "네 번째 답변",
    "다섯 번째 답변"
]

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!광운"):
        random_responses = random.sample(responses, 3)
        response = ', '.join(random_responses)
        await message.channel.send(response)

client.run(TOKEN)
