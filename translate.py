"""Compatibility shim: re-export the division_changes.translate module.

This allows the legacy ``python3 translate.py`` and ``from translate import translate``
usage to keep working from a source checkout, even without ``pip install``.
"""
from division_changes.translate import *  # noqa: F401,F403
from division_changes.translate import main


if __name__ == "__main__":
    main()
