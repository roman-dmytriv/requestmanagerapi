from app import db
from enum import Enum
from sqlalchemy import Enum as EnumField


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20))


class RequestStatus(Enum):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    REJECTED = 'REJECTED'


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    status = db.Column(EnumField(RequestStatus), default=RequestStatus.PENDING)
    processed_by = db.Column(db.Integer, db.ForeignKey('operator.id'))


class Operator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
