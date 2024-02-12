from flask_restful import Resource, reqparse
from app.models import Request, RequestStatus, db
from app.utils import handle_db_operation

request_parser = reqparse.RequestParser()
request_parser.add_argument('body', type=str, required=True, help='Body is required')   # noqa
request_parser.add_argument('status', type=str, default=RequestStatus.PENDING.value, help='Status is required') # noqa
request_parser.add_argument('processed_by', type=int)


class RequestResource(Resource):
    @handle_db_operation
    def get(self):
        requests = Request.query.all()
        return [{
            'id': request.id,
            'body': request.body,
            'status': request.status.value,
            'processed_by': request.processed_by
        } for request in requests]

    @handle_db_operation
    def post(self):
        data = request_parser.parse_args()
        if not data.get('body'):
            return {'error': 'Body is required'}, 400

        status = getattr(RequestStatus, data['status'], None)
        if status is None:
            return {'error': f'Invalid status: {data["status"]}'}, 400

        request = Request(
            body=data['body'],
            status=status,
            processed_by=data.get('processed_by')
        )
        db.session.add(request)
        db.session.commit()
        return {'message': 'Request created successfully', 'id': request.id}

    def delete(self):
        db.session.query(Request).delete()
        db.session.commit()
        return {'message': 'All requests deleted successfully'}


class RequestItemResource(Resource):
    @handle_db_operation
    def get(self, request_id):
        request = Request.query.get(request_id)
        if not request:
            return {'error': f'Request with ID {request_id} not found'}, 404

        return {
            'id': request.id,
            'body': request.body,
            'status': request.status.value,
            'processed_by': request.processed_by
        }
