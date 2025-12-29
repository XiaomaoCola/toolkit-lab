"""
Example 03: Random Click in Rectangle

Demonstrates how to click at random positions within a defined rectangle area.
Useful for avoiding detection in automation or testing different areas.
"""

from interaction_mouse import Clicker, Rect


def main():
    clicker = Clicker()

    # Define a rectangle area
    # x=100, y=200 is top-left corner
    # width=200, height=100 defines the size
    rect = Rect(x=100, y=200, width=200, height=100)

    print(f"Clicking randomly within rectangle: {rect}")
    print("Top-left: (100, 200), Bottom-right: (300, 300)")

    # Perform 5 random clicks within the rectangle
    print("\nPerforming 5 random clicks...")
    clicker.random_click(
        rect=rect,
        count=5,
        interval=0.5,
        button="left"
    )
    print("Random clicks completed!")

    # Define a larger area for more variation
    large_rect = Rect(x=50, y=50, width=500, height=400)
    print(f"\nClicking randomly in larger area: {large_rect}")

    clicker.random_click(
        rect=large_rect,
        count=10,
        interval=0.3
    )
    print("Large area random clicks completed!")

    # With human-like behavior
    print("\nRandom clicks with human-like timing...")
    human_clicker = Clicker(
        click_delay=(0.1, 0.2),
        move_duration=(0.2, 0.5)
    )
    human_clicker.random_click(
        rect=Rect(x=200, y=200, width=150, height=150),
        count=3,
        interval=1.0
    )
    print("Human-like random clicks completed!")


if __name__ == "__main__":
    main()
