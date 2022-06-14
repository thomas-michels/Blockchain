"""
    Module for Validate event
"""
from app.shared_schemas import EventSchema
from pydantic.error_wrappers import ValidationError
import json
from app.configs import get_logger

_logger = get_logger(name=__name__)


def payload_conversor(raw_payload) -> EventSchema:
    """
    Function to convert raw payload in EventSchema

    :param payload: dict
    :return: EventSchema
    """
    try:
        payload = json.loads(raw_payload)
        return EventSchema(**payload)

    except ValidationError as err:
        _logger.error(
            f"Error on validate payload in {', '.join([i['loc'][0] for i in err.errors()])} field(s)"
        )