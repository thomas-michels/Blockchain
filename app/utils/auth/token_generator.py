import jwt
from app.configs import get_environment

_env = get_environment()


class JWTGenerator():
    "Generate Auth Bearer Shared Tokens"

    def generate_jwt_token(self, payload) -> str:
        """This function recieve payload and create a token"""
        token = jwt.encode(payload, _env.JWT_SECRET, _env.JWT_ALGORITHM)
        return token
