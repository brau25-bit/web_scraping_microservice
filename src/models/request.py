from pydantic import BaseModel

class MangaRequest(BaseModel):
    series_url: str
    source: str

class ChapterRequest(BaseModel):
    chapter_url: str
    source: str

class SearchRequest(BaseModel):
    series_name: str
    source: str