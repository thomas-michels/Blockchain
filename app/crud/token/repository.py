"""
    Module for token repository
"""

from typing import List
from app.db import BaseRepository
from app.crud.token import NTTokenSchema, TokenModel


class TokenRepository(BaseRepository):
    """
    TokenRepository class
    """

    def create(self, item: NTTokenSchema) -> NTTokenSchema:
        """
        This method save item in TokenModel

        :params:
            item: NTTokenSchema

        :return:
            NTTokenSchema
        """
        item_serialized = item.dict()
        TokenModel(**item_serialized).save_safe()
        return item

    def get(self) -> List[NTTokenSchema]:
        """
        This method get all tokens in DB

        return:
            List[NTTokenSchema]
        """
        results = TokenModel.objects_safe().all()
        return [NTTokenSchema(**token.serialize()) for token in results]

    def get_by_key(self, key: str) -> NTTokenSchema:
        token = self.__get_by_id(key)
        return NTTokenSchema(**token.serialize())

    def __get_by_id(self, key) -> TokenModel:
        """
        This method get token by key and return model

        :return:
            TokenModel
        """
        return TokenModel.objects_safe(key=key).first()
