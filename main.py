# from uvicorn import run
from api import app
# from OTUrl import main as oturl_main



# run(app, host="0.0.0.0", port=8000)


# from fastapi import FastAPI, HTTPException
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# # Replace with your database connection details
# engine = create_engine("your_database_url")
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# from schemas import ProgramModel
# from program_schema import ProgramSchema

# app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/programs/{program_name}", response_model=ProgramModel)
# async def get_program(program_name: str, db: SessionLocal = Depends(get_db)):
#     program = db.query(Program).filter_by(name=program_name).first()
#     if not program:
#         raise HTTPException(status_code=404, detail="Program not found")

#     program_schema = ProgramSchema().load(program)
#     return program_schema

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
