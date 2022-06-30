"""
    Module for transaction repository
"""

from typing import List
from app.db import BaseRepository
from app.crud.transaction import (
    TransactionSchemaInDB,
    TransactionModel,
)


class TransactionRepository(BaseRepository):
    """
    TokenRepository class
    """

    def create(self, item: TransactionSchemaInDB) -> TransactionSchemaInDB:
        """
        This method save item in TokenModel

        :params:
            item: TransactionSchemaInDB

        :return:
            TransactionSchemaInDB
        """
        item_serialized = item.dict()
        TransactionModel(**item_serialized).save_safe()
        return item

    def get(self) -> List[TransactionSchemaInDB]:
        """
        This method get all tokens in DB

        return:
            List[TransactionSchemaInDB]
        """
        results = TransactionModel.objects_safe().all()
        return [TransactionSchemaInDB(**token.serialize()) for token in results]

    def get_by_id(self, id: str) -> TransactionSchemaInDB:
        transaction = self.__get_by_id(id)
        return TransactionSchemaInDB(**transaction.serialize())

    def __get_by_id(self, id: str) -> TransactionModel:
        """
        This method get token by key and return model

        :return:
            TransactionModel
        """
        return TransactionModel.objects_safe(transaction_id=id).first()
