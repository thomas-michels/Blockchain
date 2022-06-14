"""
    Module for Block schemas
"""
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class BlockSchema(BaseModel):
    """
    Block Schema
    """
 
    data: List = Field()
    hash: str = Field()
    previous_hash: str = Field()
    timestamp: float = Field()
    nonce: int = Field()


class BlockSchemaInDB(BlockSchema):
    """
    Block schema in db class
    """
    block_id: str = Field(example="16f8ddc6-3697-4b90-a5c5-1b60e26de6dc")


class SimpleBlockSchema(BaseModel):
    """
    Class for SimpleBlockSchema
    """

    data: List = Field()
    nonce: int = Field()
