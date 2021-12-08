###
# About:  Creating SocketHandler to send log event across network
# Docs:   https://docs.python.org/3/howto/logging-cookbook.html#network-logging
# Output: No output, as LogRecord will be send through the network.
###

import logging
import logging.handlers

logger = logging.getLogger(__name__)

# Create SockerHandler
sh = logging.handlers.SocketHandler(
    "localhost",
    logging.handlers.DEFAULT_TCP_LOGGING_PORT,
)

logger.addHandler(sh)
logger.setLevel("INFO")

# Log 10 records
for i in range(10):
    logger.info("hi from another app %d" % i)
