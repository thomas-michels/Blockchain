"""
    Module for register block callback
"""
from app.callbacks.callback_interface import CallbackInterface
from app.shared_schemas import EventSchema
from app.configs import get_logger

_logger = get_logger(name=__name__)


class RegisterBlockCallback(CallbackInterface):
    """
    Class for callback register block
    """

    def handle(self, message: EventSchema) -> bool:
        """
        This method save block in db

        :params:
            message: EventSchema

        :return:
            bool
        """
        _logger.info(f"Message - {message}")
        return True
