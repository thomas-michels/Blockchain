"""
    Module for transactions
"""

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.crud.transaction import (
    SimpleTransactionSchema,
    TransactionsServices,
    MiddleTransactionSchema,
)
from app.crud.account import AccountServices
from app.utils import JWTBearer
from app.exceptions import AccountInexistent, TransactionUnfonded
from app.configs import get_environment

router = APIRouter()
_env = get_environment()
__services = TransactionsServices()


@router.post(
    "/transference/", tags=["transactions"], dependencies=[Depends(JWTBearer())]
)
async def create_new_account(transaction: SimpleTransactionSchema):
    try:
        account_services = AccountServices()
        transaction.quantity = int(transaction.quantity * _env.BALANCE_CONVERTER)

        tokens = account_services.get_tokens_account(
            transaction.sender_number, transaction.quantity
        )
        transaction_schema = transaction.dict()
        transaction_schema["balance"] = tokens
        transaction_schema = MiddleTransactionSchema(**transaction_schema)
        transaction_saved = __services.create_transaction(transaction_schema)
        if transaction_saved:
            return JSONResponse(content="Transaction sended with success")

        return JSONResponse(status_code=400, content="Transaction not sended")

    except AccountInexistent:
        return JSONResponse(status_code=404, content="Account not found")

    except TransactionUnfonded:
        return JSONResponse(status_code=400, content="Transaction Unfonded")
