"""
    Module for Account Services
"""

from datetime import datetime
from typing import List
from app.crud import token
from app.crud.account import AccountRepository, AccountSchema, SimpleAccountSchema, AccountSchemaInDB
from app.crud.token import NTTokenSchema
from app.crud.transaction.schemas import TransactionSchemaInDB
from app.exceptions import AccountInexistent, TransactionUnfonded
from app.configs import get_logger
from hashlib import sha256
from random import randint
from app.utils import generate_uuid

_logger = get_logger(name=__name__)


class AccountServices:
    """
    AccountServices class
    """

    def __init__(self) -> None:
        self.__sha256 = sha256()
        self.__repository = AccountRepository()

    def create_account(self, simple_account: SimpleAccountSchema) -> AccountSchemaInDB:
        """
        Method to insert account in DB

        :param simple_account: SimpleAccountSchema
        :return: AccountSchemaInDB
        """
        try:
            account = self.__mount_account(simple_account)
            account_schema = self.__repository.create(account)
            if account_schema:
                _logger.info(
                    f"Account saved with success. Number: {account_schema.number}"
                )
                return account_schema

            _logger.info("Account not saved")
            return False

        except Exception as error:
            _logger.error(f"Account not saved. Error: {error}")
            return False

    def get_all_accounts(self) -> List[AccountSchema]:
        """
        Method to get all blocks in DB

        :return: List[AccountSchema]
        """
        return self.__repository.get()

    def get_by_number(self, number: int) -> AccountSchema:
        """
        Method to get by number

        :return: List[AccountSchema]
        """
        return self.__repository.get_by_number(number)

    def delete(self, number: int) -> AccountSchema:
        """
        Method to delete by number

        :return: AccountSchema
        """
        return self.__repository.delete(number)

    def get_tokens_account(self, number: int, quantity: int) -> List[str]:
        account = self.__repository.get_by_number(number)
        if 0 < len(account.balance) >= quantity:
            return account.balance[:quantity]

        raise TransactionUnfonded

    def add_mined_tokens(self, number: int, tokens: List[NTTokenSchema]) -> bool:
        return self.__repository.add_mined_tokens(number, tokens)

    def register_transaction(self, transaction: TransactionSchemaInDB) -> True:
        """
        Method to add 
        """
        try:
            sender_account = self.get_by_number(transaction.sender_number)
            receiver_account = self.get_by_number(transaction.receiver_number)
            if sender_account and receiver_account:
                self.__repository.registry_new_transaction(receiver_account.number, transaction)
                self.__repository.registry_new_transaction(sender_account.number, transaction)
                _logger.info("Tokens sended with success")
                return True

        except Exception as error:
            _logger.error(f"Error in register_transaction. Error: {error}")
            raise TransactionUnfonded()

    @staticmethod
    def __check_found(sender_account: AccountSchema, tokens: List[NTTokenSchema]) -> List[NTTokenSchema]:
        tokens_to_send = []
        for token in sender_account.balance:
            if token in tokens:
                tokens_to_send.append(token)        

            else:
                return []
        
        return tokens_to_send

    def __mount_account(self, simple_account: SimpleAccountSchema) -> AccountSchemaInDB:

        payload = {}
        payload["account_id"] = generate_uuid()
        payload["nickname"] = simple_account.nickname
        payload["password"] = self.__generate_hash(simple_account.password)
        payload["creation_date"] = datetime.now()
        payload["number"] = self.__generate_valid_number()
        payload["history"] = []
        payload["balance"] = []
        payload["active"] = True

        return AccountSchemaInDB(**payload)

    def __generate_hash(self, password: str) -> str:
        self.__sha256.update(bytes(password, encoding="utf-8"))
        return self.__sha256.hexdigest()

    def __generate_valid_number(self) -> int:
        while True:
            try:
                number = randint(10000, 999999)
                self.get_by_number(number)

            except AccountInexistent:
                return number
