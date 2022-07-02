"""JWT token verifier"""
import time
from typing import Dict, Optional, Tuple
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from jwt.exceptions import DecodeError
from app.configs import get_environment

_env = get_environment()


def decode_jwt(token: str) -> Optional[dict]:
    """Decode JWT token"""
    try:
        decoded_token = jwt.decode(
            token,
            _env.JWT_SECRET,
            algorithms=[_env.JWT_ALGORITHM],
            options={"verify_aud": False},
        )
        # if (
        #     "expires" in decoded_token
        #     and decoded_token["expires"] >= time.time()
        #     or "exp" in decoded_token
        #     and decoded_token["exp"]
        # ):
        return decoded_token
        # return None
    except DecodeError:
        return {}


class JWTBearer(HTTPBearer):
    """JWT Bearer token"""

    def __init__(self, auto_error: bool = True):
        super(__class__, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            __class__, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            is_toke_valid, decoded_token = self.verify_jwt(credentials.credentials)
            if not is_toke_valid:
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            return decoded_token["number"]

        raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> Tuple[bool, Dict]:
        """Verify JWT token"""
        is_token_valid: bool = False

        try:
            payload = decode_jwt(jwtoken)
        except DecodeError:
            payload = None
        if payload:
            is_token_valid = True
        return is_token_valid, payload
