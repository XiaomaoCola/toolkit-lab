"""
Random click action implementation
"""

import time
from typing import Union, Tuple
from interaction_mouse.models import Rect, Button
from interaction_mouse.protocol import IMouseDriver
from interaction_mouse.targets.random_rect import RandomRectTarget
from interaction_mouse.timing import sleep, get_duration


class RandomClickAction:
    """
    Action for performing clicks at random positions within a rectangle.
    """

    def __init__(
        self,
        driver: IMouseDriver,
        click_delay: Union[float, Tuple[float, float]] = 0.01,
        move_duration: Union[float, Tuple[float, float]] = 0.0,
    ):
        """
        Initialize a random click action.

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
        rect: Rect,
        count: int = 1,
        interval: float = 0.0,
        button: Button = "left",
    ) -> None:
        """
        Execute clicks at random positions within a rectangle.

        Args:
            rect: Rectangle area to click within
            count: Number of times to click
            interval: Time between clicks in seconds
            button: Mouse button to use
        """
        target = RandomRectTarget(rect)

        for i in range(count):
            # Get random position
            point = target.get_target()

            # Move to position
            duration = get_duration(self.move_duration)
            self.driver.move_to(point, duration=duration)

            # Click
            self.driver.press(button)
            sleep(self.click_delay)
            self.driver.release(button)

            # Wait before next click (except after the last one)
            if i < count - 1 and interval > 0:
                time.sleep(interval)
