from pydantic import BaseModel

class MangaRequest(BaseModel):
    series_url: str

class ChapterRequest(BaseModel):
    chapter_url: str

class SearchRequest(BaseModel):
    series_name: str