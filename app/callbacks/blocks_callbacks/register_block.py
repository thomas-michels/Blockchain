"""
    Module for register block callback
"""
from app.callbacks.callback_interface import CallbackInterface
from app.crud.block import BlockServices
from app.crud.block import SimpleBlockSchema
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
        try:
            _logger.info(f"Message - {message}")
            block = SimpleBlockSchema(**message.payload)
            feedback = BlockServices().create_block(block)
            if feedback.is_success:
                _logger.info("New block saved")
                return True

            return False

        except Exception as error:
            return False
