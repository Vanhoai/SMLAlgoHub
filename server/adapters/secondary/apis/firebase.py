from pydantic import BaseModel
from server.core.types import string

class OAuthClaims(BaseModel):
    name: string
    picture: string
    iss: string
    aud: string
    auth_time: int
    user_id: string
    sub: string
    iat: int
    exp: int
    email: string
    email_verified: bool
    uid: string
