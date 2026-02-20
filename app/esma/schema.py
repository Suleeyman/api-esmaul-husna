from pydantic import BaseModel, Field, RootModel

from app.core.schemas import DynamicLangDict

# -------------------------
# Sous-objets dynamiques
# -------------------------


class ExplanationPartSchema(BaseModel):
    short: str | DynamicLangDict
    long: str | DynamicLangDict


class TransliterationSchema(BaseModel):
    iso: str
    popular: str | DynamicLangDict


class ImagePngSchema(BaseModel):
    d_64x64: str = Field(alias="64x64")
    d_128x128: str = Field(alias="128x128")
    d_256x256: str = Field(alias="256x256")


class ImageSchema(BaseModel):
    png: ImagePngSchema
    svg: str


class VerseSchema(RootModel[dict[int, list[int]]]):
    """Mapping of verse number to list of related verse numbers."""


# -------------------------
# Schéma principal
# -------------------------
class EsmaSchema(BaseModel):
    slug: str
    id: int
    ar: str
    ar_enhanced: str = Field(alias="ar-enhanced")

    name: str | DynamicLangDict
    explanation: ExplanationPartSchema
    transliteration: TransliterationSchema

    ipa: str
    audio: str
    image: ImageSchema

    verse: VerseSchema
