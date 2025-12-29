"""
Protocol definitions for mouse drivers

This module defines the interface that all mouse drivers must implement.
"""

from typing import Protocol
from interaction_mouse.models import Point, Button


class IMouseDriver(Protocol):
    """
    Protocol defining the interface for mouse drivers.

    All mouse driver implementations must provide these methods.
    """

    def move_to(self, point: Point, duration: float = 0.0) -> None:
        """
        Move the mouse cursor to a specific position.

        Args:
            point: Target position to move to
            duration: Time in seconds to complete the movement (0 for instant)
        """
        ...

    def press(self, button: Button = "left") -> None:
        """
        Press a mouse button down without releasing.

        Args:
            button: Which button to press ("left", "right", or "middle")
        """
        ...

    def release(self, button: Button = "left") -> None:
        """
        Release a pressed mouse button.

        Args:
            button: Which button to release ("left", "right", or "middle")
        """
        ...

    def click(self, button: Button = "left") -> None:
        """
        Perform a complete click (press and release).

        Args:
            button: Which button to click ("left", "right", or "middle")
        """
        ...

    def get_position(self) -> Point:
        """
        Get the current mouse cursor position.

        Returns:
            Current cursor position as a Point
        """
        ...
