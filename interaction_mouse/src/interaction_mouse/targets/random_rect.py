"""
Random rectangle target strategy

This module provides a strategy that returns random points within a rectangle.
"""

import random
from interaction_mouse.models import Point, Rect
from interaction_mouse.errors import InvalidTargetError


class RandomRectTarget:
    """
    A target strategy that returns random points within a rectangle.

    This is useful for avoiding detection in automation or for testing
    different areas within a region.
    """

    def __init__(self, rect: Rect):
        """
        Initialize a random rectangle target.

        Args:
            rect: The rectangle within which to generate random points

        Raises:
            InvalidTargetError: If the rectangle has invalid dimensions
        """
        if rect.width <= 0 or rect.height <= 0:
            raise InvalidTargetError(
                f"Rectangle must have positive dimensions: {rect}"
            )
        self.rect = rect

    def get_target(self) -> Point:
        """
        Get a random target point within the rectangle.

        Returns:
            A random point within the rectangle bounds
        """
        x = random.randint(self.rect.x, self.rect.x + self.rect.width - 1)
        y = random.randint(self.rect.y, self.rect.y + self.rect.height - 1)
        return Point(x=x, y=y)

    def __str__(self) -> str:
        return f"RandomRectTarget({self.rect})"
