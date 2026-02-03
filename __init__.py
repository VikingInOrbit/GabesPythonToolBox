"""Project root package shim for src layout."""

from __future__ import annotations

from pathlib import Path
from pkgutil import extend_path

# Allow imports to resolve to src/GabesPythonToolBox when running from repo root.
__path__ = extend_path(__path__, __name__)
_src_pkg = Path(__file__).resolve().parent / "src" / __name__
if _src_pkg.exists():
    __path__.append(str(_src_pkg))

__all__: list[str] = []
