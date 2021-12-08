###
# About:  exc_info argument in the logging module. 
# Docs:   https://docs.python.org/3/library/logging.html#logging.Logger.debug
# Output: LogRecord with and without traceback
###

import logging
from typing import Any

logger = logging.getLogger(__name__)
logger.setLevel("INFO")


def to_int(obj: Any):
    int(obj)


# try-except with exc_info
# compare with sys
