from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services import manga_service
from models.request import MangaRequest, ChapterRequest, SearchRequest

router = APIRouter()

@router.get('/search')
async def search(data: SearchRequest):

    series_name = data.series_name

    return JSONResponse(await manga_service.search_series(series_name))

@router.get('/')
async def getManga(data: MangaRequest):
    
    series_url = data.series_url

    return JSONResponse(await manga_service.get_manga(series_url))

@router.get('/chapter/images')
async def getImages(data: ChapterRequest):

    chapter_url = data.series_url

    return JSONResponse(await manga_service.get_chapter_img(chapter_url))