"""
Tests for timing utilities
"""

import time
import pytest
from interaction_mouse.timing import (
    sleep_range,
    sleep,
    add_jitter,
    clamp,
    get_duration,
)


class TestSleepRange:
    """Tests for sleep_range function"""

    def test_sleep_within_range(self):
        """Should sleep for duration within specified range"""
        min_sleep = 0.01
        max_sleep = 0.02

        start = time.time()
        sleep_range(min_sleep, max_sleep)
        elapsed = time.time() - start

        # Allow small margin for timing precision
        assert elapsed >= min_sleep * 0.9
        assert elapsed <= max_sleep * 1.1


class TestSleep:
    """Tests for sleep function"""

    def test_sleep_exact_duration(self):
        """Should sleep for exact duration when given float"""
        duration = 0.01

        start = time.time()
        sleep(duration)
        elapsed = time.time() - start

        assert elapsed >= duration * 0.9
        assert elapsed <= duration * 1.1

    def test_sleep_with_range(self):
        """Should sleep within range when given tuple"""
        duration_range = (0.01, 0.02)

        start = time.time()
        sleep(duration_range)
        elapsed = time.time() - start

        assert elapsed >= duration_range[0] * 0.9
        assert elapsed <= duration_range[1] * 1.1


class TestAddJitter:
    """Tests for add_jitter function"""

    def test_jitter_within_bounds(self):
        """Jitter should be within specified percentage"""
        value = 1.0
        jitter_percent = 0.1

        # Test multiple times due to randomness
        for _ in range(100):
            result = add_jitter(value, jitter_percent)
            expected_min = value * (1 - jitter_percent)
            expected_max = value * (1 + jitter_percent)
            assert expected_min <= result <= expected_max

    def test_jitter_with_zero_value(self):
        """Should work with zero value"""
        result = add_jitter(0.0, 0.1)
        assert result == 0.0

    def test_jitter_varies(self):
        """Jitter should produce different values"""
        value = 1.0
        results = [add_jitter(value, 0.2) for _ in range(10)]
        # At least some values should be different
        assert len(set(results)) > 1


class TestClamp:
    """Tests for clamp function"""

    def test_clamp_within_bounds(self):
        """Value within bounds should be unchanged"""
        assert clamp(5.0, 0.0, 10.0) == 5.0

    def test_clamp_below_min(self):
        """Value below min should be clamped to min"""
        assert clamp(-5.0, 0.0, 10.0) == 0.0

    def test_clamp_above_max(self):
        """Value above max should be clamped to max"""
        assert clamp(15.0, 0.0, 10.0) == 10.0

    def test_clamp_at_boundaries(self):
        """Values at boundaries should remain unchanged"""
        assert clamp(0.0, 0.0, 10.0) == 0.0
        assert clamp(10.0, 0.0, 10.0) == 10.0


class TestGetDuration:
    """Tests for get_duration function"""

    def test_fixed_duration(self):
        """Should return exact value for fixed duration"""
        assert get_duration(1.0) == 1.0

    def test_range_duration(self):
        """Should return value within range"""
        min_dur, max_dur = 0.5, 1.5

        for _ in range(50):
            result = get_duration((min_dur, max_dur))
            assert min_dur <= result <= max_dur

    def test_with_jitter(self):
        """Should apply jitter when requested"""
        base_value = 1.0
        results = [get_duration(base_value, jitter=True) for _ in range(20)]

        # Results should vary
        assert len(set(results)) > 1

        # All results should be reasonably close to base value
        for result in results:
            assert 0.8 <= result <= 1.2

    def test_non_negative(self):
        """Should always return non-negative value"""
        assert get_duration(0.0) >= 0.0
        assert get_duration((0.0, 1.0)) >= 0.0
