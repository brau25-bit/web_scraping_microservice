from pydantic import BaseModel

class Chapter(BaseModel):
    chapter: str
    chapter_release_date: str
    chapter_url: str
