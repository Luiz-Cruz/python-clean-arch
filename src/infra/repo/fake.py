from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakerRepo:
    """A simple Repository"""

    @classmethod
    def insert_user(cls):
        """Some method to insert user"""
        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Luizera", password="Fallen")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except Exception:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
