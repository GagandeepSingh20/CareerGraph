from datetime import datetime
from typing import Annotated, Literal

from pydantic import (
    AnyUrl,
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    field_validator,
)


UserRole = Literal["CANDIDATE", "RECRUITER", "ADMIN"]


class CandidateSignup(BaseModel):
    email: Annotated[
        EmailStr,
        Field(
            title="Candidate Email",
            description="Enter candidate email address",
        ),
    ]

    password: Annotated[
        str,
        Field(
            min_length=8,
            max_length=128,
            title="Password",
            description="Enter password with at least 8 characters",
        ),
    ]

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
        Field(
            description="Enter your gender",
        ),
    ]

    linkedin_url: Annotated[
        AnyUrl | None,
        Field(
            title="LinkedIn profile of the Candidate",
            description="Enter your LinkedIn profile URL",
        ),
    ] = None

    skills: Annotated[
        list[str],
        Field(
            title="Candidate Skills",
            description="Enter candidate skills",
        ),
    ]

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

    @field_validator("name")
    @classmethod
    def normalize_name(cls, value: str) -> str:
        return value.strip().title()

    @field_validator("linkedin_url")
    @classmethod
    def validate_linkedin_url(cls, value: AnyUrl | None) -> AnyUrl | None:
        if value is None:
            return None

        host = (value.host or "").lower()

        if host != "linkedin.com" and not host.endswith(".linkedin.com"):
            raise ValueError("URL must belong to linkedin.com")

        return value

    @field_validator("skills")
    @classmethod
    def normalize_skills(cls, value: list[str]) -> list[str]:
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
            raise ValueError("Skills cannot be empty")

        return cleaned_skills


class RecruiterSignup(BaseModel):
    email: Annotated[
        EmailStr,
        Field(
            title="Recruiter Email",
            description="Enter recruiter email address",
        ),
    ]

    password: Annotated[
        str,
        Field(
            min_length=8,
            max_length=128,
            title="Password",
            description="Enter password with at least 8 characters",
        ),
    ]

    full_name: Annotated[
        str,
        Field(
            min_length=2,
            max_length=100,
            title="Recruiter Full Name",
            description="Enter recruiter full name",
        ),
    ]

    organization_name: Annotated[
        str,
        Field(
            min_length=2,
            max_length=150,
            title="Organization Name",
            description="Enter organization name",
        ),
    ]

    designation: Annotated[
        str,
        Field(
            min_length=2,
            max_length=100,
            title="Designation",
            description="Enter recruiter designation",
        ),
    ]

    organization_website: Annotated[
        AnyUrl | None,
        Field(
            title="Organization Website",
            description="Enter organization website URL",
        ),
    ] = None

    organization_location: Annotated[
        str,
        Field(
            min_length=1,
            max_length=200,
            title="Organization Location",
            description="Enter organization location",
        ),
    ]

    @field_validator("full_name")
    @classmethod
    def normalize_full_name(cls, value: str) -> str:
        return value.strip().title()

    @field_validator("organization_name")
    @classmethod
    def normalize_organization_name(cls, value: str) -> str:
        return value.strip()

    @field_validator("designation")
    @classmethod
    def normalize_designation(cls, value: str) -> str:
        return value.strip().title()

    @field_validator("organization_location")
    @classmethod
    def normalize_organization_location(cls, value: str) -> str:
        return value.strip()


class LoginRequest(BaseModel):
    email: Annotated[
        EmailStr,
        Field(
            title="Email",
            description="Enter your registered email address",
        ),
    ]

    password: Annotated[
        str,
        Field(
            min_length=8,
            max_length=128,
            title="Password",
            description="Enter your password",
        ),
    ]


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: UserRole


class CurrentUserResponse(BaseModel):
    id: int
    email: EmailStr
    role: UserRole
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)