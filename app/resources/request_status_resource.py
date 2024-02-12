from flask import g
from flask_restful import Resource, reqparse
from app.models import Request, RequestStatus, Operator, db
from app.utils import handle_db_operation


class RequestStatusResource(Resource):
    @handle_db_operation
    def put(self, request_id):
        # Parse the request data
        parser = reqparse.RequestParser()
        parser.add_argument('status', type=str, required=True)
        data = parser.parse_args()

        # Update the status of the request
        new_status = data['status']
        if new_status not in RequestStatus.__members__:
            return {'error': f'Invalid status: {new_status}'}, 400

        # Check if the user making the request is an operator
        # print(g.operator_id)
        if 'operator_id' not in g:
            return {'error': 'Unauthorized access'}, 403

        # Get the operator making the request
        operator = Operator.query.get(g.operator_id)
        if not operator:
            return {'error': 'Operator not found'}, 404

        # Get the request to update
        _request = Request.query.get(request_id)
        if not _request:
            return {'error': 'Request not found'}, 404

        # Ensure the operator is authorized to update the status
        if _request.processed_by != operator.id:
            return {'error': 'Unauthorized access'}, 403

        _request.status = RequestStatus[new_status]
        db.session.commit()

        return {'message': 'Request status updated successfully'}
