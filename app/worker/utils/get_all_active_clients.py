"""
    Module for function to get all active clients
"""
from app.worker.utils.start_connection import start_connection_bus


def get_all_active_clients():
    connection = start_connection_bus()
    connection.connect()

    manager = connection.get_manager()
    queues = manager.get_queues("/")
    correct_queues = []
    for queue in queues:
        if len(queue["name"].split()) > 1:
            correct_queues.append(queue)
            
    return correct_queues
