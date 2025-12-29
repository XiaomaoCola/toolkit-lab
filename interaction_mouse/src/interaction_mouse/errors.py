"""
Custom exception classes for the interaction_mouse library
"""


class InteractionMouseError(Exception):
    """Base exception for all interaction_mouse errors"""

    pass


class DriverError(InteractionMouseError):
    """Raised when a mouse driver operation fails"""

    pass


class InvalidTargetError(InteractionMouseError):
    """Raised when a target position or area is invalid"""

    pass


class ActionError(InteractionMouseError):
    """Raised when a mouse action fails to execute"""

    pass


class ConfigurationError(InteractionMouseError):
    """Raised when there's an issue with configuration"""

    pass
