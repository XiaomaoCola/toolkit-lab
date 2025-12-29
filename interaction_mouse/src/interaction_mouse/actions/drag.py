"""
Drag action implementation
"""

from typing import Union, Tuple
from interaction_mouse.models import Point, Button
from interaction_mouse.protocol import IMouseDriver
from interaction_mouse.timing import sleep, get_duration


class DragAction:
    """
    Action for performing drag operations from one point to another.
    """

    def __init__(
        self,
        driver: IMouseDriver,
        click_delay: Union[float, Tuple[float, float]] = 0.01,
        move_duration: Union[float, Tuple[float, float]] = 0.0,
    ):
        """
        Initialize a drag action.

        Args:
            driver: Mouse driver to use
            click_delay: Delay between press and release (not used in drag)
            move_duration: Duration for mouse movement (can be overridden in execute)
        """
        self.driver = driver
        self.click_delay = click_delay
        self.move_duration = move_duration

    def execute(
        self,
        start: Point,
        end: Point,
        duration: float = 0.5,
        button: Button = "left",
    ) -> None:
        """
        Execute a drag operation.

        Args:
            start: Starting position
            end: Ending position
            duration: Time to complete the drag in seconds
            button: Mouse button to use for dragging
        """
        # Move to start position
        start_move_duration = get_duration(self.move_duration)
        self.driver.move_to(start, duration=start_move_duration)

        # Press the button
        self.driver.press(button)

        # Small delay after pressing
        sleep(self.click_delay)

        # Drag to end position
        self.driver.move_to(end, duration=duration)

        # Small delay before releasing
        sleep(self.click_delay)

        # Release the button
        self.driver.release(button)
