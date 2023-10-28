from googleapiclient.discovery import build
import os


class Video:
    youtube = build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))

    def __init__(self, video_id):
        self.video_id = video_id
        try:
            video_response = self.youtube.videos().list(part='snippet, statistics, contentDetails, topicDetails',
                                                        id=self.video_id).execute()

            self.title = video_response['items'][0]['snippet']['title']
            self.video_link = f"https://youtu.be/{self.video_id}"
            self.view_count = video_response['items'][0]['statistics']['viewCount']
            self.like_count = video_response['items'][0]['statistics']['likeCount']

        except IndexError:
            self.title = None
            self.video_link = None
            self.view_count = None
            self.like_count = None

    def fetch_video_info(self):
        service = build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))
        video_response = service.videos().list(part='snippet, statistics', id=self.video_id).execute()
        self.title = video_response['items'][0]['snippet']['title']
        self.video_link = f"https://youtu.be/{self.video_id}"
        self.view_count = video_response['items'][0]['statistics']['viewCount']
        self.like_count = video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id  # Add the title parameter here
