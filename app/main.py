from fastapi import FastAPI

from app.database import Base, engine
from app.models.candidate_model import CandidateDB
from app.models.job_model import JobDB
from app.models.recruiter_model import RecruiterProfileDB
from app.models.user_model import UserDB
from app.routers import candidates, jobs


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