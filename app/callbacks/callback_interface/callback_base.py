"""
    Module for callbacks interface
"""

from abc import abstractmethod, ABC


class CallbackInterface(ABC):
    """
    Class for callback base
    """

    @abstractmethod
    def handle(self, message) -> bool:
        """
        This method handle message and returns a bool

        :param:
            message
        :return: 
            Boolean
        """
