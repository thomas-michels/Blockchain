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

    def get(self):
        """
        """
        raise MethodNotImplemented(message="Get not implemented")

    def get_by_id(self, id):
        """
        """
        raise MethodNotImplemented(message="Get by id not implemented")

    def update(self, id, data):
        """
        """
        raise MethodNotImplemented(message="Update not implemented")

    def delete(self, id):
        """
        """
        raise MethodNotImplemented(message="Delete not implemented")
