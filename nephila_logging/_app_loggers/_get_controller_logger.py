"""
Defines the function that retrieves the logger used to register endpoint calls.
"""


from datetime import timezone


from ._build_logger import build_logger

from .._constants import CONTROLLER_LOGGER_NAME, CONTROLLER_LOGGER_FORMAT

from .._validations._validate_logging_level import validate_logging_level
from .._validations._validate_timezone import validate_timezone


def get_controller_logger(logging_level: str, tzone: timezone):

    """
    Retrieves the logger used to register endpoint calls.
    """

    validate_logging_level(logging_level)
    validate_timezone(tzone)

    return build_logger(
        logger_name = CONTROLLER_LOGGER_NAME,
        logger_format = CONTROLLER_LOGGER_FORMAT,
        logging_level = logging_level,
        tzone = tzone,
    )