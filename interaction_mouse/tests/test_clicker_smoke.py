"""
Smoke tests for Clicker class

These tests verify basic functionality without actually moving the mouse.
We use a mock driver to avoid real mouse movements during testing.
"""

import pytest
from unittest.mock import Mock, call
from interaction_mouse import Clicker, Point, Rect
from interaction_mouse.protocol import IMouseDriver


class MockDriver:
    """Mock driver for testing without real mouse movements"""

    def __init__(self):
        self.position = Point(x=0, y=0)
        self.calls = []

    def move_to(self, point: Point, duration: float = 0.0) -> None:
        self.position = point
        self.calls.append(("move_to", point, duration))

    def press(self, button: str = "left") -> None:
        self.calls.append(("press", button))

    def release(self, button: str = "left") -> None:
        self.calls.append(("release", button))

    def click(self, button: str = "left") -> None:
        self.calls.append(("click", button))

    def get_position(self) -> Point:
        return self.position


class TestClickerBasics:
    """Basic smoke tests for Clicker"""

    def test_initialization(self):
        """Clicker should initialize without errors"""
        clicker = Clicker()
        assert clicker is not None

    def test_initialization_with_driver(self):
        """Clicker should accept custom driver"""
        driver = MockDriver()
        clicker = Clicker(driver=driver)
        assert clicker.driver is driver


class TestClickerClick:
    """Tests for single click functionality"""

    def test_click_calls_driver(self):
        """Click should call driver methods"""
        driver = MockDriver()
        clicker = Clicker(driver=driver, click_delay=0.0, move_duration=0.0)

        point = Point(x=100, y=200)
        clicker.click(point)

        # Should have moved, pressed, and released
        assert len(driver.calls) >= 3
        assert driver.calls[0][0] == "move_to"
        assert driver.calls[0][1] == point

    def test_click_different_buttons(self):
        """Should support different mouse buttons"""
        driver = MockDriver()
        clicker = Clicker(driver=driver, click_delay=0.0, move_duration=0.0)

        point = Point(x=100, y=200)

        # Test all button types
        for button in ["left", "right", "middle"]:
            driver.calls.clear()
            clicker.click(point, button=button)
            # Check that button was used
            press_calls = [c for c in driver.calls if c[0] == "press"]
            assert len(press_calls) > 0
            assert press_calls[0][1] == button


class TestClickerRepeatClick:
    """Tests for repeat click functionality"""

    def test_repeat_click_count(self):
        """Should click the specified number of times"""
        driver = MockDriver()
        clicker = Clicker(driver=driver, click_delay=0.0, move_duration=0.0)

        point = Point(x=100, y=200)
        count = 5

        clicker.repeat_click(point, count=count, interval=0.0)

        # Count press operations
        press_calls = [c for c in driver.calls if c[0] == "press"]
        assert len(press_calls) == count

    def test_repeat_click_same_position(self):
        """Should click at the same position"""
        driver = MockDriver()
        clicker = Clicker(driver=driver, click_delay=0.0, move_duration=0.0)

        point = Point(x=100, y=200)
        clicker.repeat_click(point, count=3, interval=0.0)

        # Should move once to the position
        move_calls = [c for c in driver.calls if c[0] == "move_to"]
        assert len(move_calls) >= 1
        assert move_calls[0][1] == point


class TestClickerRandomClick:
    """Tests for random click functionality"""

    def test_random_click_count(self):
        """Should click the specified number of times"""
        driver = MockDriver()
        clicker = Clicker(driver=driver, click_delay=0.0, move_duration=0.0)

        rect = Rect(x=100, y=200, width=50, height=30)
        count = 5

        clicker.random_click(rect, count=count, interval=0.0)

        # Count press operations
        press_calls = [c for c in driver.calls if c[0] == "press"]
        assert len(press_calls) == count

    def test_random_click_within_bounds(self):
        """Random clicks should be within rectangle bounds"""
        driver = MockDriver()
        clicker = Clicker(driver=driver, click_delay=0.0, move_duration=0.0)

        rect = Rect(x=100, y=200, width=50, height=30)
        count = 10

        clicker.random_click(rect, count=count, interval=0.0)

        # Check all move_to calls are within bounds
        move_calls = [c for c in driver.calls if c[0] == "move_to"]
        for call in move_calls:
            point = call[1]
            assert rect.x <= point.x < rect.x + rect.width
            assert rect.y <= point.y < rect.y + rect.height


class TestClickerDrag:
    """Tests for drag functionality"""

    def test_drag_calls_driver(self):
        """Drag should move and use button properly"""
        driver = MockDriver()
        clicker = Clicker(driver=driver, click_delay=0.0, move_duration=0.0)

        start = Point(x=100, y=200)
        end = Point(x=300, y=400)

        clicker.drag(start, end, duration=0.0)

        # Should have: move to start, press, move to end, release
        assert len(driver.calls) >= 4

        move_calls = [c for c in driver.calls if c[0] == "move_to"]
        assert len(move_calls) >= 2

        press_calls = [c for c in driver.calls if c[0] == "press"]
        release_calls = [c for c in driver.calls if c[0] == "release"]
        assert len(press_calls) == 1
        assert len(release_calls) == 1

    def test_drag_button_types(self):
        """Should support different buttons for dragging"""
        driver = MockDriver()
        clicker = Clicker(driver=driver, click_delay=0.0, move_duration=0.0)

        start = Point(x=100, y=200)
        end = Point(x=300, y=400)

        for button in ["left", "right", "middle"]:
            driver.calls.clear()
            clicker.drag(start, end, duration=0.0, button=button)

            press_calls = [c for c in driver.calls if c[0] == "press"]
            assert press_calls[0][1] == button
