import os
import pytest
from flask import Flask
from models.models import db as _db

TESTDB = "test_project.db"
TESTDB_PATH = "/opt/project/data/{}".format(TESTDB)
TEST_DATABASE_URI = "sqlite:///" + TESTDB_PATH


@pytest.fixture(scope="session")
def db(request):
    """Session-wide test database."""
    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)

    def teardown():
        _db.drop_all()
        os.unlink(TESTDB_PATH)

    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope="session")
def app(db):
    """
    Create a Flask app context for the tests.
    """
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DB_CONN

    return app


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