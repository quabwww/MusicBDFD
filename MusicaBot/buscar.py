from youtubesearchpython import VideosSearch
import json

def search_youtube(text: str):
    videos_search = VideosSearch(text, limit=1)  # Limitamos la búsqueda a 1 video
    results = obj=videos_search.result()["result"][0]["link"]
    return results

