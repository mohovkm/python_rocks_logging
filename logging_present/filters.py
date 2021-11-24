import logging
from typing import Dict

# Format string with new keyword
logging.basicConfig(format="%(asctime)s - %(message)s - %(login)s - %(appname)s")
logger = logging.getLogger(__name__)

# Set logger level
logger.setLevel("INFO")

# Inspect errors
logging.info("logging message")  # will not be printed
# Enreach with extra
logger.info("logger message", extra={"login": "admin", "appname": "myapp"})


class ContextFilter(logging.Filter):
    def filter(self, record: Dict[str, str]):
        record.appname = "logging_app"
        if hasattr(record, "password"):
            return False

        record.attention = "true"
        return True


ft = ContextFilter()
logger.addFilter(ft)
logger.info("some message", extra={"password": "qwerty", "login": "admin"})
logger.info("some message", extra={"login": "root"})
