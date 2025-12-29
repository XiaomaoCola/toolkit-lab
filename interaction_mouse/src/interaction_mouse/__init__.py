"""
Interaction Mouse - A flexible mouse interaction library

This package provides a clean and extensible interface for mouse automation
with support for multiple backends and human-like behavior simulation.
"""

from interaction_mouse.models import Point, Rect, Button
from interaction_mouse.clicker import Clicker
from interaction_mouse.errors import (
    InteractionMouseError,
    DriverError,
    InvalidTargetError,
    ActionError,
)

__version__ = "0.1.0"
__all__ = [
    # Main interface
    "Clicker",
    # Models
    "Point",
    "Rect",
    "Button",
    # Errors
    "InteractionMouseError",
    "DriverError",
    "InvalidTargetError",
    "ActionError",
]
