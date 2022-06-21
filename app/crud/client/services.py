"""
    Module for client services
"""
from typing import List
from app.crud.client import ClientSchema, ClientRepository, SimpleClientSchema
from app.utils import Feedback
from app.configs import get_logger
from datetime import datetime

_logger = get_logger(name=__name__)


class ClientServices:
    """
    BlockServices class
    """

    def __init__(self) -> None:
        self.__repository = ClientRepository()

    def create_client(self, simple_client: SimpleClientSchema) -> Feedback:
        """
        Method to insert client in DB

        :param simple_client: SimpleClientSchema
        :return: Feedback
        """
        try:
            client = self.__mount_client(simple_client)
            client_schema = self.__repository.create(client)
            if client_schema:
                _logger.info(f"Client registred with success. ID: {client.client_id}")
                return Feedback(is_success=True)

            _logger.info("Client not registred")
            return Feedback(is_success=False)

        except Exception as error:
            _logger.error(f"Client not registred. Error: {error}")
            return Feedback(is_success=False, message=error)

    def get_all_active_clients(self) -> List[ClientSchema]:
        """
        Method to get all active clients in DB

        :return: List[ClientSchema]
        """
        return self.__repository.get(active=True)

    def __mount_client(self, simple_client: SimpleClientSchema) -> ClientSchema:
        """
        Method to mount the block

        :param simple_block: ClientSchema

        :return: ClientSchema
        """
        payload = {}
        payload["client_id"] = simple_client.client_id
        payload["name"] = simple_client.name
        payload["connection_date"] = datetime.now()
        payload["active"] = True
        return ClientSchema(**payload)
