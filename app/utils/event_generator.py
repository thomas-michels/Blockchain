"""
    Module for event generator function
"""
from app.shared_schemas import EventSchema, EventClientSchema
from app.utils.uuid_generator import generate_uuid
from datetime import datetime


def generate_event(send_to: str, payload: dict) -> EventSchema:
    """
    Function to generate valid EventSchema

    :param send_to: Name of queue to send this message
    :param payload: Payload of event

    :return: EventSchema
    """
    event = {
        "id": generate_uuid(),
        "sended_to": send_to,
        "payload": payload,
        "creation_date": datetime.now(),
    }
    return EventSchema(**event)


def generate_event_client(
    send_to: str, function: str, payload: dict
) -> EventClientSchema:
    """
    Function to generate valid EventSchema

    :param send_to: Name of queue to send this message
    :param payload: Payload of event

    :return: EventClientSchema
    """
    event = {
        "id": generate_uuid(),
        "sended_to": send_to,
        "function": function,
        "payload": payload,
        "creation_date": datetime.now(),
    }
    return EventClientSchema(**event)
