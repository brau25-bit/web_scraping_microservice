from pydantic import BaseModel

class Download(BaseModel):
    id: str
    source: str
    series: Series
    chapters: list[Chapters]

class Series(BaseModel):
    title: str
    cover: str
    release: str
    status: str
    url: str

class Chapters(BaseModel):
    chapter: str
    chapter_url: str

class Chapter(BaseModel):
    image_number: int
    image_url: str