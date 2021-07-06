import json
import random

import requests
from aiogram.types import Message
from environs import Env


async def send_gif(message: Message):
    """
    send animation
    """

    env = Env()
    env.read_env()
    gifs = []
    search = message.text.split(' ')[1:]
    api_key = env.str("GIF_API_KEY")
    limit = 8

    # get the top 8 GIFs for the search term
    r = requests.get(f"https://g.tenor.com/v1/search?q={search}&key={api_key}&limit={limit}")

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_gifs = json.loads(r.content)
        for gif in top_gifs['results']:
            gifs.append(gif['url'])
        await message.answer_animation(random.choice(gifs))
    else:
        await message.answer("not find")
