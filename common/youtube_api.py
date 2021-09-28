import json
import os

from googleapiclient.discovery import build


def youtube_api_init():
    youtube_api_key = os.getenv('YOUTUBE_API_KEY')
    youtube_api_service_name = "youtube"
    youtube_api_version = "v3"

    return build(youtube_api_service_name, youtube_api_version, developerKey=youtube_api_key)


def youtube_search():
    youtube_api = youtube_api_init()
    sheremet_channel_id = 'UCW-EN3hRb9hQwhkMcGzhJUQ'

    video_titles = []
    next_page_token = None
    cnt = 9
    while cnt <= 10:
        response = youtube_api.search().list(
            part="id,snippet",
            channelId=sheremet_channel_id,
            pageToken=next_page_token,
            maxResults=50
        ).execute()

        next_page_token = response['nextPageToken']
        cnt += 1

        current_video_titles = []
        for item in response['items']:
            title = item['snippet']['title']
            title = title.replace('Real video', '').replace('&quot;', '').replace('Real Video', '')
            current_video_titles.append(title)

        video_titles += current_video_titles

    with open('sheremet_titles.json', 'w') as f:
        json.dump(video_titles, f)
