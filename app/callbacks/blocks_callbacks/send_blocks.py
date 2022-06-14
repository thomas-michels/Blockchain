"""
    Module for send blocks to all consumers
"""
from app.callbacks.callback_interface import CallbackInterface
from app.crud.block import BlockServices
from app.crud.block import SimpleBlockSchema
from app.shared_schemas import EventSchema
from app.configs import get_logger

_logger = get_logger(name=__name__)


class SendBlocksToConsumers(CallbackInterface):
    """
    Class for callback send blocks
    """

    def handle(self, message) -> bool:
        """
        This method send all blocks to consumers
        """
        try:
            _logger.info(f"Message - {message}")
            blocks = BlockServices().get_all_blocks()
            for block in blocks:
                pass
            
            return True

        except Exception as error:
            return False
