# from contextlib import asynccontextmanager
# from fastapi import FastAPI, Depends, HTTPException

# from sqlmodel import Session, select
# from db import engine, create_db_and_table, get_session
# from models import Book

from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from logger import logger
from middleware import log_middleware
from db import create_db_and_table
# from OTUrl import main as oturl_main
from OTUrl.main import router as oturl_router


@asynccontextmanager
async def lifespan(app: FastAPI):
  create_db_and_table()
  yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)
# app.add_exception_handler
app.include_router(oturl_router)


@app.get('/')
async def index() -> dict:
  logger.info('Hello')
  return {'message': 'hi'}

# app.include_router(oturl_main.router)

# app = FastAPI()



# @app.post('/books')
# def create_book(book: Book):
#   with Session(engine) as session:
#     db_item = book
#     session.add(db_item)
#     session.commit()
#     session.refresh(db_item)
#     return db_item


# @app.get('/books', response_model=list[Book]) #output serialiser
# def read_books():
#   with Session(engine) as session:
#     books = session.exec(select(Book)).all()
#     return books

# @app.get('/books/{book_id}', response_model=Book) #output serialiser
# def read_book(book_id:int, session:Session = Depends(get_session)):
#   book = session.get(Book,book_id)
#   if not book:
#       raise HTTPException(status_code=404,detail="Book not found")
#   return book


# @app.patch('/books/{book_id}', response_model=Book) #output serialiser
# def update_book(book_id:int, book:Book, session:Session = Depends(get_session)):
#   book_fromdb = session.get(Book, book_id)
#   if not book:
#       raise HTTPException(status_code=404,detail="Book not found")
  
#   data = book.model_dump(exclude_unset=True) #partial update
#   for k, v in data.items():
#     setattr(book_fromdb, k, v)
#   session.add(book_fromdb)
#   session.commit()
#   session.refresh(book_fromdb)
#   return book_fromdb


# @app.delete('/books/{book_id}') #output serialiser
# def delete_book(book_id:int, session:Session = Depends(get_session)):
#   book = session.get(Book,book_id)
#   if not book:
#       raise HTTPException(status_code=404,detail="Book not found")
#   session.delete(book)
#   session.commit()
#   return {"deleted": True}


# In-memory storage for simplicity (replace with a real database)
# config = Configuration(
#     programs=[
#         Program(name="AOD", assessment_types=["InitialAssessment", "ReviewAssessment"]),
#         Program(name="MentalHealth", assessment_types=["Intake", "Progress"]),
#     ],
#     clients=[
#         Client(slk="ABC123", current_program="AOD"),
#         Client(slk="DEF456", current_program="MentalHealth"),
#     ],
# )

# @app.get("/programs/{program_name}")
# async def get_program_config(program_name: str):
#     for program in config.programs:
#         if program.name == program_name:
#             return program
#     return {"message": "Program not found"}, 404

# def get_program_by_name(program_name: str):
#     for program in config.programs:
#         if program.name == program_name:
#             return program
#     return None

# @app.get("/clients/{slk}/assessment_types")
# async def get_client_assessment_types(slk: str):
#     for client in config.clients:
#         if client.slk == slk:
#             program = get_program_by_name(client.current_program)
#             if program:
#                 return program.assessment_types
#     return {"message": "Client not found"}, 404

