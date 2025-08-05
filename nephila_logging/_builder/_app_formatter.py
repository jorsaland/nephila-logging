"""
Defines the custom logging formatter used by the app offset and its builder function.
"""


from datetime import datetime, timezone
from logging import Formatter


def build_app_formatter(tzone: timezone):

    """
    Builds the AppFormatter class with a timezone.
    """

    class AppFormatter(Formatter):

        """
        Custom logging formatter which uses the app offset. 
        """

        converter = staticmethod(
            lambda timestamp, /: datetime.fromtimestamp(
                timestamp = timestamp,
                tz = tzone,
            )
            .timetuple()
        )

    return AppFormatter