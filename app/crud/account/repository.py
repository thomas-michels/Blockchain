"""
    Module for client repository
"""

from typing import List
from app.db import BaseRepository
from app.crud.account import AccountSchemaInDB, AccountSchema, AccountModel
from app.exceptions import AccountInexistent


class AccountRepository(BaseRepository):
    """
    AccountRepository class
    """

    def create(self, item: AccountSchema) -> AccountSchema:
        """
        This method save item in ClientModel

        :params:
            item: AccountSchema

        :return:
            AccountSchema
        """
        item_serialized = item.dict()
        AccountModel(**item_serialized).save_safe()
        return item

    def get(self, active=False) -> List[AccountSchema]:
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
                accounts.append(AccountSchema(**account.serialize()))

            else:
                if account.active:
                    accounts.append(AccountSchema(**account.serialize()))

        return accounts

    def get_by_number(self, number: int) -> AccountSchema:
        account_model = self.__get_by_number(number)
        return AccountSchema(**account_model.serialize())

    def delete(self, number: int) -> AccountSchema:
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

        return AccountSchema(**result.serialize())

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
