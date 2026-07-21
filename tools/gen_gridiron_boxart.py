#!/usr/bin/env python3
"""Regenerate the Gridiron (1977) box art and re-embed it in index.html.

The box art is stored as a base64 PNG on the <img id="art-gridiron"> tag;
the catalog gallery clones it via data-art. This script re-renders the art
from SVG (via headless Chrome) and swaps the base64 payload in place.

All copy on the box is original VogelTronics material — do not use real
manufacturers' advertising lines.

Usage:  python3 tools/gen_gridiron_boxart.py
"""

import base64
import pathlib
import re
import subprocess
import tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ROOT = pathlib.Path(__file__).resolve().parent.parent
W, H = 600, 780

FOOTER_1 = "ALL THE ACTION OF THE GRIDIRON · IT THINKS TWO PLAYS AHEAD"
FOOTER_2 = "2 PLAYERS · PRO 1 / PRO 2 · REQUIRES 9-VOLT BATTERY · NO. 2100"

# blip grid: 3 rows x 9 cols; a handful lit "bright" for drama
BRIGHT = {(0, 4), (0, 7), (1, 1), (1, 5), (2, 5)}


def blips() -> str:
    out = []
    for row in range(3):
        for col in range(9):
            cx, cy = 108 + col * 48, 210 + row * 52
            if (row, col) in BRIGHT:
                out.append(f'<circle cx="{cx}" cy="{cy}" r="16" fill="#ff3b2a" opacity=".22"/>')
                out.append(f'<circle cx="{cx}" cy="{cy}" r="11" fill="#ff3b2a"/>')
            else:
                out.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="#4a0b06"/>')
    return "\n    ".join(out)


SVG = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="{W}" height="{H}" fill="#101014"/>
  <rect x="14" y="14" width="{W - 28}" height="{H - 28}" rx="6" fill="none" stroke="#2e2e33" stroke-width="2"/>

  <text x="48" y="74" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-weight="800" font-size="36"><tspan fill="#f4efe6">Vogel</tspan><tspan fill="#e8322a">Tronics</tspan></text>
  <text x="552" y="70" text-anchor="end" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-weight="600" font-size="17" letter-spacing="5" fill="#9a9aa2">1977</text>

  <rect x="70" y="115" width="460" height="230" rx="18" fill="#1c0605" stroke="#3a0c08" stroke-width="4"/>
  <text x="300" y="172" text-anchor="middle" font-family="Menlo, Courier New, monospace" font-weight="700" font-size="32" letter-spacing="6" fill="#ff5040">1st &amp; 10</text>
  <g>
    {blips()}
  </g>

  <text x="300" y="472" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-weight="800" font-size="82" letter-spacing="10" fill="#f2ead8">GRIDIRON</text>
  <text x="300" y="520" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-weight="700" font-size="25" letter-spacing="8" fill="#e01f10">ELECTRONIC FOOTBALL</text>

  <g transform="translate(300 600) rotate(-4)">
    <rect x="-218" y="-33" width="436" height="66" rx="9" fill="#e01f10"/>
    <text x="0" y="11" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-weight="800" font-style="italic" font-size="30" letter-spacing="3" fill="#ffffff">GAMES THAT THINK!</text>
  </g>

  <text x="300" y="702" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-weight="600" font-size="13" letter-spacing="1.4" fill="#c9c9cf">{FOOTER_1}</text>
  <text x="300" y="740" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-weight="500" font-size="13" letter-spacing="2" fill="#85858d">{FOOTER_2}</text>
</svg>
"""


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        page = pathlib.Path(td) / "box.html"
        out = pathlib.Path(td) / "box.png"
        page.write_text(
            "<!doctype html><html><head><meta charset='utf-8'>"
            "<style>html,body{margin:0;padding:0;overflow:hidden}</style></head>"
            f"<body>{SVG}</body></html>"
        )
        subprocess.run(
            [CHROME, "--headless=new", f"--screenshot={out}", f"--window-size={W},{H}",
             "--hide-scrollbars", "--disable-gpu", f"file://{page}"],
            check=True, capture_output=True,
        )
        b64 = base64.b64encode(out.read_bytes()).decode()

    index = ROOT / "index.html"
    html = index.read_text()
    pattern = r'(<img src="data:image/png;base64,)[A-Za-z0-9+/=]+("[^>]*id="art-gridiron")'
    new_html, n = re.subn(pattern, lambda m: m.group(1) + b64 + m.group(2), html, count=1)
    if n != 1:
        raise SystemExit("could not find the art-gridiron master image tag")
    index.write_text(new_html)
    print(f"re-embedded art-gridiron ({len(b64)} b64 chars)")


if __name__ == "__main__":
    main()
