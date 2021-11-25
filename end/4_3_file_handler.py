import logging
import logging.handlers

fmt = "%(asctime)s - %(levelname)s - %(message)s"

# Creating RotatingFileHandler
h = logging.handlers.RotatingFileHandler(
    "/tmp/python_logging/log.log",
    maxBytes=53,
    backupCount=5,
)
# Setting Formatter
h.setFormatter(logging.Formatter(fmt))

# Setting up logger
logger = logging.getLogger(__name__)
logger.setLevel("INFO")

# Adding handler
logger.addHandler(h)

# Performing actions
for i in range(100):
    logger.info("one interesting thing %d", i)
