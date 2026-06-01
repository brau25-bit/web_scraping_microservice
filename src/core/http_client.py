import httpx

HEADERS = {
    "Accept-Language":"en-US,en;q=0.8",
    "Referer": "https://manhwa18.cc/",
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/148.0.0.0 "
        "Safari/537.36"
    )
}

class HTTPX:
    def __init__(self):
        self.client = httpx.AsyncClient(
            headers=HEADERS,
            timeout=30,
            follow_redirects=True
        )
    
    async def get(self, base_url: str, param: str):
        try:
            search_request = await self.client.get(
                base_url, 
                params={"q": param}
            )
            
            return search_request
        
        except Exception as e:
            raise e
        
    async def getSeries(self, series_url: str):
        try:
            series_request = await self.client.get(series_url)

            return series_request
        
        except Exception as e:
            raise e
        
    async def getChapters(self, chapter_url):
        try:
            result = await self.client.get(chapter_url)

            result.raise_for_status()
            
            return result
        except Exception as e:
            raise e