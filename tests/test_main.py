from http import HTTPStatus

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main() -> None:
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "message": "API Esmaul Husna",
        "link": "https://github.com/Suleeyman/api-esmaul-husna",
    }
