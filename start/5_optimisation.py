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
