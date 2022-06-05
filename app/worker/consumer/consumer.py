"""
    Module Consumer
"""
from typing import Dict
from confluent_kafka import Consumer as ConfluentConsumer
from app.utils import Singleton


class Consumer(Singleton):
    """
    Consumer class
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
            # TODO logger
            pass

    def 

    def start_connection(self) -> ConfluentConsumer:
        try:
            return ConfluentConsumer(self.__generate_payload())

        except Exception:
            pass
            # _logger.error("Error on connect Consumer")

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
