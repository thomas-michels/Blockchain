"""
    Module for base repository class
"""
from app.exceptions import MethodNotImplemented


class BaseRepository:
    """
    Base repository class
    """

    def create(self, data):
        """
        """
        raise MethodNotImplemented(message="Create not implemented")

    def get(self, id=None):
        """
        """
        raise MethodNotImplemented(message="Get not implemented")

    def update(self, id, data):
        """
        """
        raise MethodNotImplemented(message="Update not implemented")

    def delete(self, id):
        """
        """
        raise MethodNotImplemented(message="Delete not implemented")
