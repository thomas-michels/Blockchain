"""
    Module for AccountModel
"""

from mongoengine import (
    Document,
    StringField,
    DateTimeField,
    IntField,
    ListField,
    BooleanField,
)
from app.db import SafeDocumentMixin


class AccountModel(Document, SafeDocumentMixin):
    """
    AccountModel class
    """

    account_id = StringField(unique=True)
    number = IntField(required=True)
    nickname = StringField(required=True)
    password = StringField(required=True)
    history = ListField(required=False)
    balance = ListField(required=False)
    creation_date = DateTimeField(required=True)
    active = BooleanField(required=True)

    meta = {"collection": "accounts", "indexes": ["account_id"]}

    def serialize(self) -> dict:
        return {
            "account_id": self.account_id,
            "number": self.number,
            "nickname": self.nickname,
            "history": self.history,
            "balance": self.balance,
            "creation_date": self.creation_date,
            "active": self.active,
        }
