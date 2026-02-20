from fastapi import APIRouter, HTTPException, status
from tinydb import Query as dbQuery

from app.core.language import Lang, LanguageQuery
from app.core.pagination import PaginatedResponse, PaginationQueries, paginate
from app.core.utils import not_found_response_annotation
from app.database import DB
from app.esma.dependencies import EsmaId, EsmaSlug
from app.esma.schema import EsmaSchema

esma_table = DB.table("esma")


def filter_esma_by_lang(item: dict, lang: Lang) -> dict:
    return {
        **item,
        "name": item["name"].get(lang),
        "explanation": {
            "short": item["explanation"]["short"].get(lang, ""),
            "long": item["explanation"]["long"].get(lang, ""),
        },
        "transliteration": {
            **item["transliteration"],
            "popular": item["transliteration"]["popular"].get(lang),
        },
    }


router = APIRouter(
    prefix="/esmas",
    tags=["Esma"],
)


@router.get(
    "/",
    summary="List all Esmas",
    description="Retrieve all Esmas with optional language filtering and pagination.",
    response_description="Paginated list of Esmas",
)
def get_esmas(
    lg: LanguageQuery,
    pagination_queries: PaginationQueries,
) -> PaginatedResponse[EsmaSchema]:
    data = esma_table.all()
    page, limit = pagination_queries["page"], pagination_queries["limit"]

    if lg is not None:
        data = [filter_esma_by_lang(item, lg) for item in data]

    return paginate(data, page, limit)


@router.get(
    "/{esma_id}",
    summary="Get Esma by ID",
    description="Retrieve an Esma by its ID with optional language filtering.",
    responses={404: not_found_response_annotation("Esma")},
)
def get_esma_by_id(
    esma_id: EsmaId,
    lg: LanguageQuery,
) -> EsmaSchema:
    result = esma_table.get(doc_id=esma_id)
    if not result:
        raise HTTPException(status_code=404, detail="Esma not found")

    if lg is None:
        return result

    return filter_esma_by_lang(result, lg)


@router.get(
    "/name/{esma_slug}",
    summary="Get Esma by name",
    description="Retrieve an Esma by its slug (latinized english name) with optional language filtering.",
    responses={404: not_found_response_annotation("Esma")},
)
def get_esma_by_name(
    esma_slug: EsmaSlug,
    lg: LanguageQuery,
) -> EsmaSchema:
    lower_esma_slug = esma_slug.lower()
    result = esma_table.get(dbQuery().slug == lower_esma_slug)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Esma not found",
        )

    if lg is None:
        return result

    return filter_esma_by_lang(result, lg)
