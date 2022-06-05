"""
    Module Consumer
"""
from typing import Dict
from confluent_kafka import Consumer as ConfluentConsumer
from app.utils import Singleton
from app.configs import get_logger, get_environment

_logger = get_logger(name=__name__)
_env = get_environment()


class Consumer(Singleton):
    """
    Kafka Consumer class
    """

    __topics = []

    def __init__(self) -> None:
        super().__init__()
        self.__client: ConfluentConsumer = self.start_connection()

    def register_topic(self, topic_name: str) -> None:
        """
        Method to register topic to listen
        """
        if self.__check_topic(topic_name):
            self.__topics.append(topic_name)

        else:
            _logger.info(f"Duplicated topic - {topic_name}")

    def __check_topic(self, topic_name) -> bool:
        if topic_name in self.__topics:
            return True
        return False

    def start_connection(self) -> ConfluentConsumer:
        try:
            return ConfluentConsumer(self.__generate_payload())

        except Exception:
            _logger.error("Error on connect Consumer")

    def __generate_payload(self) -> Dict[str, str]:
        return {
        "bootstrap.servers": "pkc-epwny.eastus.azure.confluent.cloud:9092",
        "security.protocol": "SASL_SSL",
        "sasl.mechanisms": "PLAIN",
        "sasl.username": "SXE57BOJVWTB2KK3",
        "sasl.password": "XoILmw1EPO1ggIUU6xY1iK7UodIKf5C5MSrLR+/frO8PQF3CIfpQrVHwJCdhmGdR",
        "group.id": "mygroup",
        "auto.offset.reset": "earliest",
    }
