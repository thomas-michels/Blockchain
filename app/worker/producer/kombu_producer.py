"""
    Module for Kombu Producer class
"""

from kombu.mixins import Producer
from app.worker.utils import start_connection_bus, connect_on_exchange
from app.configs import get_logger, get_environment
from app.shared_schemas import EventSchema

_env = get_environment()
_logger = get_logger(name=__name__)


class KombuProducer:
    """
    Class for Producer to send messages in queues
    """

    @staticmethod
    def send_messages(message: EventSchema) -> bool:
        """
        Method to send messages

        :param message: EventSchema

        :return: bool
        """
        try:
            with start_connection_bus() as conn:
                producer = Producer(conn)
                producer.publish(
                    body=message.dict(),
                    exchange=connect_on_exchange(_env.RBMQ_EXCHANGE),
                    routing_key=message.sended_to,
                )

            _logger.info(f"Sended message to {message.sended_to}")
            return True

        except Exception as error:
            _logger.error(
                f"Error on send message to {message.sended_to}. Error: {error}"
            )
