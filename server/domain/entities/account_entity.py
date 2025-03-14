from pydantic import EmailStr

from server.core.types import string
from server.domain.entities.base_entity import BaseEntity

class AccountEntity(BaseEntity):
    username: string
    email: string
    avatar: string
    device_token: string

    @staticmethod
    def new(username: string, email: EmailStr, avatar: string, device_token: string):
        return AccountEntity(
            username=username,
            email=email,
            avatar=avatar,
            device_token=device_token
        )
