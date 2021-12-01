import logging
from typing import Any

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def to_int(obj: Any):
    int(obj)


# try-except with exc_info
# compare with sys
