"""
Example 01: Basic Single Click

Demonstrates how to perform a simple mouse click at a specific position.
"""

from interaction_mouse import Clicker, Point


def main():
    # Create a clicker instance
    clicker = Clicker()

    # Click at position (100, 200)
    print("Clicking at position (100, 200)...")
    clicker.click(Point(x=100, y=200))
    print("Click completed!")

    # Click with left button (default)
    print("\nLeft click at (300, 400)...")
    clicker.click(Point(x=300, y=400), button="left")

    # Right click
    print("Right click at (300, 400)...")
    clicker.click(Point(x=300, y=400), button="right")

    # Middle click
    print("Middle click at (300, 400)...")
    clicker.click(Point(x=300, y=400), button="middle")

    print("\nAll clicks completed!")


if __name__ == "__main__":
    main()
