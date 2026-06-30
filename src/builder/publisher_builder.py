import uuid

class SeriesDiscoveredBuilder:
    def __init__(self):
        self.data = {
            "event": "series.discovered",
            "series_id": str(uuid.uuid4())
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

    def build(self):
        return self.data