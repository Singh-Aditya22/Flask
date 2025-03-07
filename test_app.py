from app import app
import json
import pytest


@pytest.fixture
def client():
    return app.test_client()


def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '<p>Hello, World!</p>'

