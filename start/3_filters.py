###
# About:  Filtering LogRecord by parameters, enreaching LogRecord by extra attributes
# Docs:   https://docs.python.org/3/library/logging.html#filter
# Output: Enabling/disabling output based on "login" extra parameter
###

import logging

# Format string with new keyword
logging.basicConfig(format="%(asctime)s - %(message)s - %(login)s - %(appname)s")
logger = logging.getLogger(__name__)
logger.setLevel("INFO")

# Create filter method enreach with appname, filter login
class ContextFilter(logging.Filter):
    def filter(self, record):
        pass


# Instantianting ContextFilter and attaching it to logger
