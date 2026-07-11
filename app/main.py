from fastapi import FastAPI
from pydantic import BaseModel , EmailStr , AnyUrl, Field
from typing import List , Optional , Annotated

app=FastAPI()

class Candidate(BaseModel):
      
      name: Annotated [str, Field(max_length=100, title="Name of the Candidate", description="Enter your Full Name")]

      age: Annotated [int, Field(gt=0,title="Age of the Candidate", description="Enter your Age")]

      email: Annotated [EmailStr,Field(title="Email of the Candidate", description="Enter your valid Email")]

      Linkedin_url: Annotated [AnyUrl, Field(title="Linkedin of the Candidate", description="Enter your Linkedin url")]
      
      skills: List[str] | None = None
      experience: int
      

@app.get("/")
def hello():
  return {"message":"Welcome to Career Graph"}

@app.get("/health")
def health_check():
    return {"status":"Server is running in Okay condition"}

@app.post("/candidates/")
async def candidate_creation(candidates:Candidate):
    return candidates
