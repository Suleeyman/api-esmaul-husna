from app.core.schemas import ErrorResponse


def not_found_response_annotation(resource: str):
    return {
        "model": ErrorResponse,
        "description": f"{resource} not found",
    }
