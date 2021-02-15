import pytest


def test_home_page(app, client):
    print(app.url_map)
    assert client.get("/hello").status_code == 200
