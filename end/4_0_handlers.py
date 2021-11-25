import logging

# Logger (name) -> Handler -> Formatter
#               -> Filter

logger = logging.getLogger(__name__)
logger.info(...)

fmt = "%(levelname)s:%(name)s:%(message)s"

# Creating formatter
fmt = logging.Formatter(fmt)

# Creating StreamHandler
sh = logging.StreamHandler()
sh.setFormatter(fmt)

# Adding handler to logger
logger.addHandler(sh)
logger.setLevel("WARNING")

# Describe why message prints twice
# try with propagate
logger.propagate = False
logging.warning("warn message")
logger.warning("warn message")
