"""
    Module for Account schemas
"""
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class SimpleAccountSchema(BaseModel):
    """
    Base Account Schema
    """

    nickname: str = Field(example="Thomas")
    password: str = Field(example="e10adc3949ba59abbe56e057f20f883e")


class AccountSchema(SimpleAccountSchema):
    """
    Account Schema
    """

    number: int = Field(example="123456")
    history: List = Field(example=[])
    balance: List = Field(example=[])
    active: bool = Field(default=True)
    creation_date: datetime = Field(example="2022-06-04 22:13:19.332981")


class AccountSchemaInDB(AccountSchema):
    """
    Account base schema in DB
    """

    account_id: str = Field(example="16f8ddc6-3697-4b90-a5c5-1b60e26de6dc")


class StandardAccountSchema(BaseModel):
    """
    Account Schema
    """

    number: int = Field(example="123456")
    history: List = Field(example=[])
    balance: List = Field(example=[])
    active: bool = Field(default=True)
    creation_date: datetime = Field(example="2022-06-04 22:13:19.332981")
