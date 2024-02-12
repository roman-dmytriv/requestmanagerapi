from app import app
from app.models import Operator, db


def test_get_all_operators(client):
    # Add test data
    operator1 = Operator(first_name="John", last_name="Doe")
    operator2 = Operator(first_name="Jane", last_name="Doe")
    db.session.add_all([operator1, operator2])
    db.session.commit()

    # Make a GET request to fetch all operators
    response = client.get('/api/operators')

    assert response.status_code == 200

    data = response.json
    assert len(data) == 2


def test_create_operator(client):
    # Make a POST request to create an operator
    response = client.post(
        '/api/operators', json={"first_name": "Alice", "last_name": "Smith"})
    print(response.json)

    # Assert response status code
    assert response.status_code == 200

    # Assert response data
    data = response.json
    assert data['message'] == 'Operator created successfully'

    # Assert operator is added to the database
    with app.app_context():
        operator = Operator.query.filter_by(first_name="Alice").first()
        assert operator is not None

# Write similar tests for other methods (PUT, DELETE)
