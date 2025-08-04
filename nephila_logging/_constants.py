"""
Defines the package constants.
"""


valid_loggin_levels = [
    LEVEL_DEBUG := 'DEBUG',
    LEVEL_INFO := 'INFO',
    LEVEL_WARNING := 'WARNING',
    LEVEL_ERROR := 'ERROR',
    LEVEL_CRITICAL := 'CRITICAL',
]

GLOBAL_LOGGER_NAME = 'GLOBAL-LOGGER'
GLOBAL_LOGGER_FORMAT = '='*100 + '\n%(asctime)s (%(levelname)s) %(name)s: %(message)s\n' + '='*100

CONTROLLER_LOGGER_NAME = 'CONTROLLER-LOGGER'
CONTROLLER_LOGGER_FORMAT = '-'*100 + '\n%(asctime)s (%(levelname)s) %(name)s:\n%(message)s\n' + '-'*100