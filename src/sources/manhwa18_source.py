from src.core.http_client import HTTPXClient
from src.strategy.manga_strategy import MangaSource

import os
from dotenv import load_dotenv

load_dotenv()
httpx_client = HTTPXClient()

class Manhwa18Source(MangaSource):    
    base_url = os.getenv("MANHWA18_BASE_URL")

    async def search(self, series_name):
        result = await httpx_client.get(f"{self.base_url}search", series_name)

        result.raise_for_status()

        return result.text

    async def getSeries(self, series_url):
        result = await httpx_client.getSeries(series_url)

        result.raise_for_status()

        return result.text

    async def getChapters(self, chapter_url):
        result = await httpx_client.getChapters(chapter_url)

        result.raise_for_status()

        return result.text