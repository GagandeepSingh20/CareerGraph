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


class CandidateCreate(BaseModel):
    name: Annotated[
        str,
        Field(
            min_length=2,
            max_length=100,
            title="Name of the Candidate",
            description="Enter your full name",
        ),
    ]

    age: Annotated[
        int,
        Field(
            ge=18,
            le=100,
            title="Age of the Candidate",
            description="Enter your age",
        ),
    ]

    cgpa: Annotated[
        float,
        Field(
            ge=0.0,
            le=10.0,
            title="CGPA of the Candidate",
            description="Enter your CGPA",
        ),
    ]

    gender: Annotated[
        Literal["Male", "Female", "Others"],
        Field(description="Enter your gender"),
    ]

    email: Annotated[
        EmailStr,
        Field(
            title="Email of the Candidate",
            description="Enter your valid email",
        ),
    ]

    linkedin_url: Annotated[
        AnyUrl | None,
        Field(
            title="LinkedIn profile of the Candidate",
            description="Enter your LinkedIn profile URL",
        ),
    ] = None

    skills: list[str] | None = None

    experience: Annotated[
        int,
        Field(
            ge=0,
            title="Experience of the Candidate",
            description="Enter experience in years",
        ),
    ]

    graduation_year: Annotated[
        int,
        Field(
            ge=1950,
            le=2050,
            title="Graduation Year of the Candidate",
            description="Enter your graduation year",
        ),
    ]
    
    # Field Validators

    @field_validator('name')
    @classmethod
    def normalize_name(cls,value: str) -> str:
        return value.strip().title()
    
    
    @field_validator('linkedin_url')
    @classmethod
    def validate_linkedin_url(cls, value: AnyUrl | None) -> AnyUrl | None:
        if value is None:
            return None
        host = (value.host or "").lower()

        if host != "linkedin.com" and not host.endswith(".linkedin.com"):
            raise ValueError("URL must belong to linkedin.com")
        
        return value
    
    
    @field_validator('skills')
    @classmethod
    def normalize_skills(cls,value: list[str] | None,) ->list[str] | None:
        if value is None:
            return None
        
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

        return cleaned_skills or None
    
class CandidateResponse(CandidateCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)