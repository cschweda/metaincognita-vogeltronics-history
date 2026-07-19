#!/usr/bin/env python3
"""Source generator for the 1961 Vogel Novelty heritage badge.

Writes assets/vogel-novelty-badge.svg. With --embed, also rasterizes it with
rsvg-convert (librsvg; text needs DejaVu Sans installed) and swaps the PNG
into both index.html data URIs that carry the badge — the shadow-card figure
(alt "Vogel Novelty heritage logo, 1961") and the 1961->1977 evolution strip
(alt "1961 logo"). Viewing or deploying the site never needs this script; it
exists so the badge stays editable.

Geometry notes: every border is sized off measured DejaVu glyph extents so
the text keeps clear air — wordmark 603px wide vs pinstripe ring 372x150
(>=50px clearance), "EST. 1961" fully inside the ring's bottom arc, 650px
banner text in a 740px ribbon, and the daisies centered on the cream rim's
edge (+-436) so their petals read whole against the page background instead
of vanishing cream-on-cream into the rim band.
"""

import base64
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SVG_OUT = REPO / 'assets' / 'vogel-novelty-badge.svg'
INDEX = REPO / 'index.html'

CREAM = '#f4efe6'
FONT = "'DejaVu Sans',Verdana,sans-serif"

W, H = 1090, 580
CX, CY = 545, 240
DAISY_L = CX - 436  # centered on the cream rim's edge at the waist
BL, BR = CX - 370, CX + 370  # banner rect left/right edges

BADGE_ALTS = ('Vogel Novelty heritage logo, 1961', '1961 logo')

heritage = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <radialGradient id="oval" cx=".5" cy=".42" r=".75">
      <stop offset="0" stop-color="#f08a3d"/>
      <stop offset=".6" stop-color="#ec7433"/>
      <stop offset="1" stop-color="#e8622a"/>
    </radialGradient>
    <linearGradient id="ribbon" x1="0" y1="448" x2="0" y2="527" gradientUnits="userSpaceOnUse">
      <stop offset="0" stop-color="#eeba43"/>
      <stop offset="1" stop-color="#dfa028"/>
    </linearGradient>
  </defs>

  <!-- oval badge -->
  <ellipse cx="{CX}" cy="{CY}" rx="436" ry="195" fill="{CREAM}"/>
  <ellipse cx="{CX}" cy="{CY}" rx="406" ry="176" fill="url(#oval)"/>
  <ellipse cx="{CX}" cy="{CY}" rx="372" ry="150" fill="none" stroke="{CREAM}" stroke-width="3" opacity=".8"/>

  <!-- wordmark -->
  <text x="{CX}" y="{CY + 29}" text-anchor="middle" font-family="{FONT}" font-weight="bold" font-size="86" fill="{CREAM}">Vogel Novelty</text>

  <!-- daisies -->
  <g id="daisyL" transform="translate({DAISY_L} {CY})">
    <g fill="{CREAM}">
      <ellipse rx="16" ry="30" transform="rotate(0) translate(0 -30)"/>
      <ellipse rx="16" ry="30" transform="rotate(72) translate(0 -30)"/>
      <ellipse rx="16" ry="30" transform="rotate(144) translate(0 -30)"/>
      <ellipse rx="16" ry="30" transform="rotate(216) translate(0 -30)"/>
      <ellipse rx="16" ry="30" transform="rotate(288) translate(0 -30)"/>
    </g>
    <circle r="15" fill="#e0a82e"/>
  </g>
  <use href="#daisyL" x="{(CX + 436) - DAISY_L}"/>

  <!-- est line -->
  <text x="{CX}" y="{CY + 117}" text-anchor="middle" font-family="{FONT}" font-weight="bold" font-size="24" letter-spacing="8" fill="{CREAM}">&#9733; EST. 1961 &#9733;</text>

  <!-- ribbon banner -->
  <polygon points="{BL + 10},452 {BL - 42},444 {BL - 28},486 {BL - 42},528 {BL + 10},520" fill="#d9a125"/>
  <polygon points="{BL - 42},444 {BL + 10},452 {BL + 10},444" fill="#8f5c10"/>
  <polygon points="{BR - 10},452 {BR + 42},444 {BR + 28},486 {BR + 42},528 {BR - 10},520" fill="#d9a125"/>
  <polygon points="{BR + 42},444 {BR - 10},452 {BR - 10},444" fill="#8f5c10"/>
  <rect x="{BL}" y="448" width="740" height="79" rx="6" fill="url(#ribbon)"/>
  <text x="{CX}" y="{CY + 262}" text-anchor="middle" font-family="{FONT}" font-weight="bold" font-size="42" letter-spacing="6" fill="#7b3d0a">WHOLESOME FAMILY FUN</text>
</svg>
'''


def embed():
    with tempfile.NamedTemporaryFile(suffix='.png') as png:
        subprocess.run(['rsvg-convert', str(SVG_OUT), '-o', png.name], check=True)
        payload = base64.b64encode(Path(png.name).read_bytes()).decode()
    html = INDEX.read_text()
    alts = '|'.join(re.escape(a) for a in BADGE_ALTS)
    pattern = re.compile(
        r'(<img src="data:image/png;base64,)[A-Za-z0-9+/=]+(" alt="(?:' + alts + r')")')
    html, n = pattern.subn(lambda m: m.group(1) + payload + m.group(2), html)
    if n != len(BADGE_ALTS):
        sys.exit(f'expected {len(BADGE_ALTS)} badge <img> tags in index.html, found {n}')
    INDEX.write_text(html)
    print(f'embedded {W}x{H} badge PNG into {n} index.html tags')


if __name__ == '__main__':
    SVG_OUT.write_text(heritage)
    print(f'wrote {SVG_OUT.relative_to(REPO)}')
    if '--embed' in sys.argv[1:]:
        embed()
