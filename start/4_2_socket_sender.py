###
# About:  Creating SocketHandler to send log event across network
# Docs:   https://docs.python.org/3/howto/logging-cookbook.html#network-logging
# Output: No output, as LogRecord will be send through the network.
###

import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel("INFO")

# Create SockerHandler

# Log 10 records
