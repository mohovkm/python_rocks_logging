###
# About:  Creating RotatingFileHandler and observing it behaviour.
# Docs:   https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler
# Output: 5 files with log records in specified directory.
###

# import logging handlers

fmt = "%(asctime)s - %(levelname)s - %(message)s"

# Creating RotatingFileHandler

# Setting Formatter

# Setting up logger
logger = logging.getLogger(__name__)
logger.setLevel("INFO")

# Adding handler

# Performing 100 actions
