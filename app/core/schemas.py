from pydantic import AnyUrl, BaseModel, RootModel

from app.core.language import Lang


class DynamicLangDict(RootModel[dict[Lang, str]]):
    """Mapping of ISO language code to a value."""


class Root(BaseModel):
    title: str
    github_url: AnyUrl
    swagger: str
    redocly: str


class ErrorResponse(BaseModel):
    code: int
    message: str
    details: dict[str, str] | None = None
