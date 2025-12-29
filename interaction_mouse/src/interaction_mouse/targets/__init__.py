"""
Target position strategies

This module contains different strategies for determining target positions
for mouse actions.
"""

from interaction_mouse.targets.fixed import FixedTarget
from interaction_mouse.targets.random_rect import RandomRectTarget
from interaction_mouse.targets.near import NearTarget

__all__ = [
    "FixedTarget",
    "RandomRectTarget",
    "NearTarget",
]
