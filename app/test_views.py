import pytest


def test_home_page(app, client):
    assert client.get("/users/500").status_code == 200


def test_user_signup(app, client, db):
    assert (
        client.post(
            "/users",
            json={"action": "signup", "username": "TestUser", "password": "TestPass"},
        ).status_code
        == 201
    )

    assert (
        client.post(
            "/users",
            json={"action": "signup", "username": "TestUser", "password": "TestPass"},
        ).status_code
        == 400
    )


def test_user_login(app, client, db):
    assert (
        client.post(
            "/users",
            json={"action": "login", "username": "TestUser", "password": "TestPass"},
        ).status_code
        == 200
    )

    assert (
        client.post(
            "/users",
            json={"action": "login", "username": "TestUser", "password": "WrongPass"},
        ).status_code
        == 401
    )
