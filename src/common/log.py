import os
from logging import getLogger, config

logger = getLogger('api-logger')

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            'format': '%(levelname)s %(message)s'
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    },
    "loggers": {
        "api-logger": {
            "handlers": ["default"],
            "level": os.environ.get("LOG_LEVEL")
        },
    },
}

config.dictConfig(log_config)

logger = getLogger('api-logger')
