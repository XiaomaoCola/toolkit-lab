"""
Core data models for mouse interactions

This module defines the fundamental data structures used throughout the library.
"""

from dataclasses import dataclass
from typing import Literal

Button = Literal["left", "right", "middle"]


@dataclass
class Point:
    """
    Represents a 2D point in screen coordinates.

    Attributes:
        x: The x-coordinate (horizontal position)
        y: The y-coordinate (vertical position)
    """

    x: int
    y: int

    def __str__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    def __repr__(self) -> str:
        return self.__str__()


@dataclass
class Rect:
    """
    Represents a rectangular area on the screen.

    Attributes:
        x: The x-coordinate of the top-left corner
        y: The y-coordinate of the top-left corner
        width: The width of the rectangle
        height: The height of the rectangle
    """

    x: int
    y: int
    width: int
    height: int

    @property
    def left(self) -> int:
        """Get the left edge x-coordinate"""
        return self.x

    @property
    def right(self) -> int:
        """Get the right edge x-coordinate"""
        return self.x + self.width

    @property
    def top(self) -> int:
        """Get the top edge y-coordinate"""
        return self.y

    @property
    def bottom(self) -> int:
        """Get the bottom edge y-coordinate"""
        return self.y + self.height

    @property
    def center(self) -> Point:
        """Get the center point of the rectangle"""
        return Point(
            x=self.x + self.width // 2,
            y=self.y + self.height // 2
        )

    def contains(self, point: Point) -> bool:
        """
        Check if a point is inside this rectangle.

        Args:
            point: The point to check

        Returns:
            True if the point is inside the rectangle, False otherwise
        """
        return (
            self.left <= point.x <= self.right
            and self.top <= point.y <= self.bottom
        )

    def __str__(self) -> str:
        return f"Rect(x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def __repr__(self) -> str:
        return self.__str__()
