from typing import List

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    field_validator,
)


class Person(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Full name of the person"
    )

    age: int = Field(
        ...,
        ge=1,
        le=120,
        description="Age must be between 1 and 100"
    )

    email: EmailStr

    skills: List[str] = Field(
        ...,
        min_length=1,
        description="List of skills"
    )

    # -----------------------------
    # Name Validation
    # -----------------------------
    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str):

        value = value.strip()

        if not value.replace(" ", "").isalpha():
            raise ValueError(
                "Name should contain only alphabets and spaces."
            )

        return value.title()

    # -----------------------------
    # Email Validation
    # -----------------------------
    @field_validator("email")
    @classmethod
    def validate_email(cls, value: EmailStr):

        email = str(value).lower()

        blocked_domains = [
            "spam.com",
            "fake.com",
            "tempmail.com"
        ]

        domain = email.split("@")[1]

        if domain in blocked_domains:
            raise ValueError(
                "Temporary or blocked email domains are not allowed."
            )

        return email

    # -----------------------------
    # Skills Validation
    # -----------------------------
    @field_validator("skills")
    @classmethod
    def validate_skills(cls, value: List[str]):

        cleaned = []

        for skill in value:

            skill = skill.strip()

            if len(skill) < 2:
                raise ValueError(
                    "Skill names are too short."
                )

            cleaned.append(skill.title())

        return cleaned