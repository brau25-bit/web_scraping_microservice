class ChapterDownloadBuilder:

    def __init__(self, series_id):
        self.data = {
            "event": "chapter.download.queue",
            "series_id": series_id
        }

    def set_chapter_number(self, chapter: str):
        self.data["chapter_number"] = chapter
        return self

    def set_chapter_url(self, chapter: str):
        self.data["chapter_url"] = chapter
        return self
    
    def set_chapter_imgs(self, chapter):
        self.data["chapter_images"] = chapter ## Espera chapter_img y chapter_url
        return self
    
    def build(self):
        required = [
            "chapter_number",
            "chapter_url",
            "chapter_images"
        ]

        for field in required:
            if field not in self.data:
                raise ValueError(f"{field} is required")
            
        return self.data