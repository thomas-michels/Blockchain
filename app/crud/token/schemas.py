"""
    Module NT token schemas
"""
from datetime import datetime
from pydantic import BaseModel, Field


class NTTokenSchema(BaseModel):
    """
    NT token Schema
    """

    key: str = Field(example="16f8ddc6-3697-4b90-a5c5-1b60e26de6dc")
    creation_date: datetime = Field(example="2022-06-04 22:13:19.332981")


class TokensCallbackSchema(BaseModel):

    account_number: int = Field(example=123123)
    quantity: int = Field(example=100)
