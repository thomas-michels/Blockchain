"""
Inicialize application
"""

from app.db import MongoDB
from app import Application

if __name__ == "__main__":
    MongoDB()
    Application()
