"""
Global Django-Code-Framework exception and warning classes.
"""


class ImproperlyConfigured(Exception):
    """Django-Code-Framework is somehow improperly configured"""

    pass


class AppRegistryNotReady(Exception):
    """The django_code_framework.apps registry is not populated yet"""

    pass
