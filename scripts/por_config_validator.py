#!/usr/bin/env python3
"""HyperFocus Z0ne - Portal Config Validator.

Enforces Sacred Rules on markdown docs:
  - NEVER docker.io image references
  - NEVER 'from backend.app.' imports
  - WARN on plain http:// links (prefer https://)
  - WARN on hardcoded Windows paths (C:\\ or D:\\)

Usage:
    python scripts/por_config_validator.py README.md
    python scripts/por_config_validator.py PORTAL.md
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

_BANNED_IMAGE_PREFIXES = ("docker.io/", "index.docker.io/")
_BANNED_IMPORT_RE = re.compile(r"from\s+backend\.app\.")
_PLAIN_HTTP_RE = re.compile(r'http://(?!localhost|127\.0\.0\.1)', re.IGNORECASE)
_WINDOWS_PATH_RE = re.compile(r'[A-Za-z]:\\\\')


def _resolve_file(arg):
    p = Path(arg)
    if p.is_absolute():
        return p
    for base in (Path.cwd(), ROOT):
        candidate = base / p
        if candidate.exists():
            return candidate
    return Path.cwd() / p


def validate(file_path):
    errors = []
    warnings = []

    if not file_path.exists():
        errors.append("file not found: " + str(file_path))
        return errors, warnings

    for i, raw in enumerate(file_path.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = raw.strip()
        if not stripped:
            continue

        for prefix in _BANNED_IMAGE_PREFIXES:
            if prefix in stripped:
                errors.append("line " + str(i) + ": docker.io reference -- " + repr(stripped[:80]))

        if _BANNED_IMPORT_RE.search(stripped):
            errors.append("line " + str(i) + ": forbidden 'from backend.app.*' -- " + repr(stripped[:80]))

        if _PLAIN_HTTP_RE.search(stripped):
            warnings.append("line " + str(i) + ": plain http:// link -- prefer https://")

        if _WINDOWS_PATH_RE.search(stripped):
            warnings.append("line " + str(i) + ": hardcoded Windows path -- not portable")

    return errors, warnings


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python scripts/por_config_validator.py <file>")
        return 2

    file_path = _resolve_file(sys.argv[1])

    print("\n[CONFIG VALIDATOR] HyperFocus Z0ne Portal -- " + sys.argv[1])
    print("-" * 40)
    print("   Path: " + str(file_path))
    print()

    errors, warnings = validate(file_path)

    for w in warnings:
        print("   WARN  " + w)
    if warnings:
        print()

    if errors:
        for e in errors:
            print("   FAIL  " + e)
        print()
        print("FAIL  Validation FAILED -- " + str(len(errors)) + " error(s).\n")
        return 1

    print("PASS  " + file_path.name + " passed all Sacred Rules checks!")
    if warnings:
        print("      (" + str(len(warnings)) + " warning(s) -- non-blocking)")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
