"""
    Module for Validate Chain
"""
from app.callbacks.callback_interface import CallbackInterface
from app.shared_schemas import EventClientSchema
from app.configs import get_logger, get_environment
from app.worker.producer import KombuProducer
from app.utils import generate_event_client, generate_event
from app.worker.utils import get_all_active_clients
import time
from app.crud.client import ClientServices

_logger = get_logger(name=__name__)
_env = get_environment()


class ElectionCallback(CallbackInterface):
    """
    ElectionCallback
    """

    def handle(self, message: EventClientSchema) -> bool:
        try:
            _logger.info(f"Winner: {message.payload['client_name']}")
            clients = get_all_active_clients()
            producer = KombuProducer()
            for client in clients:
                if client["name"] != message.payload["client_name"]:
                    payload = generate_event_client(
                        send_to=client["name"],
                        function=_env.STOP_POW_FUNCTION,
                        payload={"winner": message.payload["client_name"]},
                    )
                    producer.send_messages(payload)

            _logger.info("POW stopped in all clients")
            # Enviar novo bloco
            payload = generate_event_client(
                send_to=message.payload["client_name"],
                function=_env.NEW_BLOCK_FUNCTION,
                payload={
                    "data": message.payload["data"],
                    "nonce": message.payload["nonce"],
                },
            )
            producer.send_messages(payload)

            time.sleep(0.5)
            # Validar blockchain
            payload = generate_event(
                send_to=_env.VALIDATE_CHANNEL,
                payload={"winner": message.payload["client_name"]},
            )
            producer.send_messages(payload)

            # Enviar recompensas
            _logger.info("Sending rewards")
            client_services = ClientServices()
            for client in clients:
                client_schema = client_services.get_client_by_name(client["name"])
                payload = generate_event(
                    send_to=_env.TOKENS_CHANNEL,
                    payload={
                        "quantity": _env.REWARD,
                        "account_number": client_schema.account_number,
                    },
                )
                producer.send_messages(payload)

            return True

        except Exception as error:
            _logger.error(f"Error on ElectionCallback: {error}")
            return False
