###
# About:  Logging with extra parameters, extra by default, changing and formatting output.
# Docs:   https://docs.python.org/3/howto/logging-cookbook.html#using-loggeradapters-to-impart-contextual-information
#         https://docs.python.org/3/library/logging.html#logging.debug
# Output: 2021-12-07 11:20:24,328 - message from adapter 1 - football 
#         2021-12-07 11:21:44,488 - [original: some message; client_ip: localhost; appname: football]
#         2021-12-07 11:21:44,488 - [original: some message; client_ip: localhost; appname: None]
###

import logging
from typing import Dict, Tuple

# Example of config with new keyword argument
logging.basicConfig(
    format="%(asctime)s - %(message)s",
    level="INFO",
)
logger = logging.getLogger(__name__)

# Logging with extra


# Creating default LoggerAdapter with extra by default


# Creating CustomAdapter class to enreach logging data
class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg: str, kwargs: Dict) -> Tuple[str, Dict]:
        pass


# Instantiating Adapter

# Logging without and with extra
