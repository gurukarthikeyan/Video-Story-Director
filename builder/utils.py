"""
Video Story Director
Build Utilities

Common helper functions used throughout the build system.
"""

from datetime import datetime
from pathlib import Path


# ============================================================================
# File Helpers
# ============================================================================

def read_text(file_path: Path) -> str:
    """
    Read a UTF-8 text file.

    Raises:
        FileNotFoundError
            If the file does not exist.
    """
    return file_path.read_text(encoding="utf-8")


def write_text(file_path: Path, content: str) -> None:
    """
    Write UTF-8 text to a file.
    Creates parent directories if necessary.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")


# ============================================================================
# Formatting Helpers
# ============================================================================

def separator(length: int = 78) -> str:
    """Return a separator line."""
    return "=" * length


def timestamp() -> str:
    """Return the current local timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def title(text: str) -> str:
    """Return a formatted title block."""
    return f"\n{separator()}\n{text}\n{separator()}\n"


# ============================================================================
# Console Helpers
# ============================================================================

def info(message: str) -> None:
    print(f"[INFO] {message}")


def success(message: str) -> None:
    print(f"[ OK ] {message}")


def warning(message: str) -> None:
    print(f"[WARN] {message}")


def error(message: str) -> None:
    print(f"[FAIL] {message}")