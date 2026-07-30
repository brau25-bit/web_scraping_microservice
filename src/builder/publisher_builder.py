import uuid

class SeriesDiscoveredBuilder:
    def __init__(self):
        self.data = {
            "event": "series.discovered.queue",
            "id": str(uuid.uuid4())
        }

    def set_source(self, source: str):
        self.data["source"] = source
        return self
    
    def set_title(self, title: str):
        self.data["title"] = title
        return self
    
    def set_cover(self, cover: str):
        self.data["cover"] = cover
        return self
    
    def set_serie_url(self, url: str):
        self.data["serie_url"] = url
        return self

    def set_status(self, status: str):
        self.data["status"] = status
        return self

    def build(self):
        return self.data