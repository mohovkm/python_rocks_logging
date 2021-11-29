import logging

# Format string with new keyword
logging.basicConfig(format="%(asctime)s - %(message)s - %(login)s - %(appname)s")
logger = logging.getLogger(__name__)
logger.setLevel("INFO")

# Inspect errors
logging.info("logging message")  # will not be printed
logger.info("some message")


# Create filter method enreach with appname, filter login
class ContextFilter(logging.Filter):
    def filter(self, record):
        pass


# Instantianting ContextFilter and attaching it to logger
