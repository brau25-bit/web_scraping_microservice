from src.factory.source_factory import SourceFactory
from src.factory.parser_factory import ParserFactory
from src.models.image import Chapter
from src.models.search import MangaSearchResult
from src.models.manga import MangaDetails

async def search_series(series_name: str, source: str) -> MangaSearchResult:
    try:
        source_manga = SourceFactory.create_source(source)
        searchHTML = await source_manga.search(series_name)
        
        parser = ParserFactory.create_parser(source, searchHTML)
        parsedSearchResult = parser.search()
        
        return parsedSearchResult
    except Exception as e:
        raise e
    
async def get_manga(series_url: str, source: str) -> MangaDetails:
    try:
        manga_series = SourceFactory.create_source(source)
        manga_html = await manga_series.getSeries(series_url)

        parser = ParserFactory.create_parser(source, manga_html)
        parsed_result = parser.getSeries()
        
        return parsed_result
    except Exception as e:
        raise e

async def get_chapter_img(chapter_url: str, source: str) -> Chapter:
    try: 
        source_manga = SourceFactory.create_source(source)
        chapter_html = await source_manga.search(chapter_url)
        
        parser = ParserFactory.create_parser(source, chapter_html)
        parsedSearchResult = parser.getChapter()

        return parsedSearchResult
    except Exception as e:
        raise e