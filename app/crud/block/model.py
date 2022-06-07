"""
    Block model
"""

from mongoengine import Document, StringField, IntField, FloatField, ListField
from app.db import SafeDocumentMixin


class BlockModel(Document, SafeDocumentMixin):
    """
    Block model class
    """

    id = StringField(required=True)
    data = ListField(required=True)
    hash = StringField(required=True)
    previous_hash = StringField(required=True)
    timestamp = FloatField(required=True)
    nonce = IntField(required=True)

    meta = {"collection": "blocks", "indexes": ["id"]}

    def serialize(self) -> dict:
        return {
            "id": self.id,
            "data": self.data,
            "hash": self.hash,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }
