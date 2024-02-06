import functools
import logging

logger = logging.getLogger("errors")
def loop(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> None:
        while True:
            result = func(*args, **kwargs)
            if result:
                return result

    return wrapper