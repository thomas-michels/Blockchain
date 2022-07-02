
from pydantic import BaseModel, Field


class LoginSchema(BaseModel):
    """
    LoginSchema Schema
    """

    number: int = Field(example=123123)
    password: str = Field(example="Thomas")
