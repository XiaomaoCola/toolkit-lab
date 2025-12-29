"""
Main facade interface for mouse interactions

This module provides the Clicker class, which serves as the primary
entry point for all mouse interaction functionality.
"""

from typing import Optional, Tuple, Union
from interaction_mouse.models import Point, Rect, Button
from interaction_mouse.protocol import IMouseDriver
from interaction_mouse.drivers import get_default_driver
from interaction_mouse.actions import (
    ClickAction,
    RepeatClickAction,
    RandomClickAction,
    DragAction,
)


class Clicker:
    """
    Main interface for mouse interactions.

    This class provides a simple facade for common mouse operations
    with support for customizable timing and behavior.

    Attributes:
        driver: The mouse driver implementation to use
        click_delay: Delay between press and release (float or (min, max) tuple)
        move_duration: Duration for mouse movements (float or (min, max) tuple)
    """

    def __init__(
        self,
        driver: Optional[IMouseDriver] = None,
        click_delay: Union[float, Tuple[float, float]] = 0.01,
        move_duration: Union[float, Tuple[float, float]] = 0.0,
    ):
        """
        Initialize a new Clicker instance.

        Args:
            driver: Mouse driver to use (defaults to platform-appropriate driver)
            click_delay: Delay between button press and release in seconds
            move_duration: Duration for mouse movements in seconds
        """
        self.driver = driver if driver is not None else get_default_driver()
        self.click_delay = click_delay
        self.move_duration = move_duration

    def click(self, point: Point, button: Button = "left") -> None:
        """
        Perform a single click at the specified position.

        Args:
            point: Target position to click
            button: Mouse button to use ("left", "right", or "middle")
        """
        action = ClickAction(
            driver=self.driver,
            click_delay=self.click_delay,
            move_duration=self.move_duration,
        )
        action.execute(point=point, button=button)

    def repeat_click(
        self,
        point: Point,
        count: int = 1,
        interval: float = 0.0,
        button: Button = "left",
    ) -> None:
        """
        Perform multiple clicks at the same position.

        Args:
            point: Target position to click
            count: Number of times to click
            interval: Time between clicks in seconds
            button: Mouse button to use
        """
        action = RepeatClickAction(
            driver=self.driver,
            click_delay=self.click_delay,
            move_duration=self.move_duration,
        )
        action.execute(point=point, count=count, interval=interval, button=button)

    def random_click(
        self,
        rect: Rect,
        count: int = 1,
        interval: float = 0.0,
        button: Button = "left",
    ) -> None:
        """
        Perform clicks at random positions within a rectangle.

        Args:
            rect: Rectangle area to click within
            count: Number of times to click
            interval: Time between clicks in seconds
            button: Mouse button to use
        """
        action = RandomClickAction(
            driver=self.driver,
            click_delay=self.click_delay,
            move_duration=self.move_duration,
        )
        action.execute(rect=rect, count=count, interval=interval, button=button)

    def drag(
        self,
        start: Point,
        end: Point,
        duration: float = 0.5,
        button: Button = "left",
    ) -> None:
        """
        Perform a drag operation from start to end position.

        Args:
            start: Starting position
            end: Ending position
            duration: Time to complete the drag in seconds
            button: Mouse button to use for dragging
        """
        action = DragAction(
            driver=self.driver,
            click_delay=self.click_delay,
            move_duration=self.move_duration,
        )
        action.execute(start=start, end=end, duration=duration, button=button)
