from fastapi import FastAPI
from app.api.v1.endpoints import example

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}

app.include_router(example.router, prefix="/api/v1/example", tags=["example"])