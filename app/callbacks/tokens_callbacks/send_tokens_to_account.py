"""
    Module for send tokens callbacks
"""
from app.callbacks.callback_interface import CallbackInterface
from app.crud.token import TokenServices
from app.shared_schemas import EventSchema


class SendTokensToAccount(CallbackInterface):
    """
    SendTokensToAccount class
    """

    def handle(self, message: EventSchema) -> bool:
        """
        Method to handle send tokens to account

        :return: bool
        """
