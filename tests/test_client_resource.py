from app import app
from app.models import Client, db


def test_get_all_clients(client):
    # Add test data
    client1 = Client(first_name="John", last_name="Doe", phone="123456789")
    client2 = Client(first_name="Jane", last_name="Doe", phone="987654321")

    with app.app_context():
        db.session.add_all([client1, client2])
        db.session.commit()

    # Make a GET request to fetch all clients
    response = client.get('/api/clients')

    assert response.status_code == 200

    data = response.json
    assert len(data) == 2


def test_create_client(client):
    # Make a POST request to create a client
    response = client.post(
        '/api/clients',
        json={
            "first_name": "Alice",
            "last_name": "Smith",
            "phone": "555555555"
        })

    assert response.status_code == 200

    data = response.json
    assert data['message'] == 'Client created successfully'

    # Assert client is added to the database
    with app.app_context():
        client = Client.query.filter_by(first_name="Alice").first()
        assert client is not None
