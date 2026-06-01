# Manga Library Server - web scraping microservice
Esta API de python esta diseñada como microservicio para hacer web scraping a sitios cuyo contenido es manga/manhua/manhwa.

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

### Responsabilidad de cada recurso
1. Sources: dentro de esta carpeta se definiran la logica especifica para cada sitio
2. Parsers: Transforman el HTML de las peticiones a datos estructurados
3. Services: Se encargan de la orquestacion de logica.
4. Models: Se define la estructura de los modelos