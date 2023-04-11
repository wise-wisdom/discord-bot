import random
from discord.ext import commands
from configs import get_token

TOKEN = get_token()

bot = commands.Bot(command_prefix='!')

@bot.command()
async def 밥(ctx):
    food_options = [
        "피자",
        "햄버거",
        "치킨",
        "초밥",
        "파스타"
    ]
    
    random_choices = random.sample(food_options, 3)
    response = ', '.join(random_choices)
    await ctx.send(response)

bot.run(TOKEN)