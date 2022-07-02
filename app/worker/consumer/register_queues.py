"""
    Module for register queues
"""
from app.worker.consumer.manager import QueueManager
from app.configs import get_logger, get_environment
from app.callbacks import (
    RegisterBlockCallback,
    RegisterClientCallback,
    SendBlocksToConsumers,
    SendTokensToAccount,
    CreateTransactionCallback,
    AccountBalanceCallback,
    RegisterAccountCallback,
    EventReceiverCallback
)

_logger = get_logger(name=__name__)
_env = get_environment()


class RegisterQueues:
    """
    RegisterQueues class
    """

    @staticmethod
    def register() -> QueueManager:
        _logger.info("Starting QueueManager")
        queue_manager = QueueManager()

        queue_manager.register_callback(
            _env.EVENT_CHANNEL, EventReceiverCallback().handle
        )

        queue_manager.register_callback(
            _env.ELECTION_CHANNEL, EventReceiverCallback().handle
        )

        queue_manager.register_callback(
            _env.BLOCK_CHANNEL, RegisterBlockCallback().handle
        )

        queue_manager.register_callback(
            _env.REGISTER_CHANNEL, RegisterClientCallback().handle
        )

        queue_manager.register_callback(
            _env.TRANSACTIONS_CHANNEL, CreateTransactionCallback().handle
        )

        queue_manager.register_callback(
            _env.ACCOUNT_BALANCE_CHANNEL, AccountBalanceCallback().handle
        )

        queue_manager.register_callback(
            _env.ACCOUNT_REGISTER_CHANNEL, RegisterAccountCallback().handle
        )

        queue_manager.register_callback(
            _env.TOKENS_CHANNEL, SendTokensToAccount().handle
        )

        queue_manager.register_callback(
            _env.VALIDATE_CHANNEL, SendBlocksToConsumers().handle
        )

        _logger.info("All queues started")

        return queue_manager
