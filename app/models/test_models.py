import pytest
from models.models import Word, User


def test_create_user(db):
    user = User.create("test", "password")
    assert user.name == "test"
    assert User.exists("test")

    with pytest.raises(User.UserExistsError) as excinfo:
        user = User.create("test", "password")
        assert "test" in str(excinfo)


def test_login_user(db):
    assert User.login("test", "password")
    with pytest.raises(User.IncorrectLoginError) as excinfo:
        user = User.login("test", "wrong")
        assert "test" in str(excinfo)
