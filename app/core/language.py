from enum import Enum
from typing import Annotated

from fastapi import Depends, Query


class Lang(str, Enum):
    english = "en"
    french = "fr"
    turk = "tr"


def language_depends(
    lg: Annotated[
        Lang | None,
        Query(description="Output language (e.g., 'en', 'fr', 'tr')"),
    ] = None,
):
    return lg


LanguageQuery = Annotated[Lang, Depends(language_depends)]
