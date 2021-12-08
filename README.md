# Logging module presentation based on [python docs](https://docs.python.org/3/library/logging.html)

### Requirements:
- python = "^3.7"
- poetry

### How to run examples:
```bash
poetry install
poetry shell
cd end
python -m 1_basic_config
```

## Topics:
- [Basic config](https://docs.python.org/3/library/logging.html#logging.basicConfig)
- [Extra parameters](https://docs.python.org/3/howto/logging-cookbook.html#using-loggeradapters-to-impart-contextual-information)
- [Filters](https://docs.python.org/3/library/logging.html#filter)
- [Handlers](https://docs.python.org/3/howto/logging-cookbook.html#multiple-handlers-and-formatters)
  - [Socket listener / Socket handler](https://docs.python.org/3/howto/logging-cookbook.html#network-logging)
  - [RotationFileHandler](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler)
- [Optimization](https://docs.python.org/3/howto/logging.html#optimization)
- [Exception info](https://docs.python.org/3/library/logging.html#logging.Logger.debug)

