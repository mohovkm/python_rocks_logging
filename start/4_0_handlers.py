import logging

# Logger (name) -> Handler -> Formatter
#               -> Filter

logger = logging.getLogger(__name__)
logger.info(...)

fmt = "%(levelname)s:%(name)s:%(message)s"

# Creating formatter

# Creating StreamHandler

# Adding handler to logger

# Describe why message prints twice
# try with propagate
