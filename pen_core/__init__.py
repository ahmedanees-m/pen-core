"""pen-core: Shared core library for PEN-STACK."""

try:
    from pen_core._version import __version__
except ImportError:
    __version__ = "unknown"

__all__ = ["__version__"]
