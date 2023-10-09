import functools
import logging
import time

logger = logging.getLogger(__name__)


def timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        total = end - start
        logger.debug(f"Finished {func.__name__!r} in {total:.6f} ms")
        return value

    return wrapper_timer
