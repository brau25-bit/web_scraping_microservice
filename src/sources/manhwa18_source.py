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
        
        print(result.status_code)

        return result.text

    async def getSeries(series_url):
        return

    async def getChapters(chapter_url):
        return