import math
from typing import Annotated, TypeVar

from fastapi import Depends, HTTPException, Query
from pydantic import BaseModel

T = TypeVar("T")  # type de chaque élément dans la page


class PaginatedResponse[T](BaseModel):
    page: int | None
    limit: int | None
    total: int
    total_pages: int
    has_next: bool
    has_previous: bool
    data: list[T]


def paginate[T](
    data: list[T],
    page: int | None,
    limit: int | None,
) -> PaginatedResponse[T]:
    total = len(data)

    # Pas de pagination
    if page is None and limit is None:
        return {
            "page": None,
            "limit": None,
            "total": total,
            "total_pages": 1,
            "has_next": False,
            "has_previous": False,
            "data": data,
        }

    # Règle métier
    if page is not None and limit is None:
        raise HTTPException(
            status_code=400,
            detail="limit query parameter is required when page is provided",
        )

    if page is None and limit is not None:
        page = 1

    if page < 1 or limit < 1:
        raise HTTPException(
            status_code=400,
            detail="page and limit must be greater than 0",
        )

    total_pages = math.ceil(total / limit)

    if page > total_pages and total_pages != 0:
        raise HTTPException(
            status_code=404,
            detail="Page not found",
        )

    start = (page - 1) * limit
    end = start + limit

    paginated_data = data[start:end]

    return PaginatedResponse(
        page=page,
        limit=limit,
        total=total,
        total_pages=total_pages,
        has_next=page < total_pages,
        has_previous=page > 1,
        data=paginated_data,
    )


def pagination_depends(
    page: Annotated[
        int | None,
        Query(ge=1, description="Page number for pagination"),
    ] = None,
    limit: Annotated[
        int | None,
        Query(le=99, ge=1, description="Number of items per page"),
    ] = None,
):
    return {"page": page, "limit": limit}


PaginationQueries = Annotated[dict, Depends(pagination_depends)]
