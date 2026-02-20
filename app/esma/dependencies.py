from typing import Annotated

from fastapi import Depends, Path


def esma_id_depends(
    esma_id: Annotated[int, Path(ge=1, le=99, description="ID of Esma")],
):
    return esma_id


def esma_slug_depends(
    esma_slug: Annotated[
        str,
        Path(max_length=50, description="Latinized english Esma name"),
    ],
):
    return esma_slug


EsmaId = Annotated[int, Depends(esma_id_depends)]
EsmaSlug = Annotated[str, Depends(esma_slug_depends)]
