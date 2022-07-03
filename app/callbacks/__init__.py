"""
    Module for callbacks
"""
from app.callbacks.blocks_callbacks import RegisterBlockCallback, SendBlocksToConsumers
from app.callbacks.register_client_callbacks import RegisterClientCallback
from app.callbacks.tokens_callbacks import SendTokensToAccount
from app.callbacks.transactions_callbacks import CreateTransactionCallback
from app.callbacks.account_callbacks import AccountBalanceCallback, RegisterAccountCallback
from app.callbacks.event_callbacks import EventReceiverCallback
from app.callbacks.election_callbacks import ElectionCallback
