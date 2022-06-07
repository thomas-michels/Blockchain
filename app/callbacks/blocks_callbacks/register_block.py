"""
    Module for register block callback
"""
from app.callbacks.callback_interface import CallbackInterface
from app.utils import EventSchema


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