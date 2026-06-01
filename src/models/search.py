from pydantic import BaseModel

class MangaSearchResult(BaseModel):
    title: str
    cover: str
    latest_chapter: str
    published_at: str
    series_url: str