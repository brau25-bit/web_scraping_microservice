from pydantic import BaseModel

class Chapter(BaseModel):
    chapter_number: int
    chapter_url: str
