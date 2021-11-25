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
