"""
    Module for event generator function
"""
from app.shared_schemas import EventSchema
from app.utils.uuid_generator import generate_uuid
from datetime import datetime


def generate_event(client_id: str, send_to: str, payload: dict) -> EventSchema:
    """
    Function to generate valid EventSchema

    :param send_to: Name of queue to send this message
    :param payload: Payload of event

    :return: EventSchema
    """
    event = {
        "id": generate_uuid(),
        "client_id": client_id,
        "sended_to": send_to,
        "payload": payload,
        "creation_date": datetime.now(),
    }
    return EventSchema(**event)
