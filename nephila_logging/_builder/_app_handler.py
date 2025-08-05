"""
Defines the custom logging handler used by the app offset and its builder function.
"""


from datetime import datetime, timedelta, timezone
from logging.handlers import TimedRotatingFileHandler


def build_app_handler(tzone: timezone):

    """
    Builds the AppHandler class with a timezone.
    """

    class AppHandler(TimedRotatingFileHandler):

        """
        Custom handler for logging to a file, rotating the log file at midnight, according to the app
        offset.
        """

        def computeRollover(self, currentTime: float):
            current_datetime = datetime.fromtimestamp(
                timestamp = currentTime,
                tz = tzone,
            )
            next_midnight = (
                current_datetime.replace(hour=0, minute=0, second=0, microsecond=0)
                + timedelta(days=1)
            )
            return next_midnight.timestamp()

    return AppHandler