"""
Inicialize application
"""

from app.db import MongoDB
from app import run_server


if __name__ == "__main__":
    MongoDB()    
    run_server()
