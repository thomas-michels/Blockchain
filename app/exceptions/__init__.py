"""
    Module for exceptions
"""

from app.exceptions.shared_exceptions import MethodNotImplemented
from app.exceptions.mongo_exceptions import (
    MongoConnectionException,
    MongoObjectsException,
    MongoSaveException,
    HealthCheckMongoDB,
)
from app.exceptions.callback_exceptions import (
    CallbackAlreadyCreated,
    CallbackNotMethod,
    FunctionAnnotation,
    QueueNotFound,
)

from app.exceptions.account_exceptions import *

from app.exceptions.transactions_exceptions import *
