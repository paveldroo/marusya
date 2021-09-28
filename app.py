from aiohttp import web
from dotenv import load_dotenv

from services.sheremet_news.views import sheremet_news
from services.space_quest.views import skill_space_quest


async def index(request):
    return web.Response(text='Welcome home!')


async def marusya():
    load_dotenv('.env')
    app = web.Application()
    app.router.add_get('/', index)
    app.router.add_post('/skill_test', skill_space_quest)
    app.router.add_post('/sheremet_news', sheremet_news)
    # web.run_app(app, host=HOST_IP, port=HOST_PORT)
    return app


# if __name__ == '__main__':
#     marusya_pomodoro_app()

