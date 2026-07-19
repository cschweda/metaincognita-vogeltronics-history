# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2026-07-19

### Added

- Box art on every "Play the Games" card, reused from the history's embedded illustrations by id at load time — no image data is duplicated, so the file barely grows.
- Two more COMING SOON cards in the games grid: **Gridiron II** ("now with THE FORWARD PASS" — re-created faithfully, random interceptions and all) and **The Oracle** (still giving the only answer it ever gave: I WOULD BET ON IT).

## [1.2.0] - 2026-07-19

### Added

- Rovacon sound previews in the "Play the Games" grid: the three actual in-game VoxAm voice clips — "Rovacon." (introducing itself), "System fault." (a route gone wrong), and "Ouch. That hurts." (falling down the stairs) — playable from the Rovacon card. The clips are embedded as `data:` URIs, so the site remains a single self-contained file; the source WAVs live in `assets/`.

### Changed

- The games grid is now a two-across flex layout, giving each card room for its summary and the sound buttons.
- The Rovacon card is marked COMING SOON (like Gridiron) until the game itself ships.
- Both game-card summaries now wink at the real 1977/1979 handhelds they homage — without naming the brands.
- Tightened the history since 1.1.0: removed the Sorcerer entirely, gave the hero a new founder quote, rewrote the Cordless Detour around the trickle charger, and trimmed the Colossus cord fiasco down to the stuck cartridge.

## [1.1.0] - 2026-07-18

### Added

- AmToy logo (`assets/amtoy-logo.svg`, plus a 2× PNG render at `assets/amtoy-logo.png`): a dark late-70s product-badge lockup of the masthead brand — LED-apex A, cream/red AMTOY wordmark, gold "Games That Think!" tagline. The wordmark is drawn as pure vector paths, so it renders identically everywhere with no font dependencies. Now heads the README.

## [1.0.0] - 2026-07-18

### Added

- Initial release: the complete single-page AmToy corporate history (1961–1983), from the founding in Elk Grove Village through the Heritage Hits, the Electronic Reinvention, Rovacon, the Gridiron handhelds, the Grandmaster Affair, and the Crash.
- All 18 illustrations embedded as data URIs — the site is one self-contained `index.html` with no build step.
- Fictional-parody disclaimer in the page footer.
- Repository scaffolding: README, MIT license, `.gitignore`, `netlify.toml`, and this changelog.

[1.3.0]: https://github.com/cschweda/amtoy-history/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/cschweda/amtoy-history/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/cschweda/amtoy-history/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/cschweda/amtoy-history/releases/tag/v1.0.0
