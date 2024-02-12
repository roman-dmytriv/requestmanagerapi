from flask import Flask, send_from_directory, request, g
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint


# Initialize SQLAlchemy
db = SQLAlchemy()

# Create Flask app
app = Flask(__name__)
app.config.from_pyfile('config.py')


# Gather request data before each request
@app.before_request
def gather_request_data():
    g.method = request.method
    g.url = request.url
    g.operator_id = request.headers.get('Operator-ID')


# Initialize the database
def init_db():
    with app.app_context():
        db.init_app(app)
        db.create_all()


# Create API instance with prefix
api = Api(app, prefix='/api')

from app.resources import (
    client_resource,
    request_resource,
    operator_resource,
    request_status_resource
)

api.add_resource(client_resource.ClientResource, '/clients')
api.add_resource(client_resource.ClientItemResource, '/clients/<int:client_id>')    # noqa
api.add_resource(request_resource.RequestResource, '/requests')
api.add_resource(request_resource.RequestItemResource, '/requests/<int:request_id>')    # noqa
api.add_resource(request_status_resource.RequestStatusResource, '/requests/<int:request_id>/status')    # noqa
api.add_resource(operator_resource.OperatorResource, '/operators')


# Serve API specification
@app.route('/api/spec.json')
def serve_spec():
    return send_from_directory('.', 'spec.json')


# Configure Swagger UI
SWAGGER_URL = '/api/docs'
API_URL = '/api/spec.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API Documentation"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
