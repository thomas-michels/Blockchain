"""
    Module for event receiver callback
"""
from typing import List
from app.callbacks.callback_interface import CallbackInterface
from app.shared_schemas import EventSchema
from app.configs import get_logger, get_environment
from app.utils import get_new_nonce, generate_event_client, generate_hash
from app.worker.producer import KombuProducer
from app.worker.utils import get_all_active_clients
import ast

_logger = get_logger(name=__name__)
_env = get_environment()


class EventReceiverCallback(CallbackInterface):
    """
    Class for EventReceiverCallback
    """

    @staticmethod
    def __decode_payload(payload: List[str]) -> dict:
        payload_converted = []
        for string in payload:
            string = string.replace("'", "\"")
            payload_json = ast.literal_eval(string)
            payload_converted.append(payload_json)

        return payload_converted

    def handle(self, message: EventSchema) -> bool:
        try:
            _logger.info(f"Message - {message}")
            _logger.info("Starting Proof of Work")
            nonce = str(get_new_nonce())
            hashed_nonce = generate_hash(nonce)
            clients = get_all_active_clients()
            payloads = self.__decode_payload(message.payload["data"])
            for client in clients:
                message = generate_event_client(
                    send_to=client["name"],
                    function=_env.POW_FUNCTION,
                    payload={"nonce": hashed_nonce, "data": payloads},
                )
                KombuProducer.send_messages(message)
                _logger.info(f"Function POW started in client: {client['name']}")

            _logger.info("POW started in all clients")
            return True

        except Exception as error:
            _logger.error(f"Error in EventReceiverCallback. Error: {error}")
            return False
