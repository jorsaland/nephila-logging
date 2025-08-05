"""
Defines the logger manager used to register endpoint calls.
"""


from datetime import timezone


from .._constants import CONTROLLER_LOGGER_NAME, CONTROLLER_LOGGER_FORMAT
from ._base_logger_manager import BaseLoggerManager


class ControllerLoggerManager(BaseLoggerManager):


    """
    Logger manager used to register endpoint calls.
    """


    @classmethod
    def initialize(cls, *, logging_level: str, tzone: timezone):

        """
        Sets up the logger.
        """

        super().initialize(
            logger_name = CONTROLLER_LOGGER_NAME,
            logger_format = CONTROLLER_LOGGER_FORMAT,
            logging_level = logging_level,
            tzone = tzone,
        )