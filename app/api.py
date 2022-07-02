"""
    Module for API
"""

from fastapi import FastAPI
from app.routers import accounts_router, transaction_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(accounts_router)
app.include_router(transaction_router)


def run_server():
    uvicorn.run(app, host="0.0.0.0", port=8000)
