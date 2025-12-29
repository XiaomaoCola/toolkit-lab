"""
Timing utilities for human-like behavior simulation

This module provides functions for adding randomness and jitter to timing
to make automated interactions appear more natural.
"""

import time
import random
from typing import Tuple, Union


def sleep_range(min_seconds: float, max_seconds: float) -> None:
    """
    Sleep for a random duration within the specified range.

    Args:
        min_seconds: Minimum sleep duration in seconds
        max_seconds: Maximum sleep duration in seconds
    """
    duration = random.uniform(min_seconds, max_seconds)
    time.sleep(duration)


def sleep(duration: Union[float, Tuple[float, float]]) -> None:
    """
    Sleep for a specified duration or random duration within a range.

    Args:
        duration: Either a single float (exact duration) or a tuple of
                 (min, max) for random duration
    """
    if isinstance(duration, tuple):
        sleep_range(duration[0], duration[1])
    else:
        time.sleep(duration)


def add_jitter(value: float, jitter_percent: float = 0.1) -> float:
    """
    Add random jitter to a value.

    Args:
        value: The base value
        jitter_percent: Percentage of jitter to add (0.1 = 10%)

    Returns:
        The value with jitter applied
    """
    jitter = value * jitter_percent
    return value + random.uniform(-jitter, jitter)


def clamp(value: float, min_value: float, max_value: float) -> float:
    """
    Clamp a value between min and max bounds.

    Args:
        value: The value to clamp
        min_value: Minimum allowed value
        max_value: Maximum allowed value

    Returns:
        The clamped value
    """
    return max(min_value, min(max_value, value))


def get_duration(
    duration: Union[float, Tuple[float, float]], jitter: bool = False
) -> float:
    """
    Get a duration value with optional randomization and jitter.

    Args:
        duration: Either a single float or a tuple of (min, max)
        jitter: Whether to add small random jitter

    Returns:
        The final duration value
    """
    if isinstance(duration, tuple):
        result = random.uniform(duration[0], duration[1])
    else:
        result = duration

    if jitter:
        result = add_jitter(result, jitter_percent=0.1)

    return max(0.0, result)  # Ensure non-negative
