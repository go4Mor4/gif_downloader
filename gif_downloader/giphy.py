import json
import requests


class GiphyAPI:
    def __init__(self, key_word:str, limit:int, api_key:str):
        self.search_endpoint = "http://api.giphy.com/v1/gifs/search"
        self.params = {
            "q": key_word,
            "api_key": api_key,
            "limit": str(limit)
        }

    def search(self):
        try:
            response = requests.get(self.search_endpoint, params=self.params)
            response.raise_for_status()

        except requests.exceptions.HTTPError as e:
            print(f"Erro HTTP: {e.response.status_code} - {e.response.reason}")

        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")

        except Exception as e:
            print(f"Erro inesperado: {e}")

        else:
            data = response.json()
            gif_ids =  [i["embed_url"][24:] for i in data["data"]]

            return gif_ids
