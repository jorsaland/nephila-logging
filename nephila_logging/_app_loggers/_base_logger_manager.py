"""
Defines the base logger manager from which other logger managers inherit.
"""


from datetime import timezone
from logging import Logger
import warnings


from .._builder._build_logger import build_logger

from .._validations._validate_logging_level import validate_logging_level
from .._validations._validate_timezone import validate_timezone


class BaseLoggerManager:


    """
    Base logger manager from which other logger managers inherit.
    """


    _logger: (Logger|None) = None


    def __new__(cls, *args, **kwargs):
        raise RuntimeError('Nephila app loggers are not instantiable.')


    @classmethod
    def initialize(cls, *, logger_name: str, logger_format: str, logging_level: str, tzone: timezone):

        """
        Sets up the logger. If it is already set, nothing happens.
        """

        validate_logging_level(logging_level)
        validate_timezone(tzone)

        if isinstance(cls._logger, Logger):
            return

        cls._logger = build_logger(
            logger_name = logger_name,
            logger_format = logger_format,
            logging_level = logging_level,
            tzone = tzone,
        )


    @classmethod
    def get(cls):

        """
        Retrieves the logger.
        """

        if cls._logger is None:
            raise RuntimeError('The logger has not been initialized yet.')

        return cls._logger