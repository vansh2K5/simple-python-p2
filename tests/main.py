"""Simple demo Python app for Jenkins pipeline.

Run:
    python main.py --name YourName
"""

import sys
from datetime import datetime


def greet(name: str) -> str:
    """Return a friendly greeting message."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{current_time}] Hello, {name}! Jenkins Python project is working."


def parse_name(argv: list[str]) -> str:
    """Parse name from command-line arguments with a default."""
    if len(argv) >= 2:
        return argv[1]
    return "World"


def main() -> None:
    """Entry point for the script."""
    name = parse_name(sys.argv)
    message = greet(name)
    print(message)


if __name__ == "__main__":
    main()
