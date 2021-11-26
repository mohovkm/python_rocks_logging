from os import getenv

LOGLEVEL = getenv("LOGLEVEL", "INFO")
FORMAT = "%(name)s:%(levelname)s: %(asctime)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%I:%S"

log_config = {
    "format": FORMAT,
    "level": LOGLEVEL,
    "datefmt": DATE_FORMAT,
}
