from fastapi import FastAPI
from routes import manga_routes
from exception.error import CustomError
from fastapi.responses import JSONResponse

app = FastAPI()

app.include_router(manga_routes.router, prefix='/manga')

@app.exception_handler(CustomError)
async def custom_error_handler(exc: CustomError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.message,
            "error_code": exc.error_code
        }
    )