from fastapi import FastAPI
from pydantic import BaseModel , EmailStr , AnyUrl, Field, field_validator
from typing import List , Optional , Annotated, Literal

app=FastAPI()

class Candidate(BaseModel):
      
      name: Annotated [str, Field(...,max_length=100, title="Name of the Candidate", description="Enter your Full Name")]

      age: Annotated [int, Field(..., title="Age of the Candidate", description="Enter your Age")]

      cgpa: Annotated [float, Field(..., title="CGPA of the Candidate", description="Enter your CGPA")]

      gender: Annotated[Literal['Male','Female','Others'], Field(...,description="Enter your Gender")]

      email: Annotated [EmailStr,Field(..., title="Email of the Candidate", description="Enter your valid Email")]

      Linkedin_url: Annotated [AnyUrl, Field(..., title="Linkedin of the Candidate", description="Enter your Linkedin url")]
      
      skills: List[str] | None = None

      experience: Annotated [int, Field(..., gt=-1,title="Experience of the Candidate", description="Enter your Experience")]

      graduation_year: Annotated[int, Field(..., gt=2000, lt=2050, title="Graduation Year of the Candidate", description="Enter your Graduation Year")]

      @field_validator('email', mode='after')
      @classmethod
      def email_validator(cls, value):
          if value in candidate_data.db:
              raise ValueError('Email already registered')
          return value
      
      @field_validator('age', mode='after')
      @classmethod
      def age_validator(cls, value):
          if 18<=value :
            return value
          else : raise ValueError('Invalid Age; Should be greater than or equal to 18')

      @field_validator('name', mode='after')
      @classmethod
      def tranform_name(cls, value):
          return value.lower()
      
      @field_validator('cgpa', mode='after')
      @classmethod
      def cgpa_validator(cls, value):
          if 0.0<=value<=10.0 :
            return value
          else : raise ValueError('Invalid CGPA; Should be  in the range of 0 to 10')


@app.get("/")
def welcome():
  return {"message":"Welcome to Career Graph"}

@app.get("/health")
def health_check():
    return {"status":"Server is running in Okay condition"}

@app.post("/candidates/")
async def candidate_creation(candidates:Candidate):
    