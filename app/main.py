from fastapi import FastAPI, Request, status
from fastapi.concurrency import asynccontextmanager
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from app.core.schemas import ErrorResponse, Root
from app.database import DB, seed_database
from app.esma.router import router as esma_router
from app.exceptions import ResourceNotFoundError
from app.surah.router import router as surah_router


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa: ARG001
    seed_database()
    yield
    DB.close()


description = """
# 📖 Esmaul Husna API

The **Esmaul Husna API** provides structured access to:

- The 99 Names of Allah (Asmaul Husna)
- Surahs of the Qur'an
- Multi-language support
- Optional pagination for collections

---

## 📜 License

This project is licensed under the MIT License.
"""

app = FastAPI(
    title="Esmaul Husna API",
    description=description,
    summary="REST API providing structured access to the 99 Names of Allah and Surahs",
    version="1.0.0",
    contact={
        "name": "API Support",
        "url": "https://github.com/Suleeyman/api-esmaul-husna",
        "email": "ozturksuleyman.dev@outlook.fr",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
        "identifier": "MIT",
    },
    lifespan=lifespan,
)

app.mount("/images", StaticFiles(directory="assets/static/images"), name="static")
app.mount("/audio", StaticFiles(directory="assets/static/audio"), name="static")

app.include_router(esma_router)
app.include_router(surah_router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_request: Request, exc: RequestValidationError):
    message = "Validation error"
    details = {}
    for error in exc.errors():
        loc = error["loc"]
        details[loc[1]] = f"{error['msg']} (got {error['input']})."
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=ErrorResponse(
            code=status.HTTP_400_BAD_REQUEST,
            message=message,
            details=details,
        ).model_dump(),
    )


@app.exception_handler(ResourceNotFoundError)
def exception_404_handler(_request: Request, exc: ResourceNotFoundError):
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            code=exc.status_code,
            message=exc.detail,
        ).model_dump(),
    )


@app.get(
    "/",
    tags=["Root"],
    summary="General API information",
    description="Returns general information about the API, including links to the GitHub repository, Swagger UI documentation, and ReDoc documentation.",
)
def root() -> Root:
    return Root(
        title="API Esmaul Husna",
        github_url="https://github.com/Suleeyman/api-esmaul-husna",
        swagger="/docs",
        redocly="/redoc",
    )
