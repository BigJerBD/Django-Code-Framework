"""
Default Django-Code-Framework settings. Override these with settings in the module pointed to
by the DJANGOCF_SETTINGS_MODULE environment variable.
"""

####################
# CORE             #
####################

DEBUG = False

INSTALLED_APPS = []

# The callable to use to configure logging
LOGGING_CONFIG = "logging.config.dictConfig"

# Custom logging configuration.
LOGGING = {}
