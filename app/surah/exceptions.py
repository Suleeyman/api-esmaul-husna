from app.exceptions import ResourceNotFoundError


class SurahNotFoundError(ResourceNotFoundError):
    """Exception raised when a Surah resource is not found."""

    def __init__(self, identifier=None):
        super().__init__("Surah", identifier)
