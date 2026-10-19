"""Integrity check for the static demo bundle: every file the page references must exist."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "/schoolsync-demo/"


def main() -> int:
    errors: list[str] = []
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    refs = re.findall(r'(?:href|src)="([^"]+)"', html)
    for ref in refs:
        if ref.startswith(BASE):
            rel = ref[len(BASE):].split("?")[0]
            if not (ROOT / rel).is_file():
                errors.append(f"index.html references missing file: {rel}")
        elif ref.startswith(("http://", "https://", "data:", "#")):
            continue
        else:
            errors.append(f"index.html has a reference outside {BASE}: {ref}")

    manifest = json.loads((ROOT / "manifest.webmanifest").read_text(encoding="utf-8"))
    if manifest.get("start_url") != BASE or manifest.get("scope") != BASE:
        errors.append("manifest start_url/scope do not match the Pages base path")
    for icon in manifest.get("icons", []):
        if not (ROOT / icon["src"]).is_file():
            errors.append(f"manifest icon missing: {icon['src']}")

    for required in ("sw.js", ".nojekyll", "README.md"):
        if not (ROOT / required).exists():
            errors.append(f"missing {required}")

    # The demo must never ship a backend configuration.
    for js in (ROOT / "assets").glob("*.js"):
        text = js.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"AIza[0-9A-Za-z_-]{30,}", text):
            errors.append(f"{js.name} contains a Google API key")

    for e in errors:
        print("ERROR:", e)
    print("bundle OK" if not errors else f"{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
