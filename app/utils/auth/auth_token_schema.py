
from pydantic import BaseModel, Field


class AuthTokenSchema(BaseModel):
    """
    AuthTokenSchema Schema
    """

    token: str = Field(example="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJudW1iZXIiOjMxNTAwNywicGFzc3dvcmQiOiIxMjMxMjMifQ.7AZ8q_Bk0o_3wopTU8QNwruYuoMbCPigRVJFSx8mFgI")
