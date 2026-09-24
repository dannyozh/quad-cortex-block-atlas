# Quad Cortex Block Atlas

A searchable reference to every virtual device that fits in a block on the Neural DSP Quad Cortex and Quad Cortex mini as of **CorOS 4.1.0** (released 25 Aug 2026). For each device it lists the real gear it's modeled on and what it's good for.

**Live page:** https://dannyozh.github.io/quad-cortex-block-atlas/

- 632 entries: amps, cabs, IR loaders, effects, factory Neural Captures (V1 and V2) and plugin-licensed devices.
- Device names, "based on" credits and the CorOS version each device was added in come from Neural DSP's [device list](https://neuraldsp.com/device-list) and the [CorOS 4.1.0 release notes](https://neuraldsp.com/quad-cortex-updates/coros-and-cortex-control-4-1-0-are-now-available), checked 23 Sep 2026. The usage descriptions are editorial.

All product names are trademarks of their owners. Neural DSP uses them only to identify the gear its models were based on. This project isn't affiliated with Neural DSP or any of the brands listed.

## How it's built

The page is a single self-contained HTML file with no framework and no bundler.

Three concerns stay in separate files while editing, and `build.py` is the only place they meet:

| Concern | Lives in | Who changes it |
|---|---|---|
| Facts (names, "based on", version) | `data/next.json` | Neural DSP, by publishing an update |
| Commentary ("what it's for") | `data/desc_*.json` | us, by writing |
| Look and behavior | `src/template.html` | front-end work |

The build pastes the data into the template as a JavaScript object, and the browser draws the rows from it. That keeps search and filtering instant, with nothing to fetch.

`index.html` is generated, so edit `src/template.html` or `data/` and rebuild:

```sh
python3 build.py   # writes index.html (and build/qc-block-atlas.html, the bare fragment)
```

```
.
├── index.html            ← generated page, served by GitHub Pages
├── build.py              ← merges data/ into src/template.html → index.html
│
├── src/
│   └── template.html     ← all CSS, markup and JS (device data is injected at /*DATA*/)
│
├── data/
│   ├── next.json         ← device list from neuraldsp.com (names, "based on", CorOS version)
│   ├── desc_*.json       ← the "What it's for" descriptions, keyed by device (editorial)
│   └── plugins_meta.json ← per-plugin info (Archetype names, links)
│
├── test/
│   ├── cdp.mjs           ← headless Chrome driver (DevTools protocol, port 9333)
│   └── cdp-mid.mjs       ← same, at tablet width
│
└── scripts/archive/      ← one-off generators that wrote data/ and early template edits;
                            kept for the record, written against an older flat layout
```
