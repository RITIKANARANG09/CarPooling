from functools import wraps
import sqlite3
from src.Exceptions.not_found_error import NotFoundError
from src.Exceptions.duplicate_error import DuplicateError
import logging
logger = logging.getLogger(__name__)
def errorhandler(func) :
    """
    Decorator function for handling sqlite3 exceptions happening in project.
    Parameter -> function: Callable
    Return type -> wrapper: Callable
    """

    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> None:
        """
            Wrapper function for executing the function and handling exception whenever occur.
            Parameter -> *args: tuple, **kwargs: dict
            Return type -> None
        """
        try:
            return func(*args, **kwargs)
        # except RangeError as error:
        #     logger.exception(error.message)
        #     print(error.message)
        except NotFoundError as error:
            logger.exception(error.message)
            print(error.message)
        except DuplicateError as error:
            logger.exception(error.message)
            print(error.message)
        # except sqlite3.IntegrityError as error:
        #     logger.exception(error)
        #     print(Prompts.INTEGRITY_ERROR_MESSAGE)
        # except sqlite3.OperationalError as error:
        #     logger.exception(error)
        #     print(Prompts.OPERATIONAL_ERROR_MESSAGE + "\n")
        # except sqlite3.ProgrammingError as error:
        #     logger.exception(error)
        #     print(Prompts.PROGRAMMING_ERROR_MESSAGE + "\n")
        # except sqlite3.Error as error:
        #     logger.exception(error)
        #     print(Prompts.GENERAL_EXCEPTION_MESSAGE + "\n")
        # except Exception as error:
        #     logger.exception(error)
        #     print(Prompts.GENERAL_EXCEPTION_MESSAGE + "\n")

    return wrapper