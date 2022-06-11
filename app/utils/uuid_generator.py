"""
    Module for uuid generator
"""
from uuid import uuid4


def generate_uuid() -> str:
    """
    Function to return uuid

    :return: str
    """
    return str(uuid4())
