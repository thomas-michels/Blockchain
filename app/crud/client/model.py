"""
    Client model
"""

from mongoengine import Document, StringField, BooleanField, DateTimeField
from app.db import SafeDocumentMixin


class ClientModel(Document, SafeDocumentMixin):
    """
    Client model class
    """

    client_id = StringField(unique=True)
    name = StringField(required=True)
    connection_date = DateTimeField(required=True)
    active = BooleanField(required=True)

    meta = {"collection": "clients", "indexes": ["client_id"]}

    def serialize(self) -> dict:
        return {
            "client_id": self.client_id,
            "name": self.name,
            "connection_date": self.connection_date,
            "active": self.active,
        }
