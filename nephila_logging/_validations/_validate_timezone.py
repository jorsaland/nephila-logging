"""
Defines the function that validates the input timezone.
"""


from datetime import timezone


def validate_timezone(tzone):

    """
    Validates the input timezone.
    """

    if not isinstance(tzone, timezone):
        raise TypeError(f'A datetime.timezone instance is expected as tzone.')