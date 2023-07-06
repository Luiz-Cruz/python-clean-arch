from faker import Faker
from sqlalchemy import text
from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository


faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()

def test_insert_user():
    """ Should Insert User """
    
    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine()

    new_user = user_repository.insert_user(name, password)
    with engine.connect() as conn:
        query_user = conn.execute(
            text(f"SELECT * FROM users WHERE id= '{new_user.id}';")
        ).fetchone()

       
        assert new_user.id == 10
        assert new_user.name == query_user.name
        assert new_user.password == query_user.password
