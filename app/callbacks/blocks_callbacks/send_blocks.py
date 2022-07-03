"""
    Module for send blocks to all consumers
"""
from typing import List
from app.callbacks.callback_interface import CallbackInterface
from app.crud.block import BlockServices, SimpleBlockSchema
from app.shared_schemas import EventSchema
from app.configs import get_logger, get_environment
from app.worker.producer import KombuProducer
from app.utils import generate_event_client
from app.worker.utils import get_all_active_clients

_logger = get_logger(name=__name__)
_env = get_environment()

class SendBlocksToConsumers(CallbackInterface):
    """
    Class for callback send blocks
    """
    def handle(self, message: EventSchema) -> bool:
        """
        This method send all blocks to consumers
        """
        try:
            _logger.info(f"Message - {message}")
            clients = get_all_active_clients()
            blocks = BlockServices().get_all_blocks()
            blocks_serialized = [block.dict() for block in blocks]
            for client in clients:
                message = generate_event_client(send_to=client["name"], function=_env.VALIDATE_FUNCTION, payload={"data": blocks_serialized})
                KombuProducer.send_messages(message)
                _logger.info(f"Send blocks to client: {client['name']}")
            
            _logger.info("Sended all blocks for all active clients")
            return True

        except Exception as error:
            _logger.error(f"Error in send blocks: {error}")
            return False
