"""
Windows-specific mouse driver using Win32 API (SendInput)

This driver provides native Windows mouse control with better performance
and reliability than cross-platform alternatives.
"""

import time
import ctypes
from ctypes import wintypes
from typing import Optional

from interaction_mouse.models import Point, Button
from interaction_mouse.errors import DriverError

# Win32 API constants
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040

INPUT_MOUSE = 0


class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.POINTER(wintypes.ULONG)),
    ]


class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [("mi", MOUSEINPUT)]

    _anonymous_ = ("_input",)
    _fields_ = [("type", wintypes.DWORD), ("_input", _INPUT)]


class Win32Driver:
    """
    Mouse driver implementation using Windows SendInput API.

    This provides direct, low-level mouse control on Windows platforms.
    """

    def __init__(self) -> None:
        """Initialize the Win32 driver."""
        try:
            self.user32 = ctypes.windll.user32
            # Test if we can access the required functions
            self.user32.GetCursorPos
            self.user32.SendInput
        except AttributeError as e:
            raise DriverError(f"Failed to initialize Win32 driver: {e}")

    def _get_screen_dimensions(self) -> tuple[int, int]:
        """Get the screen dimensions."""
        width = self.user32.GetSystemMetrics(0)  # SM_CXSCREEN
        height = self.user32.GetSystemMetrics(1)  # SM_CYSCREEN
        return width, height

    def _to_absolute_coords(self, point: Point) -> tuple[int, int]:
        """Convert screen coordinates to absolute coordinates for SendInput."""
        screen_width, screen_height = self._get_screen_dimensions()
        # Absolute coordinates are in the range 0-65535
        abs_x = int(point.x * 65535 / screen_width)
        abs_y = int(point.y * 65535 / screen_height)
        return abs_x, abs_y

    def move_to(self, point: Point, duration: float = 0.0) -> None:
        """
        Move the mouse cursor to a specific position.

        Args:
            point: Target position
            duration: Time in seconds to complete the movement (approximated with steps)
        """
        if duration > 0:
            # Smooth movement with intermediate steps
            start = self.get_position()
            steps = max(10, int(duration * 60))  # 60 steps per second
            delay = duration / steps

            for i in range(1, steps + 1):
                # Linear interpolation
                t = i / steps
                intermediate = Point(
                    x=int(start.x + (point.x - start.x) * t),
                    y=int(start.y + (point.y - start.y) * t),
                )
                self._move_immediate(intermediate)
                time.sleep(delay)
        else:
            self._move_immediate(point)

    def _move_immediate(self, point: Point) -> None:
        """Move cursor immediately to position."""
        abs_x, abs_y = self._to_absolute_coords(point)

        input_struct = INPUT()
        input_struct.type = INPUT_MOUSE
        input_struct.mi.dx = abs_x
        input_struct.mi.dy = abs_y
        input_struct.mi.dwFlags = MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE
        input_struct.mi.time = 0
        input_struct.mi.dwExtraInfo = None

        result = self.user32.SendInput(1, ctypes.byref(input_struct), ctypes.sizeof(INPUT))
        if result == 0:
            raise DriverError("Failed to move mouse cursor")

    def press(self, button: Button = "left") -> None:
        """Press a mouse button down."""
        flags = self._get_press_flag(button)
        self._send_button_event(flags)

    def release(self, button: Button = "left") -> None:
        """Release a mouse button."""
        flags = self._get_release_flag(button)
        self._send_button_event(flags)

    def click(self, button: Button = "left") -> None:
        """Perform a complete click (press and release)."""
        self.press(button)
        self.release(button)

    def _send_button_event(self, flags: int) -> None:
        """Send a button event with the specified flags."""
        input_struct = INPUT()
        input_struct.type = INPUT_MOUSE
        input_struct.mi.dwFlags = flags
        input_struct.mi.time = 0
        input_struct.mi.dwExtraInfo = None

        result = self.user32.SendInput(1, ctypes.byref(input_struct), ctypes.sizeof(INPUT))
        if result == 0:
            raise DriverError("Failed to send mouse button event")

    def _get_press_flag(self, button: Button) -> int:
        """Get the flag for pressing a button."""
        if button == "left":
            return MOUSEEVENTF_LEFTDOWN
        elif button == "right":
            return MOUSEEVENTF_RIGHTDOWN
        elif button == "middle":
            return MOUSEEVENTF_MIDDLEDOWN
        else:
            raise ValueError(f"Invalid button: {button}")

    def _get_release_flag(self, button: Button) -> int:
        """Get the flag for releasing a button."""
        if button == "left":
            return MOUSEEVENTF_LEFTUP
        elif button == "right":
            return MOUSEEVENTF_RIGHTUP
        elif button == "middle":
            return MOUSEEVENTF_MIDDLEUP
        else:
            raise ValueError(f"Invalid button: {button}")

    def get_position(self) -> Point:
        """Get the current mouse cursor position."""
        point = wintypes.POINT()
        result = self.user32.GetCursorPos(ctypes.byref(point))
        if not result:
            raise DriverError("Failed to get cursor position")
        return Point(x=point.x, y=point.y)
