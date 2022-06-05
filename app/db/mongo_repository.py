"""
This is a mongo repository module
"""

import mongoengine
from pymongo.errors import ServerSelectionTimeoutError
from app.configs import get_environment, get_logger
from app.exceptions import MongoConnectionException

_logger = get_logger(name=__name__)
_env = get_environment()


class MongoDB:
    """
    MongoDB connection class
    """
    def __init__(self):
        self.__set_connection()

    def __set_connection(self):
        try:
            _logger.debug("Connecting to Mongo")
            connetion = mongoengine.connect(host=_env.MONGODB_URI)
            connetion.server_info()
            _logger.debug("Connected to Mongo")

        except ServerSelectionTimeoutError:
            _logger.critical(f"Error on connect in MongoDB")
            raise MongoConnectionException("Error on connect in MongoDB")

        except Exception as error:
            _logger.critical(f"Error on connect in MongoDB - {error}")
            raise MongoConnectionException("Error on connect in MongoDB")
