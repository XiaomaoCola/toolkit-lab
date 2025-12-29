"""
Mouse driver implementations

This module contains different backend implementations for mouse control.
"""

from interaction_mouse.protocol import IMouseDriver

try:
    from interaction_mouse.drivers.win32 import Win32Driver
    HAS_WIN32 = True
except ImportError:
    HAS_WIN32 = False
    Win32Driver = None  # type: ignore

from interaction_mouse.drivers.pyautogui import PyAutoGUIDriver


def get_default_driver() -> IMouseDriver:
    """
    Get the best available driver for the current platform.

    Returns:
        IMouseDriver: Win32Driver on Windows if available, otherwise PyAutoGUIDriver
    """
    if HAS_WIN32:
        return Win32Driver()
    return PyAutoGUIDriver()


__all__ = [
    "IMouseDriver",
    "Win32Driver",
    "PyAutoGUIDriver",
    "get_default_driver",
    "HAS_WIN32",
]
