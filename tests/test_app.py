from fastapi import status
from fastapi.testclient import TestClient
from httpx import Response

from learning_fastapi.app import app

client = TestClient(app)


def test_hello_world_return_ok():
    response: Response = client.get('/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == 'Hello, World!'
