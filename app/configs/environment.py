"""
Module to load all Environment variables
"""

from pydantic import BaseSettings


class Environment(BaseSettings):
    """
    Environment, add the variable and its type here matching the .env file
    """
    MONGODB_URI: str
    RBMQ_HOST: str
    RBMQ_USER: str
    RBMQ_PASS: str
    RBMQ_PORT: str
    RBMQ_VHOST: str
    RBMQ_EXCHANGE: str
    BLOCK_CHANNEL: str
    EVENT_CHANNEL: str
    ELECTION_CHANNEL: str
    REGISTER_CHANNEL: str
    VALIDATE_CHANNEL: str

    class Config:
        """Load config file"""

        env_file = ".env"
