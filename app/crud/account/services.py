"""
    Module for Account Services
"""

from typing import List
from app.crud.account import AccountRepository, AccountSchema, SimpleAccountSchema
from app.exceptions import AccountInexistent
from app.utils import Feedback
from app.configs import get_logger
from hashlib import sha256
from app.utils import generate_uuid
from datetime import datetime
from random import randint

_logger = get_logger(name=__name__)


class AccountServices:
    """
    AccountServices class
    """

    def __init__(self) -> None:
        self.__sha256 = sha256()
        self.__repository = AccountRepository()

    def create_account(self, simple_account: SimpleAccountSchema) -> Feedback:
        """
        Method to insert account in DB

        :param simple_account: SimpleAccountSchema
        :return: Feedback
        """
        try:
            account = self.__mount_account(simple_account)
            account_schema = self.__repository.create(account)
            if account_schema:
                _logger.info(
                    f"Account saved with success. Number: {account_schema.number}"
                )
                return Feedback(is_success=True)

            _logger.info("Account not saved")
            return Feedback(is_success=False)

        except Exception as error:
            _logger.error(f"Account not saved. Error: {error}")
            return Feedback(is_success=False, message=error)

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

    def __mount_account(self, simple_account: SimpleAccountSchema) -> AccountSchema:

        payload = {}
        payload["nickname"] = simple_account.nickname
        payload["password"] = self.__generate_hash(simple_account.password)
        payload["creation_date"] = simple_account.creation_date
        payload["number"] = self.__generate_valid_number()
        payload["history"] = []
        payload["balance"] = []
        payload["active"] = True

        return AccountSchema(**payload)

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
