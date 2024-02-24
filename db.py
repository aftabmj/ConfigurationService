
from sqlmodel import create_engine, SQLModel, Session

sqlite_url = 'sqlite:///urls.db'

# sqlite_url = 'sqlite:///books.db'
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def get_session():
  with Session(engine) as session:
    yield session

def create_db_and_table():
  SQLModel.metadata.create_all(engine)
