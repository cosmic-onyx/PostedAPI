import logging
import functools


logger = logging.getLogger('utils')


def error_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            logger.info(f"Success: {func.__name__} - {response}")

            return response
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            raise e

    return wrapper