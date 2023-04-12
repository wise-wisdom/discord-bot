import random
from discord.ext import commands
from configs import get_token
import discord

TOKEN = get_token()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def 밥(ctx):
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




from pydantic import BaseModel, Field

class SummonerDTO(BaseModel):
    accountId: str = Field(
        ..., max_length=56,
description="Encrypted account ID. Max length 56 characters"
    )
    profileIconId: int = Field(
        ..., description="ID of the summoner icon associated with the summoner"
    )
    revisionDate: int = Field(
        ...,
        description="Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: summoner name change",
    )
    name: str = Field(..., description="Summoner name")
    id: str = Field(
        ...,
        max_length=63,
        description="Encrypted summoner ID. Max length 63 characters",
    )
    puuid: str = Field(
        ..., max_length=78, description="Encrypted PUUID. Exact length of 78 characters"
    )
    summonerLevel: int = Field(
        ..., min=1, description="Summoner level associated with the summoner"
    )




import asyncio
import aiohttp
import requests
import json
from models import SummonerDTO
from pprint import pprint

URL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}"
API_TOKEN = "RGAPI-bdd745ed-9636-4d2c-aa85-e9584c1be1a6"

HEADERS = {"X-Riot-Token": API_TOKEN}


NAME = "찾을 닉네임"


def 동기적으로_API_호출하기():
    resp = requests.get(URL.format(name=NAME ), headers=HEADERS)
    aa = resp.json()
    summoner = SummonerDTO(**aa)
    #pprint(summoner)


async def 비동기적으로_API_호출하기():
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.get(URL.format(name=NAME)) as response:
            #print("Status:", response.status)
            #print("Content-type:", response.headers["content-type"])
            html = await response.json()
            summoner = SummonerDTO(**html)
            #pprint(summoner)



if __name__ == "__main__":
    #동기적으로_API_호출하기()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(비동기적으로_API_호출하기())