"""
    Module for send tokens callbacks
"""
from app.callbacks.callback_interface import CallbackInterface
from app.crud.token import TokenServices, TokensCallbackSchema
from app.crud.account import AccountServices
from app.shared_schemas import EventSchema
from app.configs import get_logger
from app.exceptions import AccountInexistent

_logger = get_logger(name=__name__)


class SendTokensToAccount(CallbackInterface):
    """
    SendTokensToAccount class
    """

    def handle(self, message: EventSchema) -> bool:
        """
        Method to handle send tokens to account

        :return: bool
        """
        _logger.info("Creating new tokens")
        try:
            token_callback = TokensCallbackSchema(**message.payload)
            services = TokenServices()
            tokens_list = services.generate_tokens(token_callback.quantity)

            account_services = AccountServices()
            if account_services.add_mined_tokens(token_callback.account_number, tokens_list):
                _logger.info("Tokens created with success")
                return True

            return False

        except AccountInexistent:
            _logger.info("Tokens created but Account is inexistent")
            return True

        except Exception as error:
            _logger.error(f"Error in SendTokensToAccount. Error: {error}")
            return False
