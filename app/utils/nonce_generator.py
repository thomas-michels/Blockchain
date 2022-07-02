from random import randint

def get_new_nonce() -> int:
    return randint(100, 900)
