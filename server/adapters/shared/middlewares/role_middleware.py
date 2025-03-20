from typing import List
from fastapi import Depends, Request

from server import dependencies
from server.core.exceptions import ErrorCodes, ExceptionHandler
from server.domain.entities.role_entity import EnumRole
from server.domain.services.role_service import RoleService


def role_middleware(required: List[EnumRole] = []):
    async def execute(
        req: Request, role_service: RoleService = Depends(dependencies.role_service)
    ) -> bool:
        if len(required) == 0:
            return True

        if not req.state.account:
            raise ExceptionHandler(
                code=ErrorCodes.NOT_FOUND, msg="Cannot find account in request"
            )

        enitiy = await role_service.find_one(req.state.account.id)
        if not enitiy:
            raise ExceptionHandler(
                code=ErrorCodes.FORBIDDEN, msg="Not enough permissions"
            )

        if enitiy.role not in required:
            return False

        return True

    return execute
