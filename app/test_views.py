import pytest


def test_home_page(app, client):
    assert client.get("/users/500").status_code == 200


def test_user_signup(app, client, db):
    assert (
        client.post(
            "/users",
            data={"action": "signup", "username": "TestUser", "password": "TestPass"},
        ).status_code
        == 201
    )
