###
# About:  Configuring logger with basicConfig, difference between logging and logger.
#         Loggers should NEVER be instantiated directly, but always through the module-level function:
#         logging.getLogger(name)
# Docs:   https://docs.python.org/3/library/logging.html#logging.basicConfig
#         https://docs.python.org/3/library/logging.html#logger-objects
# Output: Different logger name, same format.
###

import logging

# importing somefunction from module
from end.functions.functions import somefunction
from end.settings import log_config

# Configuring with basic config
logging.basicConfig(**log_config)
logger = logging.getLogger(__name__)

# Logging data
logging.info("logging message")
logger.info("logger message")

# Calling somefunction and comparing output
somefunction()
