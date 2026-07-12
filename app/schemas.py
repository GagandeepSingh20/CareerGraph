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
