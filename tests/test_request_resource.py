from app import app
from app.models import Request, RequestStatus, db


def test_get_all_requests(client):
    # Add test data
    request1 = Request(body="Test request 1", status=RequestStatus.PENDING)
    request2 = Request(body="Test request 2", status=RequestStatus.COMPLETED)

    with app.app_context():
        db.session.add_all([request1, request2])
        db.session.commit()

    # Make a GET request to fetch all requests
    response = client.get('/api/requests')

    # Assert response status code
    assert response.status_code == 200

    # Assert response data
    data = response.json
    assert len(data) == 2


def test_create_request(client):
    # Make a POST request to create a request
    response = client.post(
        '/api/requests', json={"body": "Test request", "status": "PENDING"})

    print(response.data)

    # Assert response status code
    assert response.status_code == 200

    # Assert response data
    data = response.json
    assert data['message'] == 'Request created successfully'

    # Assert request is added to the database
    with app.app_context():
        request = Request.query.filter_by(body="Test request").first()
        assert request is not None

# Write similar tests for other methods (PUT, DELETE)
