import json, os, html, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
P = json.load(open('data/next.json'))['props']['pageProps']
D = {}
for f in ['desc_amps.json', 'desc_cabs.json', 'desc_fx.json', 'desc_caps.json']:
    D.update(json.load(open('data/' + f)))
PL = json.load(open('data/desc_plugins.json'))
PM = json.load(open('data/plugins_meta.json'))
G = {g['deviceType']: g['list'] for g in P['groups']}
missing = []

def core(dt, x):
    name = x['name']
    key = f"{dt}|{name}"
    desc = D.get(key)
    if desc is None: missing.append(key); desc = ''
    bo = x.get('basedOn', '')
    if name == 'Mono Synth':
        name = 'Overlord Synth'
    prev = x.get('previousName') or ''
    if x['name'] == 'Mono Synth': prev = 'Mono Synth'
    return dict(kind='core', name=name, basedOn=bo, desc=desc, added=x.get('addedInCorOs', ''),
                isNew=x.get('addedInCorOs') == '4.1.0', prev=prev)

def sec(id, title, color, blurb, groups, kind='core'):
    return dict(id=id, title=title, color=color, blurb=blurb, kind=kind, groups=groups)

def grp(title, dt):
    return dict(title=title, items=[core(dt, x) for x in G[dt]])

sections = [
    sec('amps', 'Amps', '--c-amp', 'Full amp models (preamp and power amp). Put a cab or IR after them unless you are feeding a real guitar cab.',
        [grp('Guitar amps', 'guitar_amps'), grp('Bass amps', 'bass_amps')]),
    sec('cabs', 'Cabs & IRs', '--c-cab', 'Speaker cabinet simulations with selectable mics, plus IR loaders for third-party or your own impulse responses.',
        [grp('Guitar cabinets', 'guitar_cabinets'), grp('Bass cabinets', 'bass_cabinets'), grp('IR loaders', 'ir_loader')]),
    sec('drive', 'Overdrive & Fuzz', '--c-drive', 'Drive, distortion, fuzz and boost pedals. Put them before an amp to push it or after a clean amp as the main dirt.',
        [grp('Guitar overdrive', 'guitar_overdrive'), grp('Bass overdrive', 'bass_overdrive')]),
    sec('comp', 'Compressor', '--c-dyn', 'Dynamics control, from pedal-style squash to studio compressors.', [grp('', 'compressor')]),
    sec('eq', 'EQ', '--c-dyn', 'Tone shaping and cleanup.', [grp('', 'eq')]),
    sec('filter', 'Filter', '--c-mod', 'Envelope and synth-style filters.', [grp('', 'filter')]),
    sec('wah', 'Wah', '--c-mod', 'Expression-controlled and automatic wahs.', [grp('', 'wah')]),
    sec('pitch', 'Pitch', '--c-pitch', 'Octaves, harmonies, detune, whammy and tuning tools.', [grp('', 'pitch')]),
    sec('mod', 'Modulation', '--c-mod', 'Chorus, flanger, phaser, vibe, tremolo, rotary and vibrato.', [grp('', 'modulation')]),
    sec('morph', 'Morph', '--c-pitch', 'Experimental sound-mangling effects: bit crushing, freezing, glitching and ring mod.', [grp('', 'morph')]),
    sec('delay', 'Delay', '--c-time', 'Echoes, from slapback to reverse and pitched multi-tap.', [grp('', 'delay')]),
    sec('reverb', 'Reverb', '--c-time', 'Rooms, halls, plates, springs and ambient reverbs.', [grp('', 'reverb')]),
    sec('synth', 'Synth', '--c-pitch', 'A guitar-driven synthesizer.', [grp('', 'synth')]),
    sec('looper', 'Looper', '--c-util', 'Loop recording inside the grid.', [grp('', 'looper')]),
    sec('util', 'Utility', '--c-util', 'Gates, gain, volume, blending, doubling and phase tools.', [grp('', 'utility')]),
]

# Captures
v2 = []
for x in P['neuralCapturesV2List']:
    key = f"cap2|{x['name']}"
    if key not in D: missing.append(key)
    v2.append(dict(kind='cap', name=x['name'], basedOn=x['basedOn'], desc=D.get(key, ''), added=x['addedInCorOs'],
                   isNew=False, prev='', sub=x['deviceCategory']))
v2groups = {}
for d in v2: v2groups.setdefault(d.pop('sub'), []).append(d)
v1 = []
for x in G['neural_captures_v1']:
    key = f"cap1|{x['name']}"
    if key not in D: missing.append(key)
    prev = x.get('previousName') or ''
    v1.append(dict(kind='cap', name=x['name'], basedOn=x.get('basedOn', ''), desc=D.get(key, ''), added=x.get('addedInCorOs', ''),
                   isNew=False, prev=prev))
sections.append(sec('caps', 'Factory Captures', '--c-cap',
    'Neural Captures made by Neural DSP from real amps and pedals, loaded in a Capture block. A capture is a snapshot of one setting, so its controls are simpler than a full model. V2 captures (CorOS 3.3.0+) are more accurate and include pedals and compressors.',
    [dict(title=f'Neural Capture V2 · {k}', items=v) for k, v in v2groups.items()] + [dict(title='Neural Capture V1', items=v1)], kind='cap'))

# Plugins
pg = {}
for x in P['deviceList']:
    rp = x['requiredPlugin']
    key = f"plugin|{rp}|{x['name']}|{x['deviceCategory']}"
    e = PL.get(key)
    if e is None: missing.append(key); e = {'basedOn': '', 'desc': ''}
    pg.setdefault(rp, []).append(dict(kind='plug', name=x['name'], basedOn=e.get('basedOn', ''),
        desc=f"{x['deviceCategory']}. " + e.get('desc', ''), added=x['addedInCorOs'], isNew=x['addedInCorOs'] == '4.1.0', prev='', plugin=rp))
order = sorted(pg, key=lambda k: (-max(float(d['added'][:3]) for d in pg[k]), k))
pgroups = []
for rp in order:
    m = PM.get(rp, {})
    meta = html.escape(m.get('blurb', ''))
    if m.get('url'): meta += f' <a href="{html.escape(m["url"])}" target="_blank" rel="noopener">Plugin page</a>'
    pgroups.append(dict(title=rp, meta=meta, items=pg[rp]))
sections.append(sec('plugins', 'Plugin Devices', '--c-mod',
    'Devices from Neural DSP desktop plugins. They show up on the Quad Cortex only if you own a licence for that plugin. The 4.1.0 update added five Archetype X plugins.',
    pgroups, kind='plug'))

if missing:
    print('MISSING', len(missing), missing[:20], file=sys.stderr)
t = open('src/template.html').read()
out = t.replace('/*DATA*/', json.dumps({'sections': sections}, ensure_ascii=False).replace('</', '<\\/'))

# build/qc-block-atlas.html is the bare fragment (what the claude.ai artifact is published from);
# index.html wraps it in a full document for GitHub Pages.
os.makedirs('build', exist_ok=True)
open('build/qc-block-atlas.html', 'w').write(out)
i = out.index('</style>') + len('</style>')
page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + out[:i] + '\n</head>\n<body>\n' + out[i:] + '\n</body>\n</html>\n')
open('index.html', 'w').write(page)
print('ok', sum(len(g['items']) for s in sections for g in s['groups']), len(out))
