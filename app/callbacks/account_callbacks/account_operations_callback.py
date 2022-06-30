"""
    Module for send tokens callbacks
"""
from app.callbacks.callback_interface import CallbackInterface
from app.crud.transaction import TransactionSchemaInDB
from app.crud.account import AccountServices
from app.shared_schemas import EventSchema
from app.configs import get_logger

_logger = get_logger(name=__name__)


class AccountBalanceCallback(CallbackInterface):
    """
    AccountAddBalanceCallback class
    """

    def handle(self, message: EventSchema) -> bool:
        """
        Method to handle send tokens to account

        :return: bool
        """
        transaction = TransactionSchemaInDB(**message.payload)
        _logger.info(
            f"Start validation of transaction with id: {transaction.transaction_id}"
        )

        service = AccountServices()
        try:
            if service.register_transaction(transaction):
                _logger.info(
                    f"Transaction registered success. ID: {transaction.transaction_id}"
                )
                return True

            _logger.info(f"Transaction not validated")
            return False

        except Exception as error:
            _logger.error(f"Error in AccountBalanceCallback. Error: {error}")
            return False
