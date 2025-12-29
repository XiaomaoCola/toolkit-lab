"""
Tests for target position strategies
"""

import pytest
from interaction_mouse.models import Point, Rect
from interaction_mouse.targets import FixedTarget, RandomRectTarget, NearTarget
from interaction_mouse.errors import InvalidTargetError


class TestFixedTarget:
    """Tests for FixedTarget strategy"""

    def test_returns_same_point(self):
        """Fixed target should always return the same point"""
        point = Point(x=100, y=200)
        target = FixedTarget(point)

        # Call multiple times, should always get the same point
        assert target.get_target() == point
        assert target.get_target() == point
        assert target.get_target() == point

    def test_different_points(self):
        """Different fixed targets should return different points"""
        target1 = FixedTarget(Point(x=100, y=200))
        target2 = FixedTarget(Point(x=300, y=400))

        assert target1.get_target() != target2.get_target()


class TestRandomRectTarget:
    """Tests for RandomRectTarget strategy"""

    def test_point_within_bounds(self):
        """Random points should be within the rectangle bounds"""
        rect = Rect(x=100, y=200, width=50, height=30)
        target = RandomRectTarget(rect)

        # Test multiple random points
        for _ in range(100):
            point = target.get_target()
            assert rect.x <= point.x < rect.x + rect.width
            assert rect.y <= point.y < rect.y + rect.height

    def test_invalid_rectangle(self):
        """Should raise error for invalid rectangle dimensions"""
        with pytest.raises(InvalidTargetError):
            RandomRectTarget(Rect(x=0, y=0, width=0, height=100))

        with pytest.raises(InvalidTargetError):
            RandomRectTarget(Rect(x=0, y=0, width=100, height=-10))

    def test_single_pixel_rectangle(self):
        """Should work with 1x1 rectangle"""
        rect = Rect(x=100, y=200, width=1, height=1)
        target = RandomRectTarget(rect)

        # All points should be the same for 1x1 rectangle
        point = target.get_target()
        assert point == Point(x=100, y=200)


class TestNearTarget:
    """Tests for NearTarget strategy"""

    def test_point_within_offset(self):
        """Random points should be within max_offset of center"""
        center = Point(x=500, y=500)
        max_offset = 10
        target = NearTarget(center, max_offset)

        # Test multiple random points
        for _ in range(100):
            point = target.get_target()
            assert abs(point.x - center.x) <= max_offset
            assert abs(point.y - center.y) <= max_offset

    def test_zero_offset(self):
        """Zero offset should always return center point"""
        center = Point(x=100, y=200)
        target = NearTarget(center, max_offset=0)

        # Should always return exact center
        for _ in range(10):
            assert target.get_target() == center

    def test_negative_offset_raises_error(self):
        """Negative offset should raise error"""
        with pytest.raises(InvalidTargetError):
            NearTarget(Point(x=100, y=200), max_offset=-5)

    def test_large_offset(self):
        """Should work with large offsets"""
        center = Point(x=1000, y=1000)
        max_offset = 100
        target = NearTarget(center, max_offset)

        point = target.get_target()
        assert abs(point.x - center.x) <= max_offset
        assert abs(point.y - center.y) <= max_offset
