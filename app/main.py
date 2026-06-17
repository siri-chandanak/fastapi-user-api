from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Management REST API",
    description="FastAPI project with PostgreSQL, SQLAlchemy, JWT, CRUD, and Pagination",
    version="1.0.0"
)

app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "FastAPI User API is running"}