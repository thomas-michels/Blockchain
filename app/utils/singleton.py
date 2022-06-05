"""
Module to singleton class
"""


class Singleton:
    """
    Singleton class
    """

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
