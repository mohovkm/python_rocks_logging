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
