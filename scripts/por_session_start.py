#!/usr/bin/env python3
"""HyperFocus Z0ne - Portal Session Start Hook.

Writes a .focus_session_start marker and checks core doc files exist.
Exits 0 on pass, 1 on hard failure.
"""

import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SESSION_FILE = ROOT / ".focus_session_start"


def main() -> int:
    now = datetime.now()
    print("\n[SESSION START] HyperFocus Z0ne -- Portal")
    print("-" * 40)
    print("   Time    : " + now.strftime("%Y-%m-%d %H:%M:%S"))

    SESSION_FILE.write_text(now.isoformat())

    readme_ok = (ROOT / "README.md").exists()
    portal_ok = (ROOT / "PORTAL.md").exists()
    contrib_ok = (ROOT / "CONTRIBUTING.md").exists()

    print("   README.md    : " + ("PASS found" if readme_ok else "FAIL missing"))
    print("   PORTAL.md    : " + ("PASS found" if portal_ok else "WARN missing"))
    print("   CONTRIBUTING : " + ("PASS found" if contrib_ok else "WARN missing"))
    print()

    if not readme_ok:
        print("FAIL  Session start FAILED -- README.md not found.\n")
        return 1

    print("PASS  Portal session started. BROski forever! Let's build!\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
