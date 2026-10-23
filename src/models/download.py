from pydantic import BaseModel

class Chapters(BaseModel):
    chapter: str
    chapter_release_date: str
    chapter_url: str

class Series(BaseModel):
    title: str
    cover: str
    release: str
    status: str
    url: str
class Download(BaseModel):
    id: str
    source: str
    series: Series
    chapters: list[Chapters]
class Chapter(BaseModel):
    image_number: int
    image_url: str