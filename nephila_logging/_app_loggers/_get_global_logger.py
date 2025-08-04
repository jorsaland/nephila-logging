"""
Defines the function that retrieves the logger used for general information.
"""


from datetime import timezone


from ._build_logger import build_logger

from .._constants import GLOBAL_LOGGER_NAME, GLOBAL_LOGGER_FORMAT

from .._validations._validate_logging_level import validate_logging_level
from .._validations._validate_timezone import validate_timezone


def get_global_logger(logging_level: str, tzone: timezone):

    """
    Retrieves the logger used for general information.
    """

    validate_logging_level(logging_level)
    validate_timezone(tzone)

    return build_logger(
        logger_name = GLOBAL_LOGGER_NAME,
        logger_format = GLOBAL_LOGGER_FORMAT,
        logging_level = logging_level,
        tzone = tzone,
    )