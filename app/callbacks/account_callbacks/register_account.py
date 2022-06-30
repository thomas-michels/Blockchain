"""
    Module for send tokens callbacks
"""
from app.callbacks.callback_interface import CallbackInterface
from app.crud.account import AccountServices, SimpleAccountSchema
from app.shared_schemas import EventSchema
from app.configs import get_logger

_logger = get_logger(name=__name__)


class RegisterAccountCallback(CallbackInterface):
    """
    RegisterAccountCallback class
    """

    def handle(self, message: EventSchema) -> bool:
        """
        Method to handle send tokens to account

        :return: bool
        """
        _logger.info(
            f"Registring new account"
        )

        simple_account = SimpleAccountSchema(**message.payload)
        service = AccountServices()
        try:
            account_saved = service.create_account(simple_account)
            if account_saved:
                _logger.info(
                    f"Account registered success. ID: {account_saved.account_id}"
                )
                return True

            _logger.info(f"Account not created")
            return False

        except Exception as error:
            _logger.error(f"Error in RegisterAccountCallback. Error: {error}")
            return False
