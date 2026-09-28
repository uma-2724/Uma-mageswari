from typing import Any

from pydantic import (
    BaseModel,
    Field,
    field_validator
)


class TaskRequest(BaseModel):

    text: str = Field(
        ...,
        min_length=1,
        max_length=12000
    )

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:

        value = value.strip()

        if not value:
            raise ValueError(
                "Input cannot be empty."
            )

        return value


class APIResponse(BaseModel):

    success: bool

    result: Any