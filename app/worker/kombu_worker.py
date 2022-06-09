"""
Kombu worker class module
"""

from kombu.mixins import ConsumerMixin
from app.configs import get_logger
from app.exceptions import QueueNotFound
from app.queues import QueueManager

_logger = get_logger(name=__name__)


class KombuWorker(ConsumerMixin):
    """
    This class is Kombu Worker
    """

    def __init__(self, connection):
        self.queues = QueueManager()
        self.connection = connection

    def get_consumers(self, consumer, channel):
        return [
            consumer(queues=self.queues.get_queues(), callbacks=[self.process_task])
        ]

    def process_task(self, body, message):
        try:
            infos = message.delivery_info
            _logger.info(f"Message received to {infos['routing_key']}")
            function = self.queues.get_function(infos["routing_key"])
            if function(body):
                message.ack()
        except QueueNotFound:
            _logger.error("Callback not found!")

        except Exception as error:
            _logger.error(f"Error on process_task - {error}")
