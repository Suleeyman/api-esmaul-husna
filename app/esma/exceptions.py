from app.exceptions import ResourceNotFoundError


class EsmaNotFoundError(ResourceNotFoundError):
    """Exception raised when an Esma resource is not found."""

    def __init__(self, identifier=None):
        super().__init__("Esma", identifier)
