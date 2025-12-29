"""
Single click action implementation
"""

from typing import Union, Tuple
from interaction_mouse.models import Point, Button
from interaction_mouse.protocol import IMouseDriver
from interaction_mouse.timing import sleep, get_duration


class ClickAction:
    """
    Action for performing a single click at a specified position.
    """

    def __init__(
        self,
        driver: IMouseDriver,
        click_delay: Union[float, Tuple[float, float]] = 0.01,
        move_duration: Union[float, Tuple[float, float]] = 0.0,
    ):
        """
        Initialize a click action.

        Args:
            driver: Mouse driver to use
            click_delay: Delay between press and release
            move_duration: Duration for mouse movement
        """
        self.driver = driver
        self.click_delay = click_delay
        self.move_duration = move_duration

    def execute(self, point: Point, button: Button = "left") -> None:
        """
        Execute a single click.

        Args:
            point: Position to click
            button: Mouse button to use
        """
        # Move to the target position
        duration = get_duration(self.move_duration)
        self.driver.move_to(point, duration=duration)

        # Perform the click with delay
        self.driver.press(button)
        sleep(self.click_delay)
        self.driver.release(button)
