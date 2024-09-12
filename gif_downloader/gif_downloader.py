import os
import requests
from .giphy import GiphyAPI


class GifDownloader:
    def __init__(self, key_word:str, 
                        download_path:str,
                        api_key:str,
                        limit:int=5):

        self.key_word = key_word
        self.download_path = download_path
        self.api_key = api_key
        self.limit = limit

    @property
    def download_path(self):
        return self._download_path

    @download_path.setter
    def download_path(self, value):
        if not os.path.isdir(value):
            raise TypeError(f"Invalid path : {value}")

        self._download_path = value

    def download(self, gif_id:str, gif_name:str):
        download_url = f"https://media.giphy.com/media/{gif_id}/giphy.gif"

        with open(fr"{self.download_path}/{gif_name}.gif", 'wb') as f:
            f.write(requests.get(download_url).content)

    def run(self):
        gif_ids = GiphyAPI(self.key_word, self.limit, self.api_key).search()

        for n, g_id in enumerate(gif_ids):
            self.download(gif_id=g_id, gif_name=f"gif_{n+1}")
