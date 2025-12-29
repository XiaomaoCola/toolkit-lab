"""
Cross-platform mouse driver using PyAutoGUI

This driver works on all platforms but may have lower performance
compared to native implementations.
"""

import time
import pyautogui
from interaction_mouse.models import Point, Button
from interaction_mouse.errors import DriverError


class PyAutoGUIDriver:
    """
    Cross-platform mouse driver using PyAutoGUI.

    This is a fallback driver that works on Windows, macOS, and Linux
    but may have lower performance than platform-specific drivers.
    """

    def __init__(self) -> None:
        """Initialize the PyAutoGUI driver."""
        # Disable PyAutoGUI's fail-safe feature for better control
        pyautogui.FAILSAFE = False
        # Set a minimal pause between PyAutoGUI commands
        pyautogui.PAUSE = 0.0

    def move_to(self, point: Point, duration: float = 0.0) -> None:
        """
        Move the mouse cursor to a specific position.

        Args:
            point: Target position
            duration: Time in seconds to complete the movement
        """
        try:
            pyautogui.moveTo(point.x, point.y, duration=duration)
        except Exception as e:
            raise DriverError(f"Failed to move mouse: {e}")

    def press(self, button: Button = "left") -> None:
        """
        Press a mouse button down without releasing.

        Args:
            button: Which button to press
        """
        try:
            pyautogui.mouseDown(button=self._map_button(button))
        except Exception as e:
            raise DriverError(f"Failed to press mouse button: {e}")

    def release(self, button: Button = "left") -> None:
        """
        Release a pressed mouse button.

        Args:
            button: Which button to release
        """
        try:
            pyautogui.mouseUp(button=self._map_button(button))
        except Exception as e:
            raise DriverError(f"Failed to release mouse button: {e}")

    def click(self, button: Button = "left") -> None:
        """
        Perform a complete click (press and release).

        Args:
            button: Which button to click
        """
        try:
            pyautogui.click(button=self._map_button(button))
        except Exception as e:
            raise DriverError(f"Failed to click mouse button: {e}")

    def get_position(self) -> Point:
        """
        Get the current mouse cursor position.

        Returns:
            Current cursor position
        """
        try:
            x, y = pyautogui.position()
            return Point(x=x, y=y)
        except Exception as e:
            raise DriverError(f"Failed to get cursor position: {e}")

    def _map_button(self, button: Button) -> str:
        """
        Map our Button type to PyAutoGUI's button names.

        Args:
            button: Our button type

        Returns:
            PyAutoGUI button name
        """
        # PyAutoGUI uses the same names, but we validate here
        if button not in ("left", "right", "middle"):
            raise ValueError(f"Invalid button: {button}")
        return button
