from hashlib import sha256


def generate_hash(password: str) -> str:
    sha256_algoritm = sha256()
    sha256_algoritm.update(bytes(password, encoding="utf-8"))
    return sha256_algoritm.hexdigest()
