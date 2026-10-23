from pydantic import BaseModel
from .chapter import Chapter

class Manga(BaseModel):
    title: str
    cover: str
    manga_url: str
    last_chapter: str
    publishing_date: str

class PostContent(BaseModel):
    Release: str
    Status: str

class MangaDetails(BaseModel):
    post_content: PostContent
    chapters: list[Chapter]

