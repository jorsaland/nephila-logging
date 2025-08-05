"""
Defines the logger manager used for general information.
"""


from datetime import timezone


from .._constants import GLOBAL_LOGGER_FORMAT, GLOBAL_LOGGER_NAME
from ._base_logger_manager import BaseLoggerManager


class GlobalLoggerManager(BaseLoggerManager):


    """
    Logger manager used for general information.
    """


    @classmethod
    def initialize(cls, *, logging_level: str, tzone: timezone):

        """
        Sets up the logger.
        """

        super().initialize(
            logger_name = GLOBAL_LOGGER_NAME,
            logger_format = GLOBAL_LOGGER_FORMAT,
            logging_level = logging_level,
            tzone = tzone,
        )