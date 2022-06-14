"""
    Module for block repository
"""

from typing import List
from app.db import BaseRepository
from app.crud.block import BlockSchema, BlockSchemaInDB
from app.crud.block.model import BlockModel


class BlockRepository(BaseRepository):
    """
    BlockRepository class
    """

    def create(self, item: BlockSchemaInDB) -> BlockSchemaInDB:
        """
        This method save item in BlockModel

        :params:
            item: BlockSchemaInDB

        :return:
            BlockSchema
        """
        item_serialized = item.dict()
        BlockModel(**item_serialized).save_safe()
        return item

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

    def get_previous_hash(self) -> str:
        block_model = BlockModel.objects_safe().order_by('-id').first()
        if block_model:
            return block_model.hash
        return ""

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
