import os
from dotenv import load_dotenv
from src.core.http_client import HTTPX

load_dotenv()
httpx_client = HTTPX()

class Manhwa18Source:    
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