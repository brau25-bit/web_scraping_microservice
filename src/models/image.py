from pydantic import BaseModel

class ChapterImages(BaseModel):
    image_number: int
    image_url: str

class Chapter(BaseModel):
    chapter_number: int
    images: list[ChapterImages]