"""
    Module for TokenModel
"""

from mongoengine import Document, StringField, DateTimeField
from app.db import SafeDocumentMixin


class TokenModel(Document, SafeDocumentMixin):
    """
    Token model class
    """

    key = StringField(unique=True)
    creation_date = DateTimeField(required=True)

    meta = {"collection": "tokens", "indexes": ["key"]}

    def serialize(self) -> dict:
        return {
            "key": self.key,
            "creation_date": self.creation_date,
        }
