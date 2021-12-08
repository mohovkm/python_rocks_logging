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
    format="%(asctime)s - %(message)s - %(appname)s",  # delete appname before creating custom adapter
    level="INFO",
)
logger = logging.getLogger(__name__)


# Creating default LoggerAdapter
adapter1 = logging.LoggerAdapter(logger, {"appname": "football"})
adapter1.info("message from adapter 1")


# Creating CustomAdapter class to enreach logging data
class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg: str, kwargs: Dict) -> Tuple[str, Dict]:
        client_ip = kwargs.pop("client_ip")
        appname = kwargs.pop("appname", None)
        return (
            "[original: %s; client_ip: %s; appname: %s]" % (msg, client_ip, appname),
            kwargs,
        )


# Instantiating Adapter
adapter2 = CustomAdapter(logger, {})

# Logging without and with extra
adapter2.info("some message", client_ip="localhost", appname="football")
adapter2.info("some message", client_ip="localhost")
