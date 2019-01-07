import pytest
from index import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_add(client):
    rv = client.get('/add?num1=2&num2=2')
    assert b'4' in rv.data
