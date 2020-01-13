"""
Global Tusk exception and warning classes.
"""


class ImproperlyConfigured(Exception):
    """Tusk is somehow improperly configured"""

    pass


class AppRegistryNotReady(Exception):
    """The tusk.apps registry is not populated yet"""

    pass
