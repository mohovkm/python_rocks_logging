###
# About:  Creating RotatingFileHandler and observing it behaviour.
# Docs:   https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler
# Output: 5 files with log records in specified directory.
###

import logging
import logging.handlers

fmt = "%(asctime)s - %(levelname)s - %(message)s"

# Creating RotatingFileHandler
h = logging.handlers.RotatingFileHandler(
    "/tmp/python_logging/log.log",
    maxBytes=53,
    backupCount=5,
)
# Setting Formatter
h.setFormatter(logging.Formatter(fmt))

# Setting up logger
logger = logging.getLogger(__name__)
logger.setLevel("INFO")

# Adding handler
logger.addHandler(h)

# Performing actions
for i in range(100):
    logger.info("one interesting thing %d", i)
