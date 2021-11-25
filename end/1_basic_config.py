import logging

# importing somefunction from module
from logging_present.functions.functions import somefunction
from logging_present.settings import log_config

# Configuring with basic config
logging.basicConfig(**log_config)
logger = logging.getLogger(__name__)

# Logging data
logging.info("logging message")
logger.info("logger message")

# Calling somefunction and comparing output
somefunction()
