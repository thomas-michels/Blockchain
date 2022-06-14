"""
    Module for block services
"""
from app.crud.block import BlockSchemaInDB, BlockRepository, SimpleBlockSchema
from app.utils import Feedback
from app.configs import get_logger
from hashlib import sha256
from app.utils import generate_uuid
from datetime import datetime

_logger = get_logger(name=__name__)


class BlockServices:
    """
    BlockServices class
    """

    def __init__(self) -> None:
        self.__sha256 = sha256()
        self.__repository = BlockRepository()

    def create_block(self, simple_block: SimpleBlockSchema) -> Feedback:
        """
        Method to insert block in DB

        :param simple_block: SimpleBlockSchema
        :return: Feedback
        """
        try:
            block = self.__mount_block(simple_block)
            block_schema = self.__repository.create(block)
            if block_schema:
                _logger.info(f"Block saved with success. Hash: {block.hash}")
                return Feedback(is_success=True)

            _logger.info("Block not saved")
            return Feedback(is_success=False)

        except Exception as error:
            _logger.error(f"Block not saved. Error: {error}")
            return Feedback(is_success=False, message=error)

    def __mount_block(self, simple_block: SimpleBlockSchema) -> BlockSchemaInDB:
        """
        Method to mount the block

        :param simple_block: SimpleBlockSchema

        :return: BlockSchemaInDB
        """
        payload = {}
        payload["block_id"] = generate_uuid()
        payload["data"] = simple_block.data
        payload["nonce"] = simple_block.nonce
        payload["timestamp"] = datetime.now().timestamp()
        payload["previous_hash"] = self.__repository.get_previous_hash()
        payload["hash"] = self.__generate_hash(payload.__str__())
        block = BlockSchemaInDB(**payload)
        return block

    def __generate_hash(self, payload_str: str) -> str:
        """
        Method to generate hash

        :param block: BlockSchema
        :return: str
        """
        self.__sha256.update(bytes(payload_str, encoding="utf-8"))
        return self.__sha256.hexdigest()
