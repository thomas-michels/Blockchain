"""
    Module for send tokens callbacks
"""
from app.callbacks.callback_interface import CallbackInterface
from app.crud.transaction import TransactionsServices, SimpleTransactionSchema, MiddleTransactionSchema
from app.crud.account import AccountServices
from app.shared_schemas import EventSchema
from app.configs import get_logger, get_environment
from app.exceptions import TransactionUnfonded

_logger = get_logger(name=__name__)
_env = get_environment()


class CreateTransactionCallback(CallbackInterface):
    """
    SendTokensToAccount class
    """

    def handle(self, message: EventSchema) -> bool:
        """
        Method to handle send tokens to account

        :return: bool
        """
        _logger.info("Creating new Transaction")

        try:
            transaction = SimpleTransactionSchema(**message.payload)
            account_services = AccountServices()
            services = TransactionsServices()
            transaction.quantity = int(transaction.quantity * _env.BALANCE_CONVERTER)

            tokens = account_services.get_tokens_account(
                transaction.sender_number, transaction.quantity
            )
            transaction_schema = transaction.dict()
            transaction_schema["balance"] = tokens
            transaction_schema = MiddleTransactionSchema(**transaction_schema)
            transaction_saved = services.create_transaction(transaction=transaction_schema)
            if transaction_saved:
                _logger.info(f"Transaction created with id: {transaction_saved.transaction_id}")
                return True

            _logger.info(f"Transaction not created")
            return False

        except TransactionUnfonded:
            _logger.info("Transaction unfonded")
            return True

        except Exception as error:
            _logger.error(f"Error in CreateTransactionCallback. Error: {error}")
            return False
