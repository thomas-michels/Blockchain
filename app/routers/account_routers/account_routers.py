"""
    Module for all Account routers
"""

from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.crud.account import AccountServices, SimpleAccountSchema, StandardAccountSchema
from app.utils import AuthTokenSchema, LoginSchema, JWTBearer
from app.configs import get_environment
from app.exceptions import AccountInexistent
from app.crud.client import ClientServices

router = APIRouter()
_env = get_environment()
__services = AccountServices()


@router.post("/accounts/", tags=["accounts"], response_model=StandardAccountSchema)
def create_new_account(account: SimpleAccountSchema):
    response = __services.create_account(account)
    account_serialized = response.dict()
    account_serialized["creation_date"] = account_serialized["creation_date"].__str__()
    return JSONResponse(content=account_serialized)


@router.get(
    "/accounts/",
    tags=["accounts"],
    response_model=List[StandardAccountSchema],
    dependencies=[Depends(JWTBearer())],
)
async def get_all_accounts():
    response = __services.get_all_accounts()
    accounts = []
    for account in response:
        account_serialized = account.dict()
        account_serialized["balance"] = len(account_serialized["balance"]) / _env.BALANCE_CONVERTER
        account_serialized["creation_date"] = account_serialized[
            "creation_date"
        ].__str__()
        accounts.append(account_serialized)
    return JSONResponse(content=accounts)


@router.get(
    "/accounts/{number}",
    tags=["accounts"],
    response_model=StandardAccountSchema,
    dependencies=[Depends(JWTBearer())],
)
async def get_account_by_number(number: int):
    response = __services.get_by_number(number)
    account_serialized = response.dict()
    account_serialized["balance"] = len(account_serialized["balance"]) / _env.BALANCE_CONVERTER
    account_serialized["creation_date"] = account_serialized["creation_date"].__str__()
    return JSONResponse(content=account_serialized)


@router.post("/login/", tags=["login"], response_model=AuthTokenSchema)
async def login(login: LoginSchema):
    try:
        response = __services.login(login)
        if response:
            return JSONResponse(content=response.dict())

        return JSONResponse(status_code=400, content="Account number or password invalid")

    except AccountInexistent:
        return JSONResponse(status_code=404, content=f"Account with number {login.number} not exists")
