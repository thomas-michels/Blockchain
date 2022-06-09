"""
Queue manager file
"""

from typing import Any, List
from app.utils import SingletonMeta
from kombu import Exchange, Queue
from app.configs import get_environment, get_logger
from app.queues.queue_callback import QueueCallback
from app.exceptions import QueueNotFound, CallbackAlreadyCreated

_env = get_environment()
_logger = get_logger(name=__name__)


class QueueManager(metaclass=SingletonMeta):
    """
    This class create and save queues in list
    """

    def __init__(self) -> None:
        super().__init__()
        self._queues: List[QueueCallback] = []

    def destroy(self):
        self._queues = []

    def register_callback(self, queue_name: str, function: Any) -> None:
        """
        Method to register new callback

        :parms:
            queue_name: str
            function: Any

        :return:
            NoReturn
        """
        try:
            queue_exchange = self._create_exchange()

            queue = self._create_queue(queue_name.upper(), queue_exchange)

            queue_callback = QueueCallback(
                queue_name=queue_name.upper(), queue=queue, function=function
            )

            if self.get_queue_by_name(queue_callback.get_queue_name()):
                raise CallbackAlreadyCreated()

            self._queues.append(queue_callback)
            _logger.info(f"QUEUE: {queue_name.upper()} REGISTRED")

        except CallbackAlreadyCreated as error:
            _logger.error(f"Error on register callbacks - Error: {error}")

    def get_queues(self) -> List[Queue]:
        """
        Method to return all queues

        :return:
            List[Queue]
        """
        return [callback.get_queue() for callback in self._queues]

    def get_function(self, queue_name: str) -> Any:
        """
        Method to get callback function

        :return:
            Any
        """
        for callback in self._queues:
            if callback.get_queue_name() == queue_name.upper():
                return callback.get_function()

        raise QueueNotFound()

    def get_queue_by_name(self, queue_name: str) -> Queue:
        """
        Method to get queue by name

        :return:
            Any
        """
        for callback in self._queues:
            if callback.get_queue_name() == queue_name.upper():
                return callback.get_queue()

    def _create_exchange(self) -> Exchange:
        """
        Method to create exchange

        :return:
            Exchange
        """

        queue_exchange = Exchange(
            name=_env.RBMQ_EXCHANGE, type="direct"
        )
        return queue_exchange

    def _create_queue(self, queue_name: str, queue_exchange: Exchange) -> Queue:
        """
        Method to create queue

        :parms:
            queue_name: str
            queue_exchange: Exchange

        :return:
            Queue
        """
        return Queue(
            name=queue_name,
            exchange=queue_exchange,
            routing_key=queue_name,
            queue_arguments={
                "x-dead-letter-exchange": f"{_env.RBMQ_EXCHANGE}",
                "x-dead-letter-routing-key": "delay",
                "durable": True,
            },
        )
