import pytest
from models.models import Word, User


def test_create_user(db):
    user = User.create("test", "dummy")
    assert user.name == "test"
