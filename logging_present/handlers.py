import logging

# Logger (name) -> Handler -> Formatter
#               -> Filter

logger = logging.getLogger(__name__)
logger.info(...)

fmt = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

sh = logging.StreamHandler()
sh.setFormatter(fmt)
sh.setLevel("INFO")

logger.addHandler(sh)
logger.setLevel("WARNING")

# Describe why message prints twice
# try with propagate
logging.warning("warn message")
logger.warning("warn message")
