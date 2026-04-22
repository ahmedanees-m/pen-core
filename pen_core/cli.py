"""CLI for pen-core."""
from __future__ import annotations

import click


@click.group()
@click.version_option()
def main() -> int:
    """pen-core CLI."""
    return 0


if __name__ == "__main__":
    main()
