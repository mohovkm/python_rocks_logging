###
# About:  Creating StreamHandler manually. Comparing with default-created.
# Docs:   https://docs.python.org/3/howto/logging-cookbook.html#multiple-handlers-and-formatters
# Output: WARNING:root:warn message
#         WARNING:__main__:warn message
###

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
