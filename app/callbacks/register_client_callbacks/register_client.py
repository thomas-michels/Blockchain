"""
    Module for RegisterClient callback
"""
from app.callbacks.callback_interface import CallbackInterface
from app.crud.client import ClientServices
from app.crud.client import SimpleClientSchema
from app.shared_schemas import EventSchema
from app.configs import get_logger

_logger = get_logger(name=__name__)


class RegisterClientCallback(CallbackInterface):
    """
    Class for callback register client
    """

    def handle(self, message: EventSchema) -> bool:
        """
        This method register client in db

        :params:
            message: EventSchema

        :return:
            bool
        """
        try:
            _logger.info(f"Message - {message}")
            client = SimpleClientSchema(**message.payload)
            feedback = ClientServices().create_client(client)
            if feedback.is_success:
                return True

            return False

        except Exception as error:
            return False
