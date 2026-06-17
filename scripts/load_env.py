#!/usr/bin/env python3
"""Read .env and write config.local.js (gitignored) for local dev."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
env_path = ROOT / ".env"
api_key = ""

if env_path.exists():
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        if key.strip() == "OPENWEATHERMAP_API_KEY":
            api_key = value.strip().strip("'\"")
            break

(ROOT / "config.local.js").write_text(
    f"window.__OWM_API_KEY__ = {json.dumps(api_key)};\n"
)

if api_key:
    print("Wrote config.local.js from .env")
else:
    print("Wrote config.local.js (no OPENWEATHERMAP_API_KEY in .env — demo data will be used)")
