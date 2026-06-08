from src.sources.manhwa18_source import Manhwa18Source
from src.parsers.manhwa18_parser import Manhwa18Parser
from src.exception.error import CustomError
from src.models.image import Chapter
from src.models.search import MangaSearchResult
from src.models.manga import MangaDetails
from fastapi import HTTPException

source = Manhwa18Source()

async def search_series(series_name: str) -> MangaSearchResult:
    try:
        searchHTML = await source.search(series_name)
    
        if not searchHTML:
            raise CustomError("Content not found on source, try another name", 404, "source_problem")
        
        parser = Manhwa18Parser(searchHTML)
        
        parsedSearchResult = parser.search()

        if not parsedSearchResult:
            raise CustomError("Encountered a problem while parsing the page or the resource wasnt found", 404, "parsing_error")
        
        return parsedSearchResult
    except Exception as e:
        raise e
    
async def get_manga(series_url: str) -> MangaDetails:
    try:
        seriesHTML = await source.getSeries(series_url)
    
        if not seriesHTML:
            raise CustomError("There was a problem with the source, try again", 404, "source_problem")
        
        parser = Manhwa18Parser(seriesHTML)

        parsedSearchResult = parser.getSeries()

        if not parsedSearchResult:
            raise CustomError("Encountered a problem while parsing the page or the resource wasnt found", 404, "parsing_error")
        
        return parsedSearchResult
    except Exception as e:
        raise e

async def get_chapter_img(chapter_url: str) -> Chapter:
    try: 
        chaptersHTML = await source.getChapters(chapter_url)
    
        if not chaptersHTML:
            raise CustomError("There was a problem with the source, try again", 404, "source_error")
        
        parser = Manhwa18Parser(chaptersHTML)

        parsedSearchResult = parser.getChapter()

        if not parsedSearchResult:
            raise CustomError("Encountered a problem while parsing the page or the resource wasnt found", 404, "parsing_error")

        return parsedSearchResult
    except Exception as e:
        raise e