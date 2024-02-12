from sqlalchemy.exc import SQLAlchemyError
from app.models import db


def handle_db_operation(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as e:
            db.session.rollback()
            return {'error': str(e)}, 500  # Internal Server Error
        except Exception as e:
            return {'error': str(e)}, 500  # Internal Server Error
    return wrapper
