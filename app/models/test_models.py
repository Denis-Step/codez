import pytest
from models.models import Word, User


def test_create_user(db):
    user = User.create("test", "password")
    assert user.name == "test"
    assert User.exists("test")


def test_login_user(db):
    assert User.login("test", "password")
