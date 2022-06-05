"""
This is a safe document mixing module
"""

import time
from app.config import get_logger
from app.exceptions import (
    MongoSaveException,
    MongoObjectsException,
)

_logger = get_logger(name=__name__)


class SafeDocumentMixin:
    def save_safe(self, *args, **kwargs):
        for attempt in range(5):
            try:
                return self.save(*args, **kwargs)
            except MongoSaveException as err:
                wait_t = 0.5 * pow(2, attempt)  # exponential back off
                _logger.warning(
                    "PyMongo auto-reconnecting... %s. Waiting %.1f seconds.",
                    str(err),
                    wait_t,
                )
                time.sleep(wait_t)

    @classmethod
    def objects_safe(cls, *args, **kwargs):
        for attempt in range(5):
            try:
                return cls.objects(*args, **kwargs)
            except MongoObjectsException as err:
                wait_t = 0.5 * pow(2, attempt)  # exponential back off
                _logger.warning(
                    "PyMongo auto-reconnecting... %s. Waiting %.1f seconds.",
                    str(err),
                    wait_t,
                )
                time.sleep(wait_t)
