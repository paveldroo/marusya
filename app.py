from aiohttp import web
from dotenv import load_dotenv

from sheremet_news import sheremet_news


async def index(request):
    return web.Response(text='Welcome home!')


async def skill_test(request_obj):
    request = await request_obj.json()

    response = {
        'version': request['version'],
        'session': request['session'],
        'response': {'end_session': False}
    }

    response['response']['text'] = 'Привет'
    response['response']['end_session'] = True

    return web.json_response(response)


async def marusya():
    load_dotenv('.env')
    app = web.Application()
    app.router.add_get('/', index)
    app.router.add_post('/skill_test', skill_test)
    app.router.add_post('/sheremet_news', sheremet_news)
    # web.run_app(app, host=HOST_IP, port=HOST_PORT)
    return app


# if __name__ == '__main__':
#     marusya_pomodoro_app()

