#!/usr/bin/env python3
"""HyperFocus Z0ne - Portal Env Guard.

Documentation-only repo -- no required env vars.
Confirms we are in the correct repo root and passes.
Always exits 0.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    print("\n[ENV GUARD] HyperFocus Z0ne -- Portal")
    print("-" * 40)
    print("   Docs-only repo -- no required env vars.")
    print()

    marker = ROOT / "README.md"
    if not marker.exists():
        print("WARN  README.md not found -- may be wrong directory")
    else:
        print("   PASS  repo root confirmed (README.md present)")

    print()
    print("PASS  Env guard passed (docs-only repo -- no secrets required).\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
