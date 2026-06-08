# Manga Library Server - web scraping microservice
Esta API de python esta diseñada como microservicio para hacer web scraping a sitios cuyo contenido es manga/manhua/manhwa.

## Caracteristicas

- Scraping de múltiples sitios
- Rotación de User-Agent
- Reintentos automáticos
- Parseo HTML
- API REST

## Tecnologias

* Python
* FastAPI
* pydantic
* BeautifulSoup
* httpx

## Arquitectura
```
src/
|
|--main.py
|
|--routes/
|  
|--sources/
|  |--manhwa18.py
|  |--toonily.py
|
|--parsers/
|  |--manga_parser.py
|  |--chapter_parser.py
|
|--models/
|  |--manga.py
|  |--chapter.py
|
|--core/
|  |--http_client.py
|  |--exceptions.py
|  |--config.py
|
|--exception/
|  |-error.py
```

## flujo del sistema


## Endpoints

GET manga/search
```json
{
    "series_name": "blood"
}
```

Respuesta esperada: 
```json
[
    {
        "number": 1,
        "title": "White Blood",
        "cover": "https://manhwa18.cc/manga/white-bloodczv.jpg",
        "latest_chapter": " Chapter 92.5 ",
        "published_at": "Nov 03, 2021",
        "series_url": "https://manhwa18.cc/webtoon/white-blood"
    },
    {
        "number": 2,
        "title": "Revenge of the Iron-Blooded Sword Hound",
        "cover": "https://manhwa18.cc/manga/revenge-of-the-iron-blooded-sword-houndm.jpg",
        "latest_chapter": " Chapter 165 ",
        "published_at": "May 31, 2026",
        "series_url": "https://manhwa18.cc/webtoon/revenge-of-the-iron-blooded-sword-hound"
    }
]
```

GET manga/
```json
{
    "series_url": "https://manhwa18.cc/webtoon/revenge-of-the-iron-blooded-sword-hound"
}
```

Respuesta esperada: 
```json
{
    "post_content": {
        "Release": "2023",
        "Status": "OnGoing"
    },
    "chapters": [
        {
            "chapter": "Chapter 166",
            "chapter_release_date": "NEW",
            "chapter_url": "https://manhwa18.cc/webtoon/revenge-of-the-iron-blooded-sword-hound/chapter-166"
        },
        {
            "chapter": "Chapter 165",
            "chapter_release_date": "31 May 2026",
            "chapter_url": "https://manhwa18.cc/webtoon/revenge-of-the-iron-blooded-sword-hound/chapter-165"
        }
    ]
}
```

GET manga/chapter
```json
{
    "chapter_url": "https://manhwa18.cc/webtoon/revenge-of-the-iron-blooded-sword-hound/chapter-166"
}
```

Respuesta esperada: 
```json
{
    "chapter": 166,
    "manga_chapter": [
        {
            "page_number": 1,
            "image": "https://img01.manhwa18.cc/online/3835/166/1-b3bf3.jpg"
        },
        {
            "page_number": 2,
            "image": "https://img01.manhwa18.cc/online/3835/166/2-b3bf3.jpg"
        },
        {
            "page_number": 3,
            "image": "https://img01.manhwa18.cc/online/3835/166/3-b3bf3.jpg"
        },
        {
            "page_number": 4,
            "image": "https://img01.manhwa18.cc/online/3835/166/4-b3bf3.jpg"
        },
        {
            "page_number": 5,
            "image": "https://img01.manhwa18.cc/online/3835/166/5-b3bf3.jpg"
        },
        {
            "page_number": 6,
            "image": "https://img01.manhwa18.cc/online/3835/166/6-b3bf3.jpg"
        },
        {
            "page_number": 7,
            "image": "https://img01.manhwa18.cc/online/3835/166/7-b3bf3.jpg"
        },
        {
            "page_number": 8,
            "image": "https://img01.manhwa18.cc/online/3835/166/8-b3bf3.jpg"
        },
        {
            "page_number": 9,
            "image": "https://img01.manhwa18.cc/online/3835/166/9-b3bf3.jpg"
        },
        {
            "page_number": 10,
            "image": "https://img01.manhwa18.cc/online/3835/166/10-b3bf3.jpg"
        },
        {
            "page_number": 11,
            "image": "https://img01.manhwa18.cc/online/3835/166/11-b3bf3.jpg"
        },
        {
            "page_number": 12,
            "image": "https://img01.manhwa18.cc/online/3835/166/12-b3bf3.jpg"
        },
        {
            "page_number": 13,
            "image": "https://img01.manhwa18.cc/online/3835/166/13-b3bf3.jpg"
        },
        {
            "page_number": 14,
            "image": "https://img01.manhwa18.cc/online/3835/166/14-b3bf3.jpg"
        },
        {
            "page_number": 15,
            "image": "https://img01.manhwa18.cc/online/3835/166/15-b3bf3.jpg"
        },
        {
            "page_number": 16,
            "image": "https://img01.manhwa18.cc/online/3835/166/16-b3bf3.jpg"
        },
        {
            "page_number": 17,
            "image": "https://img01.manhwa18.cc/online/3835/166/17-b3bf3.jpg"
        },
        {
            "page_number": 18,
            "image": "https://img01.manhwa18.cc/online/3835/166/18-b3bf3.jpg"
        },
        {
            "page_number": 19,
            "image": "https://img01.manhwa18.cc/online/3835/166/19-b3bf3.jpg"
        },
        {
            "page_number": 20,
            "image": "https://img01.manhwa18.cc/online/3835/166/20-b3bf3.jpg"
        },
        {
            "page_number": 21,
            "image": "https://img01.manhwa18.cc/online/3835/166/21-b3bf3.jpg"
        }
    ]
}
```

****
TO DO: 

    1. Retries
    2. Headers realistas
    3. DTOs
    4. Strategy
    5. Factory
    6. Dependency Injection
    7. Adapter
    8. Builder
    9. Redis Cache
    10. Redis Queue
    11. Workers de descarga