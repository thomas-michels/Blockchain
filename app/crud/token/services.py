"""
    Module token services
"""

from typing import List
from app.configs import get_logger
from datetime import datetime
from app.crud.token import TokenRepository, NTTokenSchema
from app.utils import generate_uuid

_logger = get_logger(name=__name__)


class TokenServices:
    """
    TokenServices class
    """

    def __init__(self) -> None:
        self.__repository = TokenRepository()

    def generate_tokens(self, quantity: int) -> List[NTTokenSchema]:
        """
        Method to insert token in DB

        :param quantity: int
        :return: List[NTTokenSchema]
        """
        try:
            tokens = []
            for i in range(quantity):
                token = self.__mount_token()
                tokens.append(self.__repository.create(token))

            return tokens

        except Exception as error:
            _logger.error(f"Error on generate token. Error: {error}")
            return []

    def get_tokens_mined(self) -> int:
        return len(self.__repository.get())

    def __mount_token(self) -> NTTokenSchema:
        payload = {}
        payload["key"] = generate_uuid()
        payload["creation_date"] = datetime.now()
        return NTTokenSchema(**payload)
