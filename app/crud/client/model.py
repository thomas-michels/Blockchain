"""
    Client model
"""

from mongoengine import Document, StringField, BooleanField, DateTimeField, IntField
from app.db import SafeDocumentMixin


class ClientModel(Document, SafeDocumentMixin):
    """
    Client model class
    """

    client_id = StringField(unique=True)
    name = StringField(required=True)
    account_number = IntField(required=True)
    connection_date = DateTimeField(required=True)
    active = BooleanField(required=True)

    meta = {"collection": "clients", "indexes": ["client_id"]}

    def serialize(self) -> dict:
        return {
            "client_id": self.client_id,
            "account_number": self.account_number,
            "name": self.name,
            "connection_date": str(self.connection_date),
            "active": self.active,
        }
