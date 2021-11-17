import logging

# importing somefunction from module
from logging_present.functions.functions import somefunction
from logging_present.settings import log_config

logging.basicConfig(**log_config)
logger = logging.getLogger(__name__)


logging.info("logging message")
logger.info("logger message")

# Calling somefunction and comparing output
somefunction()

# class CustomAdapter(logging.LoggerAdapter):
#    pass
