"""
    Module for Account schemas
"""
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class AccountSchema(BaseModel):
    """
    Account Schema
    """

    number: int = Field(example="123456789")
    nickname: str = Field(example="Thomas")
    password: str = Field(example="e10adc3949ba59abbe56e057f20f883e")
    history: List = Field(example=[])
    balance: int = Field(example=123)
    creation_date: datetime = Field(example="2022-06-04 22:13:19.332981")


class AccountSchemaInDB(AccountSchema):
    """
    Account base schema in DB
    """

    id: str = Field(example="16f8ddc6-3697-4b90-a5c5-1b60e26de6dc")
