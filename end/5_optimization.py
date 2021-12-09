###
# About:  Formatting of message arguments is deferred until it cannot be avoided.
#         Don't use f-strings. Executables will be executed.
# Docs:   https://docs.python.org/3/howto/logging.html#optimization
# Output: Observing behaviour of objects with logger module
###

import logging


class SomeObject:
    def __str__(self):
        print("here we are using print instead of logging in str call :( ")
        return "formatted str"


def doing_stuff():
    print("we are doing some stuff")
    # sleep(2)
    print("and only then return")
    return "some statement"


logger = logging.getLogger(__name__)
logger.setLevel("INFO")

s = SomeObject()
logger.debug(f"f-string approach: {s}")
logger.debug("%s percent style approach", s)

logger.debug("%s percent style with function", doing_stuff())

if logger.isEnabledFor(logging.DEBUG):
    logger.debug("this is the message with checking current level", doing_stuff())
