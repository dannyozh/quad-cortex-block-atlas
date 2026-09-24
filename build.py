"""
Build step: data/*.json + src/template.html -> index.html

A one-shot static-site generator. It reads Neural DSP's device list, attaches our
editorial descriptions, arranges everything into the page's tabs, and pastes the
result into the template as a JS object. The browser renders the rows from there.

Run: python3 build.py
"""
import html
import json
import sys
from pathlib import Path
from typing import NotRequired, TypedDict

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
CURRENT_VERSION = "4.1.0"                     # devices added in this release get a "New" tag
RENAMED = {"Mono Synth": "Overlord Synth"}    # renamed in 4.1.0; the source data still has the old name


# --- Output shapes -------------------------------------------------------------
# TypedDicts are Python's closest thing to a TS `type`: plain dicts at runtime,
# checked shapes for the reader and the editor. Key order is the JSON key order.

class Device(TypedDict):
    kind: str                     # "core" | "cap" | "plug"
    name: str                     # "Brit 800"
    basedOn: str                  # "Marshall JCM800 2203"; "" for original designs
    desc: str                     # our "what it's for" text
    added: str                    # CorOS version it arrived in, "3.2.0"
    isNew: bool
    prev: str                     # former name, "" if never renamed
    plugin: NotRequired[str]      # plugin devices only (like `plugin?: string`)

class Group(TypedDict):
    title: str                    # sub-heading inside a tab, "Guitar amps"; "" for none
    meta: NotRequired[str]        # plugin groups only: blurb + link, as trusted HTML
    items: list[Device]

class Section(TypedDict):
    id: str                       # tab id, also the section's DOM id
    title: str
    color: str                    # a CSS custom property from template.html, "--c-amp"
    blurb: str
    kind: str                     # which filter toggle hides it: "core" | "cap" | "plug"
    groups: list[Group]


# --- Inputs ----------------------------------------------------------------------

def load(name):
    return json.loads((DATA_DIR / name).read_text(encoding="utf-8"))


class Descriptions:
    """Lookup over the editorial text that records every key it can't find,
    so a new CorOS release can't silently ship blank rows."""

    def __init__(self, table):
        self.table = table
        self.missing = []

    def get(self, key, default=""):
        if key not in self.table:
            self.missing.append(key)
        return self.table.get(key, default)


# --- Builders ----------------------------------------------------------------------

def device(kind, name, based_on, desc, added, prev="", plugin=None) -> Device:
    d = Device(kind=kind, name=name, basedOn=based_on, desc=desc, added=added,
               isNew=added == CURRENT_VERSION, prev=prev)
    if plugin:
        d["plugin"] = plugin
    return d


def section(id, title, color, blurb, groups, kind="core") -> Section:
    return Section(id=id, title=title, color=color, blurb=blurb, kind=kind, groups=groups)


def group_by(items, key):
    """{key(item): [items...]}, first-seen order (Java's Collectors.groupingBy
    into a LinkedHashMap; Python dicts keep insertion order)."""
    groups = {}
    for item in items:
        groups.setdefault(key(item), []).append(item)
    return groups


def version_key(version):
    return tuple(int(part) for part in version.split("."))   # "4.1.0" -> (4, 1, 0), compares correctly


# --- The tabs ------------------------------------------------------------------------

def core_sections(devices_by_type, descriptions) -> list[Section]:
    def group(title, device_type) -> Group:
        items = []
        for raw in devices_by_type[device_type]:
            name = raw["name"]
            items.append(device(
                "core",
                name=RENAMED.get(name, name),
                based_on=raw.get("basedOn", ""),
                desc=descriptions.get(f"{device_type}|{name}"),
                added=raw.get("addedInCorOs", ""),
                prev=name if name in RENAMED else (raw.get("previousName") or ""),
            ))
        return Group(title=title, items=items)

    # One entry per tab, in display order. Several Neural DSP device types can
    # share a tab (Amps = guitar + bass amps); a "" group title means no sub-heading.
    return [
        section("amps", "Amps", "--c-amp", "Full amp models (preamp and power amp). Put a cab or IR after them unless you are feeding a real guitar cab.",
                [group("Guitar amps", "guitar_amps"), group("Bass amps", "bass_amps")]),
        section("cabs", "Cabs & IRs", "--c-cab", "Speaker cabinet simulations with selectable mics, plus IR loaders for third-party or your own impulse responses.",
                [group("Guitar cabinets", "guitar_cabinets"), group("Bass cabinets", "bass_cabinets"), group("IR loaders", "ir_loader")]),
        section("drive", "Overdrive & Fuzz", "--c-drive", "Drive, distortion, fuzz and boost pedals. Put them before an amp to push it or after a clean amp as the main dirt.",
                [group("Guitar overdrive", "guitar_overdrive"), group("Bass overdrive", "bass_overdrive")]),
        section("comp", "Compressor", "--c-dyn", "Dynamics control, from pedal-style squash to studio compressors.", [group("", "compressor")]),
        section("eq", "EQ", "--c-dyn", "Tone shaping and cleanup.", [group("", "eq")]),
        section("filter", "Filter", "--c-mod", "Envelope and synth-style filters.", [group("", "filter")]),
        section("wah", "Wah", "--c-mod", "Expression-controlled and automatic wahs.", [group("", "wah")]),
        section("pitch", "Pitch", "--c-pitch", "Octaves, harmonies, detune, whammy and tuning tools.", [group("", "pitch")]),
        section("mod", "Modulation", "--c-mod", "Chorus, flanger, phaser, vibe, tremolo, rotary and vibrato.", [group("", "modulation")]),
        section("morph", "Morph", "--c-pitch", "Experimental sound-mangling effects: bit crushing, freezing, glitching and ring mod.", [group("", "morph")]),
        section("delay", "Delay", "--c-time", "Echoes, from slapback to reverse and pitched multi-tap.", [group("", "delay")]),
        section("reverb", "Reverb", "--c-time", "Rooms, halls, plates, springs and ambient reverbs.", [group("", "reverb")]),
        section("synth", "Synth", "--c-pitch", "A guitar-driven synthesizer.", [group("", "synth")]),
        section("looper", "Looper", "--c-util", "Loop recording inside the grid.", [group("", "looper")]),
        section("util", "Utility", "--c-util", "Gates, gain, volume, blending, doubling and phase tools.", [group("", "utility")]),
    ]


def captures_section(v2_list, v1_list, descriptions) -> Section:
    # V2 captures carry a sub-category ("Guitar amps", "Fuzz pedals"...) that becomes
    # a group; V1 captures are one flat group at the end.
    v2_by_category = group_by(v2_list, lambda raw: raw["deviceCategory"])
    v2_groups = [
        Group(title=f"Neural Capture V2 · {category}", items=[
            device("cap", raw["name"], raw["basedOn"], descriptions.get(f"cap2|{raw['name']}"), raw["addedInCorOs"])
            for raw in captures
        ])
        for category, captures in v2_by_category.items()
    ]
    v1_group = Group(title="Neural Capture V1", items=[
        device("cap", raw["name"], raw.get("basedOn", ""), descriptions.get(f"cap1|{raw['name']}"),
               raw.get("addedInCorOs", ""), prev=raw.get("previousName") or "")
        for raw in v1_list
    ])
    return section("caps", "Factory Captures", "--c-cap",
        "Neural Captures made by Neural DSP from real amps and pedals, loaded in a Capture block. A capture is a snapshot of one setting, so its controls are simpler than a full model. V2 captures (CorOS 3.3.0+) are more accurate and include pedals and compressors.",
        v2_groups + [v1_group], kind="cap")


def plugins_section(device_list, descriptions, plugin_info) -> Section:
    def to_device(raw) -> Device:
        plugin, category = raw["requiredPlugin"], raw["deviceCategory"]
        # A name alone isn't unique across plugins and categories, hence the long key.
        entry = descriptions.get(f"plugin|{plugin}|{raw['name']}|{category}", {})
        return device("plug", raw["name"], entry.get("basedOn", ""), f"{category}. " + entry.get("desc", ""),
                      raw["addedInCorOs"], plugin=plugin)

    by_plugin = group_by(map(to_device, device_list), lambda d: d["plugin"])

    # Newest plugins first, then A-Z. A tuple key compares element by element, like
    # Comparator.comparing(newest).reversed().thenComparing(name); negating is the
    # usual way to get "descending" for one element.
    def newest_first(plugin):
        newest = max(version_key(d["added"]) for d in by_plugin[plugin])
        return tuple(-n for n in newest), plugin

    groups = []
    for plugin in sorted(by_plugin, key=newest_first):
        info = plugin_info.get(plugin, {})
        # The page inserts `meta` as raw HTML (it holds a link), so escape every part
        # here. All other fields are escaped in the browser by the template's esc().
        meta = html.escape(info.get("blurb", ""))
        if info.get("url"):
            meta += f' <a href="{html.escape(info["url"])}" target="_blank" rel="noopener">Plugin page</a>'
        groups.append(Group(title=plugin, meta=meta, items=by_plugin[plugin]))

    return section("plugins", "Plugin Devices", "--c-mod",
        "Devices from Neural DSP desktop plugins. They show up on the Quad Cortex only if you own a licence for that plugin. The 4.1.0 update added five Archetype X plugins.",
        groups, kind="plug")


# --- Output -----------------------------------------------------------------------------

def inject(template, sections):
    """Paste the data over the template's `/*DATA*/` placeholder (JSON is valid JS).
    ensure_ascii=False keeps "·" and curly quotes as-is instead of \\u escapes.
    '</' -> '<\\/' stops any "</script>" in the text from closing the script tag
    early; JS reads "<\\/" as "</", so the data itself is unchanged."""
    payload = json.dumps({"sections": sections}, ensure_ascii=False).replace("</", "<\\/")
    return template.replace("/*DATA*/", payload)


def as_document(fragment):
    """The template has no <html>/<head>/<body>. Everything up to </style> (title,
    meta, fonts, CSS) becomes <head>; the rest becomes <body>."""
    split = fragment.index("</style>") + len("</style>")
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + fragment[:split] + "\n</head>\n<body>\n" + fragment[split:] + "\n</body>\n</html>\n")


def main():
    # next.json is the page payload scraped from neuraldsp.com/device-list; the data
    # sits under props.pageProps, as Next.js hands it to the page.
    page_props = load("next.json")["props"]["pageProps"]
    devices_by_type = {g["deviceType"]: g["list"] for g in page_props["groups"]}

    # Keys look like "guitar_amps|Brit 800", "cap2|<name>", "plugin|<plugin>|<name>|<category>".
    core_text = {}
    for name in ["desc_amps.json", "desc_cabs.json", "desc_fx.json", "desc_caps.json"]:
        core_text |= load(name)   # dict merge, like Map.putAll
    descriptions = Descriptions(core_text)
    plugin_descriptions = Descriptions(load("desc_plugins.json"))

    sections = [
        *core_sections(devices_by_type, descriptions),
        captures_section(page_props["neuralCapturesV2List"], devices_by_type["neural_captures_v1"], descriptions),
        plugins_section(page_props["deviceList"], plugin_descriptions, load("plugins_meta.json")),
    ]

    missing = descriptions.missing + plugin_descriptions.missing
    if missing:   # warn on stderr, don't fail the build
        print("MISSING", len(missing), missing[:20], file=sys.stderr)

    # build/qc-block-atlas.html is the bare fragment (the claude.ai artifact is
    # published from it); index.html wraps it in a full document for GitHub Pages.
    fragment = inject((ROOT / "src" / "template.html").read_text(encoding="utf-8"), sections)
    (ROOT / "build").mkdir(exist_ok=True)
    (ROOT / "build" / "qc-block-atlas.html").write_text(fragment, encoding="utf-8")
    (ROOT / "index.html").write_text(as_document(fragment), encoding="utf-8")

    device_count = sum(len(g["items"]) for s in sections for g in s["groups"])
    print("ok", device_count, len(fragment))   # smoke check, e.g. "ok 632 193147"


if __name__ == "__main__":
    main()
