"""
    Module for client schemas
"""

from datetime import datetime
from pydantic import BaseModel, Field

class SimpleClientSchema(BaseModel):
    """
    SimpleClientSchema class
    """
    client_id: str = Field(example="16f8ddc6-3697-4b90-a5c5-1b60e26de6dc")
    name: str = Field(example="Penny Adams")


class ClientSchema(SimpleClientSchema):
    """
    ClientSchema class
    """
    connection_date: datetime = Field(example="2022-06-04 22:13:19.332981")
    active: bool = Field(example=True)
