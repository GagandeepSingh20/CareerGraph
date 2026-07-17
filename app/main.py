from fastapi import FastAPI

from .database import Base, engine
from .routers import candidates, jobs


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="CareerGraph API",
    description="Candidate and job matching backend",
)


app.include_router(candidates.router)
app.include_router(jobs.router)


@app.get("/")
def welcome():
    return {"message": "Welcome to Career Graph"}


@app.get("/health")
def health_check():
    return {"status": "Server is running in okay condition"}