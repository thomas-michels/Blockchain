"""
    Module for event receiver callback
"""
from app.callbacks.callback_interface import CallbackInterface
from app.shared_schemas import EventSchema
from app.configs import get_logger

_logger = get_logger(name=__name__)


class EventReceiverCallback(CallbackInterface):
    """
    Class for EventReceiverCallback
    """

    def handle(self, message: EventSchema) -> bool:
        try:
            _logger.info(f"Message - {message}")
            # payloads = [json.loads(raw) for raw in message.payload["data"]]
            # block = SimpleBlockSchema(**message.payload)
            # feedback = BlockServices().create_block(block)
            # if feedback.is_success:
            #     return True

            # return False

        except Exception as error:
            return False
