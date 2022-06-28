"""
    Module for account exceptions
"""


class AccountInexistent(Exception):
    """
    Raised when account not exists
    """

    def __init__(self, message="Account Inexistent") -> None:
        self.message = message
        super().__init__(message)
