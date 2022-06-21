from app.worker.producer import KombuProducer
from app.utils import generate_event

KombuProducer.send_messages(
    generate_event("aa", "MALIK MARTINEZ", {"data": ["teste"], "nonce": 1234})
)
