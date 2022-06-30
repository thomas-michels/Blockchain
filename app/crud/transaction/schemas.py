"""
    Module for transaction schemas
"""
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field
from app.crud.token import NTTokenSchema


class SimpleTransactionSchema(BaseModel):
    """
    SimpleTransactionSchema
    """

    sender_number: int = Field(example="123123")
    receiver_number: int = Field(example="123123")
    quantity: int = Field(example=123)


class MiddleTransactionSchema(SimpleTransactionSchema):
    """
    Base Account Schema
    """

    balance: List[str] = Field(example=[])


class TransactionSchema(MiddleTransactionSchema):
    """
    Base Account Schema
    """

    creation_date: datetime = Field(example="2022-06-04 22:13:19.332981")


class TransactionSchemaInDB(TransactionSchema):
    """
    TransactionSchemaInDB class
    """

    transaction_id: str = Field(example="16f8ddc6-3697-4b90-a5c5-1b60e26de6dc")
