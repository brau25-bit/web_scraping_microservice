from fastapi import FastAPI
from src.routes import manga_routes
from src.exception.error import CustomError
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(CustomError)
async def custom_error_handler(request, exc: CustomError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.message,
            "error_code": exc.error_code
        }
    )

app.include_router(manga_routes.router, prefix='/manga')

