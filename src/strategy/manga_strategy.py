from abc import ABC, abstractmethod

class MangaSource(ABC):

    @abstractmethod
    async def search(self, query):
        pass

    @abstractmethod
    async def getSeries(self, query):
        pass

    @abstractmethod
    async def getChapters(self, query):
        pass