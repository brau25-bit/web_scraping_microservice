from sources.manhwa18_source import Manhwa18Source
from parsers.manhwa18_parser import Manhwa18Parser
from exception.error import CustomError
from models.image import Chapter
from models.search import MangaSearchResult
from models.manga import MangaDetails
from fastapi import HTTPException

async def search_series(series_name: str) -> MangaSearchResult:
    searchHTML = await Manhwa18Source.search(series_name)
    
    if not searchHTML:
        raise CustomError("Content not found on source, try another name", 404, "source_problem")
    
    parsedSearchResult = await Manhwa18Parser.search(searchHTML)

    if not parsedSearchResult:
        raise CustomError("Encountered a problem while parsing the page or the resource wasnt found", 404, "parsing_error")
    
    return parsedSearchResult

async def get_manga(series_url: str) -> MangaDetails:
    seriesHTML = await Manhwa18Source.getSeries(series_url)
    
    if not seriesHTML:
        raise CustomError("There was a problem with the source, try again", 404, "source_problem")
    
    parsedSearchResult = await Manhwa18Parser.getSeries(seriesHTML)

    if not parsedSearchResult:
        raise CustomError("Encountered a problem while parsing the page or the resource wasnt found", 404, "parsing_error")
    
    return parsedSearchResult

async def get_chapter_img(chapter_url: str) -> Chapter:
    chaptersHTML = await Manhwa18Source.getChapters(chapter_url)
    
    if not chaptersHTML:
        raise CustomError("There was a problem with the source, try again", 404, "source_error")
    
    parsedSearchResult = await Manhwa18Parser.getChapters(chaptersHTML)

    if not parsedSearchResult:
        raise CustomError("Encountered a problem while parsing the page or the resource wasnt found", 404, "parsing_error")
    
    return parsedSearchResult