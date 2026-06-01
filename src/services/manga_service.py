from sources.manhwa18_source import Manhwa18Source
from parsers.manhwa18_parser import Manhwa18Parser
from models.image import Chapter
from models.search import MangaSearchResult
from models.manga import MangaDetails

async def search_series(series_name: str) -> MangaSearchResult:
    searchHTML = await Manhwa18Source.search(series_name)
    
    if searchHTML:
        raise Exception("")
    
    parsedSearchResult = await Manhwa18Parser.search(searchHTML)

    if parsedSearchResult:
        raise Exception("")
    
    return parsedSearchResult

async def get_manga(series_url: str) -> MangaDetails:
    searchHTML = await Manhwa18Source.search(series_url)
    
    if searchHTML:
        raise Exception("")
    
    parsedSearchResult = await Manhwa18Parser.search(searchHTML)

    if parsedSearchResult:
        raise Exception("")
    
    return parsedSearchResult

async def get_chapter_img(chapter_url: str) -> Chapter:
    searchHTML = await Manhwa18Source.search(chapter_url)
    
    if searchHTML:
        raise Exception("")
    
    parsedSearchResult = await Manhwa18Parser.search(searchHTML)

    if parsedSearchResult:
        raise Exception("")
    
    return parsedSearchResult