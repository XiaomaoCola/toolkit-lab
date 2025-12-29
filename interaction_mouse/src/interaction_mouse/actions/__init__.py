"""
Mouse action implementations

This module contains implementations of various mouse actions
such as clicking, dragging, etc.
"""

from interaction_mouse.actions.click import ClickAction
from interaction_mouse.actions.repeat import RepeatClickAction
from interaction_mouse.actions.random_click import RandomClickAction
from interaction_mouse.actions.drag import DragAction

__all__ = [
    "ClickAction",
    "RepeatClickAction",
    "RandomClickAction",
    "DragAction",
]
