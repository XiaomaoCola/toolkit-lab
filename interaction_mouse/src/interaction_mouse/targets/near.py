"""
Near-point target strategy

This module provides a strategy that returns points near a center point
with some randomization for human-like behavior.
"""

import random
from interaction_mouse.models import Point
from interaction_mouse.errors import InvalidTargetError


class NearTarget:
    """
    A target strategy that returns points near a center point.

    This adds small random offsets to a center point, useful for
    simulating human-like imprecision in clicking.
    """

    def __init__(self, center: Point, max_offset: int = 5):
        """
        Initialize a near-point target.

        Args:
            center: The center point to target near
            max_offset: Maximum pixel offset in any direction (default: 5)

        Raises:
            InvalidTargetError: If max_offset is negative
        """
        if max_offset < 0:
            raise InvalidTargetError(
                f"max_offset must be non-negative, got: {max_offset}"
            )
        self.center = center
        self.max_offset = max_offset

    def get_target(self) -> Point:
        """
        Get a random point near the center.

        Returns:
            A point within max_offset pixels of the center in each direction
        """
        if self.max_offset == 0:
            return self.center

        offset_x = random.randint(-self.max_offset, self.max_offset)
        offset_y = random.randint(-self.max_offset, self.max_offset)

        return Point(
            x=self.center.x + offset_x,
            y=self.center.y + offset_y
        )

    def __str__(self) -> str:
        return f"NearTarget(center={self.center}, max_offset={self.max_offset})"
