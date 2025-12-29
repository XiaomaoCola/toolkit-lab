"""
Example 04: Drag and Drop

Demonstrates how to perform drag operations from one point to another.
Useful for drag-and-drop operations, slider controls, etc.
"""

from interaction_mouse import Clicker, Point


def main():
    clicker = Clicker()

    # Simple drag from one point to another
    start = Point(x=100, y=200)
    end = Point(x=400, y=500)

    print(f"Dragging from {start} to {end}")
    clicker.drag(
        start=start,
        end=end,
        duration=0.5,  # Takes 0.5 seconds to complete the drag
        button="left"
    )
    print("Drag completed!")

    # Horizontal drag (like a slider)
    print("\nHorizontal drag (slider simulation)...")
    clicker.drag(
        start=Point(x=200, y=300),
        end=Point(x=600, y=300),  # Same Y coordinate
        duration=1.0
    )
    print("Horizontal drag completed!")

    # Vertical drag
    print("\nVertical drag...")
    clicker.drag(
        start=Point(x=300, y=100),
        end=Point(x=300, y=500),  # Same X coordinate
        duration=0.8
    )
    print("Vertical drag completed!")

    # Slow drag for precise control
    print("\nSlow, precise drag...")
    clicker.drag(
        start=Point(x=150, y=150),
        end=Point(x=450, y=450),
        duration=2.0  # Slower movement
    )
    print("Slow drag completed!")

    # With human-like behavior
    print("\nDrag with human-like movement...")
    human_clicker = Clicker(
        move_duration=(0.3, 0.7)  # Variable duration for naturalness
    )
    human_clicker.drag(
        start=Point(x=100, y=100),
        end=Point(x=500, y=400),
        duration=1.0
    )
    print("Human-like drag completed!")


if __name__ == "__main__":
    main()
