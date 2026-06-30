class ChapterDownloadBuilder:

    def __init__(self, series_id):
        self.data = {
            "event": "chapter.download.requested",
            "series_id": series_id
        }

    def set_chapter_url(self, chapter: str):
        self.data["chapter_url"] = chapter
        return self
    
    def set_chapter_number(self, chapter: str):
        self.data["chapter_number"] = chapter
        return self
    
    def set_chapter_imgs(self, chapter):
        self.data["chapters_url"] = chapter ## Espera chapter_img y chapter_url
        return self