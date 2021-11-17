import logging

from logging_present.settings import log_config

logging.basicConfig(**log_config)
logger = logging.getLogger(__name__)


logging.info("logging message")
logger.info("logger message")


class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return (
            "original: %s, kwargs: %s, client_ip: %s"
            % (msg, kwargs, self.extra["client_ip"]),
            kwargs,
        )


adapter = CustomAdapter(logger, {"client_ip": "locahost"})

adapter.info("message from adapter")
adapter.info("message with extra", extra={"appname": "football"})
logger.info("logger again")
