import logging
from typing import Dict, Tuple

# Example of config with new keyword argument
logging.basicConfig(
    format="%(asctime)s - %(message)s - %(appname)s",
    level="INFO",
)
logger = logging.getLogger(__name__)


# Creating default LoggerAdapter
adapter1 = logging.LoggerAdapter(logger, {"appname": "football"})
adapter1.info("message from adapter 1")


# Creating CustomAdapter class to enreach logging data
class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg: str, kwargs: Dict) -> Tuple[str, Dict]:
        client_ip = None
        if "client_ip" in kwargs:
            client_ip = kwargs.pop("client_ip")

        return (
            "[original: %s, kwargs: %s, client_ip: %s]" % (msg, kwargs, client_ip),
            kwargs,
        )


# Instantiating Adapter
adapter2 = CustomAdapter(logger, {"client_ip": None})

# Logging without and with extra
adapter2.info("message without extra")
adapter2.info("message with extra", client_ip="localhost")
