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

# Inspect errors
logging.info("logging message")  # will not be printed

# Enreach with extra
logger.info("logger message", extra={"login": "admin", "appname": "myapp"})


# Create filter method enreach with appname, filter login
class ContextFilter(logging.Filter):
    def filter(self, record):
        record.appname = "logging_app"
        return record.login != "root"


# Instantianting ContextFilter and attaching it to logger
ft = ContextFilter()
logger.addFilter(ft)
logger.info("some message", extra={"login": "admin"})
logger.info("some message", extra={"login": "root"})
