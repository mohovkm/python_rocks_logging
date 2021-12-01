import logging
import sys
from typing import Any

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def to_int(obj: Any):
    int(obj)


try:
    to_int("vasya")
except ValueError as e:  # noqa W0612
    # logger.error("some error message", exc_info=True)
    e2 = sys.exc_info()
    logger.error("some error message", exc_info=e2)
