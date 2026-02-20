from typing import Annotated

from fastapi import Depends, Path


def surah_number_depends(
    number: Annotated[
        int,
        Path(ge=1, le=114, description="Surah number as it appears in the Qur'an"),
    ],
):
    return number


SurahNumber = Annotated[int, Depends(surah_number_depends)]
