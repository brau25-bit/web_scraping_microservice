from src.exception.error import CustomError

class SearchBuilder:

    def __init__(self):
        self.data = {}

    def number(self, number: int):
        self.data["number"] = number
        return self
    
    def title(self, title: str):
        self.data["title"] = title
        return self

    def cover(self, cover: str):
        self.data["cover"] = cover
        return self

    def latest_chapter(self, latest_chap: str):
        self.data["latest_chapter"] = latest_chap
        return self

    def publish_date(self, publish_date: str):
        self.data["published_at"] = publish_date
        return self

    def series_url(self, series_url: str):
        self.data["series_url"] = series_url
        return self
    
    def build(self):

        if "title" not in self.data:
            raise CustomError("Title not found", 404, "title-not-found")
        
        if "series_url" not in self.data:
            raise CustomError("Series url couldn't be extracted", 404, "seriesurl-not-found")
        
        return self.data