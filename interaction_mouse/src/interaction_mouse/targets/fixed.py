"""
Fixed point target strategy

This module provides a simple strategy that always returns the same point.
"""

from interaction_mouse.models import Point


class FixedTarget:
    """
    A target strategy that always returns the same fixed point.

    This is the simplest targeting strategy, useful for clicking
    at precise, predetermined locations.
    """

    def __init__(self, point: Point):
        """
        Initialize a fixed target.

        Args:
            point: The fixed point to always return
        """
        self.point = point

    def get_target(self) -> Point:
        """
        Get the target point.

        Returns:
            The fixed point specified during initialization
        """
        return self.point

    def __str__(self) -> str:
        return f"FixedTarget({self.point})"
