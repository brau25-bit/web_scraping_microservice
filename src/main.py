from fastapi import FastAPI
from routes import manga_routes

app = FastAPI()

app.include_router(manga_routes.router, prefix='/manga')