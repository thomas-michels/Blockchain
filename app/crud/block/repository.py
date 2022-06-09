"""
    Module for block repository
"""

from typing import List
from app.db import BaseRepository
from app.crud.block.schemas import BlockSchema, BlockSchemaInDB
from app.crud.block.model import BlockModel

class BlockRepository(BaseRepository):
    """
    BlockRepository class
    """

    def create(self, item: BlockSchema) -> BlockSchemaInDB:
        """
        This method save item in BlockModel

        :params:
            item: BlockSchema

        :return:
            BlockSchema
        """
        block = BlockModel(**item.dict()).save_safe() 
        return BlockSchemaInDB(**block.serialize())

    def get(self) -> List[BlockSchemaInDB]:
        """
        This method get all blocks in DB

        return:
            List[BlockSchemaInDB]
        """
        results = BlockModel.objects_safe().all()
        return [BlockSchemaInDB(**block.serialize()) for block in results]

    def get_by_id(self, id: str) -> BlockSchemaInDB:
        block_model = self.__get_by_id(id)
        return BlockSchemaInDB(**block_model.serialize())

    def delete(self, id: str) -> BlockSchemaInDB:
        """
        This method delete by id summarized item in Block

        :params:
            id: str

        :return:
            BlockSchemaInDB
        """
        result = self.__get_by_id(id)
        result.delete()

        return BlockSchema(**result.serialize())

    def __get_by_id(self, id) -> BlockModel:
        """
        This method get block by id and return model

        :return:
            BlockModel
        """
        return BlockModel.objects_safe(id=id).first()
