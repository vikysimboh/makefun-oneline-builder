#!/usr/bin/env python3
"""Ship the one-line pitch to the output directory.

This is the entrypoint for the make.fun bounty
u-witty-walrus-69-5301-one-line-that-makes-a-builder-871d7faf. It takes the
one-line pitch shipped beside it as entry.txt and places an exact copy in
the output directory. Nothing is fetched, nothing is
generated: the file is copied byte for byte.

Runs on Python 3.13 with the standard library only.
"""

import os as _os
import shutil as _shutil
from pathlib import Path as _Path


def _output_dir() -> _Path:
    """Return the directory the copy goes to."""
    wanted = _os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = _Path(wanted)
    target.mkdir(parents=True, exist_ok=True)
    return target


def main() -> None:
    """Copy entry.txt next to this file into the output directory."""
    # entry.txt ships beside this file; the copy keeps it exact.
    here = _Path(__file__).resolve().parent
    _shutil.copyfile(here / "entry.txt", _output_dir() / "entry.txt")


if __name__ == "__main__":
    main()
