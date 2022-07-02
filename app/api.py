"""
    Module for API
"""

from fastapi import FastAPI
from app.routers import accounts_router, transaction_router
import uvicorn


app = FastAPI()
app.include_router(accounts_router)
app.include_router(transaction_router)


def run_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)
