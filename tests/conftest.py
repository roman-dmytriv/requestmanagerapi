import pytest
from flask import g
from app import app
from app.models import db


@app.context_processor
def inject_operator_id():
    return {'operator_id': None}  # Default to None


@pytest.fixture(scope='session')
def client():
    # Initialize the database
    with app.app_context():
        db.init_app(app)
        db.create_all()

    # Create a test client using the application context
    with app.test_client() as test_client:
        yield test_client

    # Clean up the database session and drop all tables
    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def mock_operator_id(monkeypatch):
    # Mock the 'operator_id' in g
    # Set operator_id to 1 for testing purposes
    monkeypatch.setattr(g, 'operator_id', 1)
