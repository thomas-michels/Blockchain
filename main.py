"""
Inicialize application
"""

import asyncio
from app.db import MongoDB
from app import Application, run_server


if __name__ == "__main__":
    MongoDB()
    worker = asyncio.new_event_loop()
    worker.run_in_executor(None, Application)
    
    api = asyncio.new_event_loop()
    api.run_in_executor(None, run_server)
