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

if logger.isEnabledFor(logging.INFO):
    logger.info("this is the message with checking current level")
