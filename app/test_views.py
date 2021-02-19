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


def test_get_game(app, client, redis, sample_game_id):
    response = client.get("/games/0000")
    assert response.status_code == 200
    assert response.mimetype == "application/json"


def test_create_game(app, client, redis):
    response = client.post("/games", json={"ID": "0001"})
    assert response.status_code == 201
    assert response.mimetype == "application/json"


def test_submit_turn(app, client, redis):
    data = {
        "action": "spymaster",
        "team": "blue",
        "payload": {"hint": "TestHint", "attempts": 3},
    }
    response = client.post("/games/0001", json=data)
    assert response.status_code == 201

    update = client.get("/games/0000")
    data = update.get_json()
