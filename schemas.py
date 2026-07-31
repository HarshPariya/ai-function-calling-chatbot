from pydantic import BaseModel, EmailStr
from typing import List


class Person(BaseModel):
    name: str
    age: int
    email: EmailStr
    skills: List[str]