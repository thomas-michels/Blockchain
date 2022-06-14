"""
This module start connection with queues
"""

from kombu import Connection
from app.worker.manager import QueueManager
from app.configs import get_logger, get_environment
from app.worker import KombuWorker
from app.callbacks import (
    RegisterBlockCallback,
    RegisterClientCallback,
    SendBlocksToConsumers,
)

_logger = get_logger(name=__name__)
_env = get_environment()


class Application:
    """This class start connection and worker"""

    def __init__(self) -> None:
        _logger.info("Creating Connection...")

        self.queue_manager = QueueManager()

        self.queue_manager.register_callback(
            _env.BLOCK_CHANNEL, RegisterBlockCallback().handle
        )

        self.queue_manager.register_callback(
            _env.REGISTER_CHANNEL, RegisterClientCallback().handle
        )

        self.queue_manager.register_callback(
            _env.VALIDATE_CHANNEL, SendBlocksToConsumers().handle
        )

        self.start_consuming()

    def start_consuming(self):
        _logger.info("Start consuming...")
        with Connection(
            hostname=_env.RBMQ_HOST,
            userid=_env.RBMQ_USER,
            password=_env.RBMQ_PASS,
            port=_env.RBMQ_PORT,
            virtual_host=_env.RBMQ_VHOST,
        ) as conn:
            worker = KombuWorker(conn)
            worker.run()
