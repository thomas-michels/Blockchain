"""
    Module for client repository
"""

from typing import List
from app.db import BaseRepository
from app.crud.client import ClientSchema, ClientModel


class ClientRepository(BaseRepository):
    """
    ClientRepository class
    """

    def create(self, item: ClientSchema) -> ClientSchema:
        """
        This method save item in ClientModel

        :params:
            item: ClientSchema

        :return:
            ClientSchema
        """
        item_serialized = item.dict()
        ClientModel(**item_serialized).save_safe()
        return item

    def get(self, active=False) -> List[ClientSchema]:
        """
        This method get all blocks in DB

        :param active: bool (default=False)

        return:
            List[ClientSchema]
        """
        results = ClientModel.objects_safe().all()
        clients = []
        for client in results:
            if not active:
                clients.append(ClientSchema(**client.serialize()))
            
            else:
                if client.active:
                    clients.append(ClientSchema(**client.serialize()))

        return clients

    def get_by_id(self, id: str) -> ClientSchema:
        block_model = self.__get_by_id(id)
        return ClientSchema(**block_model.serialize())

    def delete(self, id: str) -> ClientSchema:
        """
        This method delete by id summarized item in Block

        :params:
            id: str

        :return:
            ClientSchema
        """
        result = self.__get_by_id(id)
        result.active = False
        result.save_safe()

        return ClientSchema(**result.serialize())

    def __get_by_id(self, id) -> ClientModel:
        """
        This method get block by id and return model

        :return:
            BlockModel
        """
        return ClientModel.objects_safe(id=id).first()
