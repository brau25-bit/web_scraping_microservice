
class ChapterImgBuilder:

    def __init__(self):
        self.data = {}

    def page_number(self, page_number: int):
        self.data["page_number"] = page_number
        return self

    def image(self, image_url: str):
        self.data["image"] = image_url
        return self
    
    def build(self):
        return self.data

class EspecifiedChapterBuilder:
    def __init__(self):
        self.data = {}

    def chapter(self, chapter):
        self.data["chapter"] = chapter
        return self
    
    def manga_chapter(self, manga_chapter):
        self.data["manga_chapter"] = manga_chapter
        return self
    
    def build(self):
        return self.data