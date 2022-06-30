"""
    Module for TransactionModel
"""

from mongoengine import Document, StringField, DateTimeField, IntField, ListField
from app.db import SafeDocumentMixin


class TransactionModel(Document, SafeDocumentMixin):
    """
    TransactionModel class
    """

    transaction_id = StringField(unique=True)
    sender_number = IntField(required=True)
    receiver_number = IntField(required=True)
    quantity = IntField(required=True)
    balance = ListField(required=True)
    creation_date = DateTimeField(required=True)

    meta = {"collection": "transactions", "indexes": ["transaction_id"]}

    def serialize(self) -> dict:
        return {
            "transaction_id": self.transaction_id,
            "sender_number": self.sender_number,
            "receiver_number": self.receiver_number,
            "balance": self.balance,
            "creation_date": self.creation_date,
        }
