import os
import pytest
import fakeredis
from flask import Flask
from models.models import db as _db
from models import setup
from game import services
from factory import create_app


TESTDB = "test_db.db"
TESTDB_PATH = "{}".format(TESTDB)
TEST_DATABASE_URI = "sqlite:///" + TESTDB_PATH


@pytest.fixture(scope="session")
def app(request):
    """Session-wide test `Flask` application."""
    app = create_app(db_path=TEST_DATABASE_URI)

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope="session")
def db(app, request):
    """Session-wide test database."""
    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)

    def teardown():
        _db.drop_all()
        os.unlink(TESTDB_PATH)

    _db.app = app
    _db.create_all()
    setup.setup_db()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope="function")
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


@pytest.fixture(scope="session")
def client(app):
    client = app.test_client()
    return client


@pytest.fixture(scope="session")
def redis():
    r = fakeredis.FakeStrictRedis()
    services.r = r
    return r


@pytest.fixture(scope="session")
def sample_game_id(redis):
    services.r = redis
    services.create_game("0000")
    return "0000"