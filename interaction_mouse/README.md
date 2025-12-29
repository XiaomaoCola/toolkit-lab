# Interaction Mouse

A flexible and extensible Python library for simulating human-like mouse interactions with support for multiple backends and customizable timing patterns.

## Features

- **Multiple Driver Backends**: Support for Win32 API (SendInput) and PyAutoGUI fallback
- **Human-like Behavior**: Configurable timing, jitter, and randomization
- **Flexible Targeting**: Fixed points, random positions within rectangles, and near-point targeting
- **Common Actions**: Click, repeat clicks, random clicks, and drag operations
- **Type-safe**: Full type hints and protocol-based design
- **Extensible**: Easy to add custom drivers, targets, and actions

## Installation

```bash
pip install interaction-mouse
```

For Windows with native Win32 API support:
```bash
pip install interaction-mouse[win32]
```

For development:
```bash
pip install interaction-mouse[dev]
```

## Quick Start

### Simple Click

```python
from interaction_mouse import Clicker, Point

clicker = Clicker()
clicker.click(Point(100, 200))
```

### Repeat Clicks

```python
from interaction_mouse import Clicker, Point

clicker = Clicker()
clicker.repeat_click(Point(100, 200), count=5, interval=0.5)
```

### Random Click in Rectangle

```python
from interaction_mouse import Clicker, Rect

clicker = Clicker()
rect = Rect(x=100, y=200, width=50, height=30)
clicker.random_click(rect, count=3)
```

### Drag Operation

```python
from interaction_mouse import Clicker, Point

clicker = Clicker()
clicker.drag(Point(100, 200), Point(300, 400), duration=0.5)
```

## Project Structure

```
interaction_mouse/
├── models.py            # Core data models (Point, Rect, Button)
├── protocol.py          # IMouseDriver protocol
├── errors.py            # Custom exceptions
├── timing.py            # Timing utilities (sleep range, jitter)
├── clicker.py           # Main facade interface
├── drivers/             # Mouse driver implementations
│   ├── win32.py        # Windows SendInput driver
│   └── pyautogui.py    # PyAutoGUI fallback driver
├── targets/             # Target position strategies
│   ├── fixed.py        # Fixed point targeting
│   ├── random_rect.py  # Random position in rectangle
│   └── near.py         # Near-point targeting
└── actions/             # Action implementations
    ├── click.py        # Single click action
    ├── repeat.py       # Repeat click action
    ├── random_click.py # Random click action
    └── drag.py         # Drag action
```

## Advanced Usage

### Custom Driver

```python
from interaction_mouse import Clicker
from interaction_mouse.drivers import Win32Driver

clicker = Clicker(driver=Win32Driver())
```

### Custom Timing

```python
from interaction_mouse import Clicker, Point

clicker = Clicker(
    click_delay=(0.05, 0.15),  # Random delay between 50-150ms
    move_duration=(0.1, 0.3)   # Random move duration
)
clicker.click(Point(100, 200))
```

## Examples

See the `examples/` directory for more detailed usage examples:

- `01_click_once.py` - Basic single click
- `02_repeat_click.py` - Repeated clicking
- `03_random_click_rect.py` - Random position clicking
- `04_drag.py` - Drag and drop operations

## Testing

```bash
pytest tests/
```

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
