<p align="center">
  <img src="assets/amtoy-logo.svg" alt="AmToy — Games That Think!" width="680">
</p>

# AmToy — The Whole Story

**Live site:** [amtoy.netlify.app](https://amtoy.netlify.app)

A single-page, magazine-style corporate history of **AmToy** ("Games That Think!") — a completely fictional American toy company founded in Elk Grove Village, Illinois in 1961 and dead by 1983, forever in the wrong place at the wrong time.

## Why a fictional company?

This project exists to give a family of retro-toy homage projects a shared backstory. The goal was to recreate the feel of the golden age of electronic handhelds and programmable toys — but the real things are protected trademarks and trade dress. So instead of imitating a real company, AmToy was invented from scratch: its own founder, its own catalog, its own logos, and its own string of heartbreaking near-misses.

Game *mechanics* are not copyrightable; the invented AmToy branding stands in for the real-world brands the projects deliberately avoid.

This history is the background lore for the [MetaIncognita](https://metaincognita.com) default page, which hosts playable recreations of AmToy's fictional catalog — including **Rovacon** (the programmable tank) and **Gridiron** / **Gridiron II** (the LED football handhelds).

## The story

The page covers, era by era:

- **1961 — The Founding** in Elk Grove Village, Illinois
- **1966–1976 — The Heritage Hits and the Lean Years** (Sergeant Steele, Meadow, Derby)
- **1977 — The Electronic Reinvention**: "Games That Think!"
- **1979 — The Flagship**: Rovacon, and the voice that shouldn't exist
- **1979–1982 — Electrify Everything**: the misfires (The Oracle, The Handicapper, Stargazer, Whirlwind…)
- **1980–1981 — The Grandmaster Affair** and the ghost in the machine
- **1981 — The Cordless Detour**: AmToy leaves the toy aisle
- **1983 — The Colossus and the Crash**: the last, fatal bet
- **Epilogue** — and links to play the games

## Tech

There is no build step and there are no dependencies. The entire site — markup, styles, and all 18 images (embedded as data URIs) — is one self-contained `index.html` (~2 MB). The `assets/` folder holds only the README logo artwork (`amtoy-logo.svg` and its PNG render), drawn as pure vector paths so it needs no fonts.

To view locally, open `index.html` in a browser, or serve the folder:

```bash
npx serve .
```

## Deployment

Deployed on [Netlify](https://www.netlify.com/) at [amtoy.netlify.app](https://amtoy.netlify.app). `netlify.toml` publishes the repo root as-is; every push to `main` deploys.

## Legal

AmToy, VoxAm, Walter T. Vogel, Viktor Ozerov, and every product named in this history are original inventions created for a set of retro-toy homage projects. They deliberately use no Hasbro, Mattel, Milton Bradley, Parker Brothers, or Fidelity trademarks, logos, or trade dress. Any resemblance to real companies or persons is affectionate parody.

## License

[MIT](LICENSE)
