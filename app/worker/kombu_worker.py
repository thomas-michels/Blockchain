"""
Kombu worker class module
"""

from kombu.mixins import ConsumerMixin
from app.configs import get_logger
from app.exceptions import QueueNotFound
from app.worker.manager import QueueManager
from app.utils import payload_conversor

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
            _logger.info(f"Message received at {infos['routing_key']}")
            function = self.queues.get_function(infos["routing_key"])
            event_schema = payload_conversor(body)
            if event_schema:
                if function(event_schema):
                    message.ack()

        except QueueNotFound:
            _logger.error("Callback not found!")

        except Exception as error:
            _logger.error(f"Error on process_task - {error}")
