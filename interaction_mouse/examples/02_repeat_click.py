"""
Example 02: Repeat Click

Demonstrates how to perform multiple clicks at the same position with intervals.
"""

from interaction_mouse import Clicker, Point


def main():
    clicker = Clicker()

    # Perform 5 clicks at the same position with 0.5 second intervals
    print("Performing 5 clicks at (200, 300) with 0.5s intervals...")
    clicker.repeat_click(
        point=Point(x=200, y=300),
        count=5,
        interval=0.5,
        button="left"
    )
    print("Repeat clicks completed!")

    # Fast clicking (0.1s interval)
    print("\nFast clicking 10 times at (400, 500)...")
    clicker.repeat_click(
        point=Point(x=400, y=500),
        count=10,
        interval=0.1
    )
    print("Fast clicks completed!")

    # With custom timing configuration
    print("\nClicking with human-like timing variation...")
    clicker_with_jitter = Clicker(
        click_delay=(0.05, 0.15),  # Random delay between clicks
    )
    clicker_with_jitter.repeat_click(
        point=Point(x=300, y=300),
        count=5,
        interval=0.3
    )
    print("Human-like clicks completed!")


if __name__ == "__main__":
    main()
