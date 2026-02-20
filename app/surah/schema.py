from pydantic import BaseModel, Field

from app.core.schemas import DynamicLangDict


class SurahSchema(BaseModel):
    number: int
    verses: int
    esma_ids: list[int]
    ar: str
    ar_enhanced: str = Field(alias="ar-enhanced")
    name: str | DynamicLangDict
