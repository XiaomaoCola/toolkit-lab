"""
Repeat click action implementation
"""

import time
from typing import Union, Tuple
from interaction_mouse.models import Point, Button
from interaction_mouse.protocol import IMouseDriver
from interaction_mouse.timing import sleep, get_duration


class RepeatClickAction:
    """
    Action for performing multiple clicks at the same position.
    """

    def __init__(
        self,
        driver: IMouseDriver,
        click_delay: Union[float, Tuple[float, float]] = 0.01,
        move_duration: Union[float, Tuple[float, float]] = 0.0,
    ):
        """
        Initialize a repeat click action.

        Args:
            driver: Mouse driver to use
            click_delay: Delay between press and release
            move_duration: Duration for mouse movement
        """
        self.driver = driver
        self.click_delay = click_delay
        self.move_duration = move_duration

    def execute(
        self,
        point: Point,
        count: int = 1,
        interval: float = 0.0,
        button: Button = "left",
    ) -> None:
        """
        Execute multiple clicks at the same position.

        Args:
            point: Position to click
            count: Number of times to click
            interval: Time between clicks in seconds
            button: Mouse button to use
        """
        # Move to the target position once
        duration = get_duration(self.move_duration)
        self.driver.move_to(point, duration=duration)

        # Perform multiple clicks
        for i in range(count):
            # Click
            self.driver.press(button)
            sleep(self.click_delay)
            self.driver.release(button)

            # Wait before next click (except after the last one)
            if i < count - 1 and interval > 0:
                time.sleep(interval)
