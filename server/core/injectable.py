from functools import wraps
from dependency_injector.wiring import inject as injection
from loguru import logger
from server.core.services import BaseService

def injectable(func):
    @injection
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        injected_services = [arg for arg in kwargs.values() if isinstance(arg, BaseService)]
        if len(injected_services) == 0:
            return response
        else:
            try:
                injected_services[-1].close_scoped_session()
            except Exception as exception:
                logger.error(exception)

        return response

    return wrapper
