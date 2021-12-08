###
# About:  Formatting of message arguments is deferred until it cannot be avoided.
#         Don't use f-strings. Executables will be executed.
# Docs:   https://docs.python.org/3/howto/logging.html#optimization
# Output: Observing behaviour of objects with logger module
###

import logging


class SomeObject:
    def __str__(self):
        pass


def doing_stuff():
    pass


logger = logging.getLogger(__name__)
logger.setLevel("INFO")

# creating SomeObject

# f-string approach and %-style approach

# Computing arguments passed to logger

# Checking current level with isEnabledFor
