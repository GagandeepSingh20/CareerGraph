from typing import Annotated, Literal
from datetime import datetime

from pydantic import (
    AnyUrl,
    EmailStr,
    BaseModel,
    field_validator,
    Field,
    ConfigDict,
)


class JobCreate(BaseModel):

    title: Annotated[
        str,
        Field(
            min_length=2,
            max_length=100,
            title="Title of the Job",
            description="Enter Title of the Job",
        ),
    ]

    company: Annotated[
        str,
        Field(
            min_length=2,
            max_length=200,
            title="Name of the Company",
            description="Enter Name of the Company",
        ),
    ]

    required_skills: Annotated[
        list[str],
        Field(
            title="Skills required for the Job",
            description="Enter Skills required for the Job",
        ),
    ]

    min_experience: Annotated[
        int,
        Field(
            ge=0,
            title="Experience required for the Job",
            description="Enter minimum experience required in years",
        ),
    ]

    location: Annotated[
        str,
        Field(
            min_length=1,
            max_length=200,
            title="Location of the Job",
            description="Enter Location of the Job",
        ),
    ]

    job_type: Annotated[
        Literal["Internship","Apprenticeship","Full-Time","Part-Time"],
        Field(
            description="Enter Type of the Job",
        ),
    ]

    # Field Validators

    @field_validator('title')
    @classmethod
    def normalize_title(cls,value: str) -> str:
        return value.strip().title()

    @field_validator('company')
    @classmethod
    def normalize_company_name(cls,value: str) -> str:
        return value.strip()
    
    @field_validator('required_skills')
    @classmethod
    def normalize_skills(cls, value: list[str]) ->list[str]:
        
        cleaned_skills: list[str] = []
        seen_skills: set[str] = set()

        for skill in value:
    
            cleaned_skill = skill.strip()

            if not cleaned_skill:
                continue

            comparison_value = cleaned_skill.casefold()

            if comparison_value not in seen_skills:
                seen_skills.add(comparison_value)
                cleaned_skills.append(cleaned_skill)
        if not cleaned_skills:
            raise ValueError("Required Skills Cannot Be Empty")

        return cleaned_skills
    
class JobResponse(JobCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)