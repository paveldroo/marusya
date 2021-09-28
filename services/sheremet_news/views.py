import json
import random

from aiohttp import web


async def sheremet_news(request_obj):
    request = await request_obj.json()

    response = {
        'version': request['version'],
        'session': request['session'],
        'response': {'end_session': False}
    }

    with open('sheremet_titles.json', 'r') as f:
        sheremet_titles = json.load(f)

    random.shuffle(sheremet_titles)
    text_for_response = ''
    for title in sheremet_titles[:20]:
        text_for_response += f'{title}. '

    response['response']['text'] = text_for_response
    response['response']['end_session'] = True

    return web.json_response(response)
