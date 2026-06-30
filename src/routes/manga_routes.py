from fastapi import APIRouter
from src.services import manga_service
from src.models.request import MangaRequest, ChapterRequest, SearchRequest
from src.models.download import Download

router = APIRouter()

@router.get('/search')
async def search(data: SearchRequest):

    series_name = data.series_name
    source = data.source

    result = await manga_service.search_series(series_name, source)

    return result

@router.get('/')
async def getManga(data: MangaRequest):
    
    series_url = data.series_url
    source = data.source

    return await manga_service.get_manga(series_url, source)

@router.get('/chapter')
async def getImages(data: ChapterRequest):

    chapter_url = data.chapter_url
    source = data.source

    return await manga_service.get_chapter_img(chapter_url, source)

@router.post('/download')
async def downloadChapters(data: Download):
    return await manga_service.publish_download(data)