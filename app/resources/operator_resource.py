from flask_restful import Resource, reqparse
from app.models import Operator, db
from app.utils import handle_db_operation

operator_parser = reqparse.RequestParser()
operator_parser.add_argument('first_name', type=str, required=True, help='First name is required')  # noqa
operator_parser.add_argument('last_name', type=str, required=True, help='Last name is required') # noqa


class OperatorResource(Resource):
    @handle_db_operation
    def get(self):
        operators = Operator.query.all()
        return [{
            'id': operator.id,
            'first_name': operator.first_name,
            'last_name': operator.last_name
        } for operator in operators]

    @handle_db_operation
    def post(self):
        data = operator_parser.parse_args()
        if not data.get('first_name'):
            return {'error': 'First name is required'}, 400
        if not data.get('last_name'):
            return {'error': 'Last name is required'}, 400
        operator = Operator(
            first_name=data['first_name'], last_name=data['last_name'])
        db.session.add(operator)
        db.session.commit()
        return {'message': 'Operator created successfully', 'id': operator.id}
