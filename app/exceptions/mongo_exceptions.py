"""
This is a project exceptions module
"""


class MongoSaveException(Exception):
    """Raise when there an error on try to save something on mongo"""


class MongoObjectsException(Exception):
    """Raise when there an error on try to query something on mongo"""


class MongoConnectionException(Exception):
    """Raise when there an error on try connect on mongo"""


class HealthCheckMongoDB(Exception):
    """Raise when there an error on health check mongoDB"""
