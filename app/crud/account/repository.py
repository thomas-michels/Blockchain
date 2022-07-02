"""
    Module for client repository
"""

from typing import List
from app.crud.token import NTTokenSchema
from app.db import BaseRepository
from app.crud.account import (
    AccountSchema,
    AccountModel,
    AccountSchemaInDB,
    StandardAccountSchema,
)
from app.exceptions import AccountInexistent
from app.crud.transaction import TransactionSchemaInDB


class AccountRepository(BaseRepository):
    """
    AccountRepository class
    """

    def create(self, item: AccountSchemaInDB) -> StandardAccountSchema:
        """
        This method save item in ClientModel

        :params:
            item: AccountSchema

        :return:
            AccountSchema
        """
        item_serialized = item.dict()
        new_item = AccountModel(**item_serialized)
        new_item.save_safe()
        return StandardAccountSchema(**item_serialized)

    def get(self, active=False) -> List[StandardAccountSchema]:
        """
        This method get all accounts in DB

        :param active: bool (default=False)

        return:
            List[AccountSchema]
        """
        results = AccountModel.objects_safe().all()
        accounts = []
        for account in results:
            if not active:
                accounts.append(StandardAccountSchema(**account.serialize()))

            else:
                if account.active:
                    accounts.append(StandardAccountSchema(**account.serialize()))

        return accounts

    def get_by_number(self, number: int, password=False) -> StandardAccountSchema:
        account_model = self.__get_by_number(number)
        if password:
            return AccountSchemaInDB(**account_model.serialize_password())
            
        return StandardAccountSchema(**account_model.serialize())

    def delete(self, number: int) -> StandardAccountSchema:
        """
        This method delete by id summarized item in Account

        :params:
            number: int

        :return:
            ClientSchema
        """
        result = self.__get_by_number(number)
        result.active = False
        result.save_safe()

        return StandardAccountSchema(**result.serialize())

    def add_mined_tokens(self, number: int, tokens: List[NTTokenSchema]) -> bool:
        account = self.__get_by_number(number)
        keys = [token.key for token in tokens]
        account.balance.extend(keys)
        account.save_safe()
        return True

    def registry_new_transaction(self, number: int, transaction: TransactionSchemaInDB):
        account = self.__get_by_number(number)
        account.history.append(transaction.transaction_id)
        if account.number == transaction.sender_number:
            for token in transaction.balance:
                account.balance.remove(token)

        elif account.number == transaction.receiver_number:
            account.balance.extend(transaction.balance)

        account.save_safe()

    def __get_by_number(self, number: int) -> AccountModel:
        """
        This method get account by number and return model

        :return:
            AccountModel
        """
        account = AccountModel.objects_safe(number=number).first()

        if account:
            return account

        raise AccountInexistent(f"Account with number {number} not exists")
