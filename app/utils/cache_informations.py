from functools import lru_cache, wraps
from datetime import datetime, timedelta
from app.worker.producer import KombuProducer
from app.utils.event_generator import generate_event
from app.configs import get_environment, get_logger

_env = get_environment()
_logger = get_logger(name=__name__)


def timed_lru_cache(seconds: int):
    def wrapper_cache(func):
        func = lru_cache()(func)
        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime
        func.cache = []

        @wraps(func)
        def wrapped_func(*args, **kwargs):

            if datetime.utcnow() >= func.expiration:
                _logger.info("Cleaning cache")
                producer = KombuProducer()
                if func.cache:
                    event = generate_event(_env.EVENT_CHANNEL, {"data": func.cache})
                    producer.send_messages(event)
                
                func.cache = []
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            func.cache.append(args[1])
            return func(*args, **kwargs)

        return wrapped_func

    return wrapper_cache
