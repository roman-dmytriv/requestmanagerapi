from flask import g
from app import app
from app.models import Request, RequestStatus, Operator, db


def test_update_request_status(client):
    # Add test data
    operator = Operator(first_name="John", last_name="Doe")
    db.session.add(operator)
    db.session.commit()
    _request = Request(body="Test request", processed_by=operator.id)
    db.session.add(_request)
    db.session.commit()

    g.operator_id = operator.id

    # Make a PUT request to update the request status
    response = client.put(
        f'/api/requests/{_request.id}/status',
        json={"status": "REJECTED"}, headers={"Operator-ID": str(operator.id)})

    print(response.data)
    assert response.status_code == 200

    data = response.json
    assert data['message'] == 'Request status updated successfully'

    # Assert request status is updated in the database
    with app.app_context():
        updated_request = Request.query.order_by(Request.id.desc()).first()
        assert updated_request.status == RequestStatus.REJECTED


# Test to check if updating status of non-existing operator is handled
def test_put_request_status_request_not_found(client):
    response = client.put(
        '/api/requests/999/status', json={"status": "COMPLETED"})
    assert response.status_code == 404
    assert response.json == {"error": "Operator not found"}


# Test to check if updating status with invalid status is handled
def test_put_request_status_invalid_status(client):
    operator = Operator(first_name="John", last_name="Doe")
    db.session.add(operator)
    db.session.commit()
    _request = Request(body="Test request", processed_by=operator.id)
    db.session.add(_request)
    db.session.commit()
    response = client.put(
        '/api/requests/1/status', json={"status": "INVALID_STATUS"})
    assert response.status_code == 400
    assert response.json == {"error": "Invalid status: INVALID_STATUS"}
