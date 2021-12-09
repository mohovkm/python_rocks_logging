# Python logging module presentation based on [python docs](https://docs.python.org/3/library/logging.html)

## About me:
- **Name**: Konstantin Mokhov
- **Position**: Team Lead
- **Company**: EPAM
- **LinkedIn**: <https://www.linkedin.com/in/konstantin-mohov>
- **Telegram**: 
    - [me](https://t.me/mohovkm)
    - [Python Rocks](https://t.me/python_rocks)
- **Speech**:
    - format: live coding
    - url: 
        - <https://github.com/mohovkm/python_rocks_logging>
        - <https://github.com/mohovkm/epam_pymeetup_2021>

## Topics:
- [Basic config](https://docs.python.org/3/library/logging.html#logging.basicConfig)
- [Extra parameters](https://docs.python.org/3/howto/logging-cookbook.html#using-loggeradapters-to-impart-contextual-information)
- [Filters](https://docs.python.org/3/library/logging.html#filter)
- [Handlers](https://docs.python.org/3/howto/logging-cookbook.html#multiple-handlers-and-formatters)
  - [Socket listener / Socket handler](https://docs.python.org/3/howto/logging-cookbook.html#network-logging)
  - [RotationFileHandler](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.RotatingFileHandler)
- [Optimization](https://docs.python.org/3/howto/logging.html#optimization)
- [Exception info](https://docs.python.org/3/library/logging.html#logging.Logger.debug)

### Requirements:
- python = "^3.7"
- [poetry](https://python-poetry.org/)

### How to run examples:
```bash
poetry install
poetry shell
cd end
python -m 1_basic_config
```

## Conclusions:
- Use `getLogger` to instantiate logger in your module and `__name__` as a logger name.
- Use `basicConfig` to provide configuration across all loggers.
- Use `extra` keyword to provide extra parameters for your logger.
- Use `LoggerAdapter` or custom adapters to provide default extra arguments or change LogRecord.
- Use filters to filter LogRecord or enreach it with some data.
- Most likely you don't need to invent a new Handler, use existing one.
- Don't use f-strings in logger.
- Use `exc_info` keyword to add traceback into LogRecord.
- [**Join EPAM to grow and succeed**](https://www.epam.com/careers)

