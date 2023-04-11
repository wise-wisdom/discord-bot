import random
from discord.ext import commands
from configs import get_token
import discord

TOKEN = get_token()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def 오늘뭐먹지(ctx):
    food_options = [
        "지지고",
        "프랭크버거",
        "한끼철판",
        "푸른스시",
        "후문식당"
    ]

    random_choices = random.sample(food_options, 3)
    response = ', '.join(random_choices)
    await ctx.send(response)

bot.run(TOKEN)