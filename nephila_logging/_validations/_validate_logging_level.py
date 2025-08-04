"""
Defines the function that validates the input logging level.
"""


from .._constants import valid_loggin_levels


def validate_logging_level(logging_level):

    """
    Validates the input logging level.
    """

    if not isinstance(logging_level, str):
        raise TypeError(f'A string is expected as logging level. Admited values are: {", ".join(valid_loggin_levels)}')
    
    if logging_level.upper() not in valid_loggin_levels:
        raise ValueError(f"Value '{logging_level}' is not admited. It should be one of these: {", ".join(valid_loggin_levels)}.")