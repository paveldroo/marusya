from dotenv import load_dotenv

from youtube_api import youtube_search


def debug():
    load_dotenv('.env')
    youtube_search()
    return


if __name__ == '__main__':
    debug()
