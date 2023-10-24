import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

        self.__channel_id = channel_id
        self.api_key = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.subscriberCount = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.view_count = self.channel["items"][0]["statistics"]["viewCount"]

    def to_json(self, file):
        attrib_dict = {"channel_id": self.__channel_id,
                       "title": self.title,
                       "description": self.description,
                       "url": self.url,
                       "subscribers_channel": self.subscriberCount,
                       "video_count": self.video_count,
                       "view_count": self.view_count}
        with open(file, "w", encoding='utf-8') as f:
            json.dump(attrib_dict, f, indent=2, ensure_ascii=False)

    def __str__(self):
        return (f"Название канала:{self.title}.\nОписание канала: {self.description}"
                f" ,\nКоличество подписчиков: {self.subscriberCount},\nКоличество видео на канале: {self.video_count},\n"
                f"Количество просмотров на канале: {self.view_count}.")

    def __add__(self, other):
        """Суммарное количество просмотров двух каналов"""
        subscriberCount_1 = self.subscriberCount
        subscriberCount_2 = other.subscriberCount
        return int(subscriberCount_1) + int(subscriberCount_2)

    def __sub__(self, other):
        """Разница количества просмотров двух каналов"""
        subscriberCount_1 = self.subscriberCount
        subscriberCount_2 = other.subscriberCount
        return int(subscriberCount_1) - int(subscriberCount_2)

    def __eq__(self, other):
        """Сравнение на равенство"""
        subscriberCount_1 = self.subscriberCount
        subscriberCount_2 = other.subscriberCount
        return int(subscriberCount_1) == int(subscriberCount_2)

    def __lt__(self, other):
        """Сравнение операторов (меньше)"""
        subscriberCount_1 = self.subscriberCount
        subscriberCount_2 = other.subscriberCount
        return subscriberCount_1 < subscriberCount_2

    def __le__(self, other):
        """Сравнение операторов (меньше или равно)"""
        subscriberCount_1 = self.subscriberCount
        subscriberCount_2 = other.subscriberCount
        return int(subscriberCount_1) <= int(subscriberCount_2)

    def __gt__(self, other):
        """Сравнение операторов (больше)"""
        subscriberCount_1 = self.subscriberCount
        subscriberCount_2 = other.subscriberCount
        return int(subscriberCount_1) > int(subscriberCount_2)

    def __ge__(self, other):
        """Сравнение операторов (больше или равно)"""
        subscriberCount_1 = self.subscriberCount
        subscriberCount_2 = other.subscriberCount
        return int(subscriberCount_1) >= int(subscriberCount_2)

    def print_info(self) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))
