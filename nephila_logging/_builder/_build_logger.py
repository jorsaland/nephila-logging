"""
Defines the function that builds a logger.
"""


from datetime import datetime, timezone
import logging
import os


from ._app_formatter import build_app_formatter
from ._app_handler import build_app_handler


def build_logger(*, logger_name: str, logger_format: str, logging_level: str, tzone: timezone):

    """
    Builds a logger.
    """

    os.makedirs('logs/', exist_ok=True)

    logger = logging.getLogger(logger_name)

    AppFormatter = build_app_formatter(tzone)
    AppHandler = build_app_handler(tzone)

    formatter = AppFormatter(logger_format)
    handler = AppHandler(
        filename = 'logs/.log',
        when= "midnight",
        interval = 1,
        backupCount = 0,
        encoding = "utf-8",
    )
    
    handler.namer = (lambda _: f'logs/{datetime.now(tzone)}.log')
    handler.setFormatter(formatter)

    logger.setLevel(logging_level.upper())
    logger.addHandler(handler)
    
    return logger