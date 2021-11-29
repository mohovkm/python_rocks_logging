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
