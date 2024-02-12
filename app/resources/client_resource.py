from flask import abort
from flask_restful import Resource, reqparse
from app.models import Client, db
from app.utils import handle_db_operation

client_parser = reqparse.RequestParser()
client_parser.add_argument('first_name', type=str, required=False)
client_parser.add_argument('last_name', type=str, required=False)
client_parser.add_argument('phone', type=str, required=False)


class ClientResource(Resource):
    @handle_db_operation
    def get(self):
        clients = Client.query.all()
        return [{
            'id': client.id,
            'first_name': client.first_name,
            'last_name': client.last_name,
            'phone': client.phone
        } for client in clients]

    @handle_db_operation
    def post(self):
        data = client_parser.parse_args()
        if not data.get('first_name'):
            return {'error': 'First name is required'}, 400
        if not data.get('last_name'):
            return {'error': 'Last name is required'}, 400
        client = Client(
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone=data.get('phone')
        )
        db.session.add(client)
        db.session.commit()
        return {'message': 'Client created successfully', 'id': client.id}


class ClientItemResource(Resource):
    @handle_db_operation
    def get(self, client_id):
        client = Client.query.get(client_id)
        if not client:
            abort(404, message=f"Client with ID {client_id} does not exist")
        return {
            'id': client.id,
            'first_name': client.first_name,
            'last_name': client.last_name,
            'phone': client.phone
        }

    @handle_db_operation
    def put(self, client_id):
        data = client_parser.parse_args()
        client = Client.query.get(client_id)
        if not client:
            abort(404, message=f"Client with ID {client_id} does not exist")

        for key, value in data.items():
            if value is not None:
                setattr(client, key, value)
        db.session.commit()
        return {'message': f'Client with ID {client_id} updated successfully'}

    @handle_db_operation
    def delete(self, client_id):
        client = Client.query.get(client_id)
        if not client:
            abort(404, message=f"Client with ID {client_id} does not exist")

        db.session.delete(client)
        db.session.commit()
        return {'message': f'Client with ID {client_id} deleted successfully'}
