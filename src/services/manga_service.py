from src.factory.source_factory import SourceFactory
from src.factory.parser_factory import ParserFactory
from src.models.image import Chapter
from src.models.search import MangaSearchResult
from src.models.manga import MangaDetails
from src.core.rabbitMQ import RabbitClient
from src.builder.chapter_publisher_builder import ChapterDownloadBuilder
from src.builder.publisher_builder import SeriesDiscoveredBuilder
import uuid

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
        chapter_html = await source_manga.getChapters(chapter_url)
        
        parser = ParserFactory.create_parser(source, chapter_html)
        parsedSearchResult = parser.getChapter()

        return parsedSearchResult
    except Exception as e:
        raise e
    
async def publish_download(data):
    try:
        rabbit = RabbitClient()
        await rabbit.connect()

        source = data.source
        series_url = data.series.url

        series_info = (
            SeriesDiscoveredBuilder()
            .set_source(source)
            .set_title(data.series.title)
            .set_cover(data.series.cover)
            .set_serie_url(data.series.url)
            .build()
        )      

        serie_event = series_info["event"]

        await rabbit.create_queue(serie_event)
        await rabbit.publish(serie_event, series_info)

        id = series_info["id"]

        for chapter in data.chapters:
            chapter_img = await get_chapter_img(chapter.chapter_url, source)

            chapter_number = chapter_img["chapter"]

            chapter_imgs = chapter_img["manga_chapter"]

            chapter_build = (
                ChapterDownloadBuilder(id)
                .set_chapter_url(series_url)
                .set_chapter_number(chapter_number)
                .set_chapter_imgs(chapter_imgs)
                .build()
            )
            
            event = chapter_build["event"]

            await rabbit.create_queue(event)
            await rabbit.publish(event, chapter_build)
        
        rabbit.close()
        
        return "Finalizado"
    except Exception as e:
        raise e