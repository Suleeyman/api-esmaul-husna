from fastapi import APIRouter
from tinydb import Query as dbQuery

from app.core.language import Lang, LanguageQuery
from app.core.pagination import PaginatedResponse, PaginationQueries, paginate
from app.core.utils import not_found_response_annotation
from app.database import DB
from app.surah.dependencies import SurahNumber
from app.surah.exceptions import SurahNotFoundError
from app.surah.schema import SurahSchema

surah_table = DB.table("surah")


def filter_surah_by_lang(item: dict, lang: Lang) -> dict:
    return {
        **item,
        "name": item["name"].get(lang),
    }


router = APIRouter(
    prefix="/surah",
    tags=[
        "Surah",
    ],
)


@router.get(
    "/",
    summary="List all Surahs",
    description="Retrieve all Surahs with optional language filtering and pagination. Each Surah object includes the Esma IDs appearing on it.",
    response_description="Paginated list of Surahs",
)
def get_sourates_esma(
    pagination_queries: PaginationQueries,
    lg: LanguageQuery,
) -> PaginatedResponse[SurahSchema]:
    data = surah_table.all()
    page, limit = pagination_queries["page"], pagination_queries["limit"]

    # Filtrage langue
    if lg is not None:
        data = [filter_surah_by_lang(item, lg) for item in data]

    return paginate(data, page, limit)


@router.get(
    "/{number}",
    summary="Get Surah by number",
    description="Retrieve a Surah by its number with optional language filtering.",
    responses={
        404: not_found_response_annotation("Surah"),
    },
)
def get_sourates_esma_by_id(
    number: SurahNumber,
    lg: LanguageQuery,
) -> SurahSchema:
    surah = surah_table.get(dbQuery().number == number)
    if not surah:
        raise SurahNotFoundError(number)

    if lg is None:
        return surah

    return filter_surah_by_lang(surah, lg)
