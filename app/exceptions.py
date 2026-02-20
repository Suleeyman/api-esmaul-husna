from fastapi import HTTPException, status


class ResourceNotFoundError(HTTPException):
    """Base exception for resources that cannot be found."""

    def __init__(self, resource_name: str, identifier=None):
        self.resource_name = resource_name
        self.identifier = identifier
        message = f"{resource_name} not found"
        if identifier is not None:
            message = f"{resource_name} identified by '{identifier}' not found"
        super().__init__(status.HTTP_404_NOT_FOUND, message)
