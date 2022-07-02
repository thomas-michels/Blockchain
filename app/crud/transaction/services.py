"""
    Module transaction services
"""

from typing import List
from app.configs import get_logger, get_environment
from datetime import datetime
from app.crud.transaction import (
    TransactionSchemaInDB,
    TransactionRepository,
    TransactionSchema,
    MiddleTransactionSchema
)
from app.utils import generate_uuid, generate_event, timed_lru_cache
from app.worker.producer import KombuProducer

_logger = get_logger(name=__name__)
_env = get_environment()


class TransactionsServices:
    """
    TokenServices class
    """

    def __init__(self) -> None:
        self.__repository = TransactionRepository()

    def create_transaction(self, transaction: MiddleTransactionSchema) -> TransactionSchemaInDB:
        """
        Method to insert token in DB

        :param quantity: int
        :return: List[NTTokenSchema]
        """
        try:
            transaction_schema = self.__mount_transaction(transaction)
            transaction_saved = self.__repository.create(transaction_schema)
            producer = KombuProducer()
            message = generate_event(_env.ACCOUNT_BALANCE_CHANNEL, transaction_saved.dict())
            if producer.send_messages(message):
                return transaction_saved

            return False

        except Exception as error:
            _logger.error(f"Error on transaction. Error: {error}")
            return None

    def get_all_transactions(self) -> List[TransactionSchemaInDB]:
        """
        Method to get all TransactionSchemaInDB

        :return: List[TransactionSchemaInDB]
        """
        return self.__repository.get()

    def get_by_id(self, transaction_id: str) -> TransactionSchemaInDB:
        """
        Method to get by id TransactionSchemaInDB

        :return: TransactionSchemaInDB
        """
        return self.__repository.get_by_id(transaction_id)

    def __mount_transaction(
        self, transaction: MiddleTransactionSchema
    ) -> TransactionSchemaInDB:
        payload = {}
        payload["transaction_id"] = generate_uuid()
        payload["sender_number"] = transaction.sender_number
        payload["receiver_number"] = transaction.receiver_number
        payload["quantity"] = transaction.quantity
        payload["balance"] = transaction.balance
        payload["creation_date"] = datetime.now()
        return TransactionSchemaInDB(**payload)
