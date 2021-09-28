from aiohttp import web

from services.space_quest import state


async def skill_space_quest(request_obj):
    request = await request_obj.json()

    response = {
        'version': request['version'],
        'session': request['session'],
        'response': {'end_session': False}
    }
    user_state = state.get_state(request)





    user_state.save_session_state(response)
    response['response']['text'] = 'Привет'
    response['response']['end_session'] = True

    return web.json_response(response)
