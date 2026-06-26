
class ChapterBuilder:

    def __init__(self):
        self.data = {}

    def chapter(self, chapter: str):
        self.data["chapter"] = chapter
        return self
    
    def chapter_release_date(self, chapter_date: str):
        self.data["chapter_release_date"] = chapter_date
        return self
    
    def chapter_url(self, chapter_url: str):
        self.data["chapter_url"] = chapter_url
        return self
    
    def build(self):
        return self.data
    
class SeriesBuilder:
    def __init__(self):
        self.data = {}

    def post_content(self, post_content):
        self.data["post_content"] = post_content
        return self
    
    def chapters(self, chapters):
        self.data["chapters"] = chapters
        return self
    
    def build(self):
        return self.data