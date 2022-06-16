"""
This module start connection with queues
"""

from kombu import Connection
from app.worker.consumer import RegisterQueues
from app.configs import get_logger, get_environment
from app.worker import KombuWorker

_logger = get_logger(name=__name__)
_env = get_environment()


class Application:
    """This class start connection and worker"""

    def __init__(self) -> None:
        _logger.info("Creating Connection...")

        queues = RegisterQueues.register()
        self.start_consuming(queues)

    def start_consuming(self, queues):
        _logger.info("Start consuming...")
        with Connection(
            hostname=_env.RBMQ_HOST,
            userid=_env.RBMQ_USER,
            password=_env.RBMQ_PASS,
            port=_env.RBMQ_PORT,
            virtual_host=_env.RBMQ_VHOST,
        ) as conn:
            worker = KombuWorker(conn, queues)
            worker.run()
