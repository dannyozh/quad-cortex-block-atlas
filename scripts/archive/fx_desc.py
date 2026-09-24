import json
D={}
def add(t,items):
    for k,v in items.items(): D[f"{t}|{k}"]=v
add("guitar_overdrive",{
"81 Creations Drive":"Model of the 1981 Inventions DRV, a modern boutique drive with a punchy, amp-like mid push and wide gain range. Great for tightening high-gain amps or as a gritty, articulate crunch into a clean amp.",
"Brit Blues":"Model of the Marshall Bluesbreaker pedal: low-to-medium gain, transparent, slightly scooped 'amp-in-a-box' breakup. Ideal for bluesy edge-of-breakup tones or a gentle push into an already driven amp.",
"Brit Governor":"Model of the Marshall Guv'nor, a 'Marshall stack in a box' distortion with an active EQ. Use it to turn a clean amp into classic British crunch and rock rhythm.",
"Chief BD2":"Model of the BOSS BD-2 Blues Driver: dynamic, touch-sensitive overdrive that cleans up with picking and volume. A go-to for edge-of-breakup blues and roots tones.",
"Chief DS1":"Model of the BOSS DS-1, the classic orange distortion with a bright, raspy, scooped voice. Good for punk, grunge and '80s rock rhythm, or as a cutting lead boost.",
"Chief MT":"Model of the BOSS MT-2 Metal Zone: high-gain distortion with a powerful semi-parametric mid EQ. Use for saturated metal tones straight into a clean amp, or dial the mids for surgical voicing.",
"Chief OD1":"Model of the BOSS OD-1, the first compact overdrive pedal: smooth, asymmetric, mid-forward clipping. Great as a vintage-flavoured boost into a crunchy amp.",
"Chief SD1":"Model of the BOSS SD-1 Super OverDrive, a Tube Screamer cousin with asymmetric clipping. Classic choice to tighten and push a high-gain amp for metal rhythm.",
"Exotic":"Model of the Xotic BB Preamp: a smooth, open overdrive with lots of headroom and a two-band active EQ. Useful as an always-on 'amp-like' drive or a clean-ish solo boost.",
"Exotic Z Boost":"Model of the Xotic RC Booster: a clean, transparent boost with active bass/treble EQ. Adds volume and a little extra gain for solos without changing your core tone much.",
"Facial Fuzz":"Model of the Dunlop Fuzz Face: a fat, round, vintage two-transistor fuzz that cleans up with your guitar's volume knob. Perfect for Hendrix-style leads and '60s rock tones.",
"Freeman BOD":"Model of the Friedman BE-OD, which packs the Friedman BE-100 high-gain voice into a pedal. Use it for aggressive modern rock crunch into a clean or lightly driven amp.",
"Fuzz Pi":"Model of the Electro-Harmonix Big Muff Pi: thick, sustaining, scooped fuzz with a violin-like decay. Built for wall-of-sound rhythm, stoner rock and singing leads.",
"Green 808":"Model of the Ibanez TS808 Tube Screamer: mid-humped, soft-clipping overdrive. The classic tool to tighten the low end and push a high-gain amp, or for warm blues lead.",
"MK3 Silicon Fuzz":"Model of the JHS Bender 1973 London, a silicon Tone Bender MkIII-style fuzz. Gives a raspy, aggressive '70s British fuzz with more bite than germanium designs.",
"Myth Drive":"Model of the Klon Centaur: a mild, transparent overdrive that blends clean signal with clipped signal. Beloved as a clean boost/light drive that adds mids and sparkle without masking the amp.",
"No-Bell OD1":"Model of the Nobels ODR-1: a warm, natural overdrive with a distinctive mid voicing and 'Spectrum' tone control. A Nashville session favourite for smooth, full-bodied drive.",
"Obsessive Drive":"Model of the Fulltone OCD: a versatile overdrive/distortion that ranges from light crunch to amp-like rock saturation. Great for turning a clean amp into a British-flavoured rock rig.",
"OD250":"Model of the DOD Overdrive Preamp 250: a simple, gritty op-amp drive with a slightly raw, edgy character. Good for vintage crunch and as a boost with some grit.",
"Rage Booster":"Model of the Dallas Rangemaster treble booster. Pushes upper mids and treble into a driven amp for classic '60s/'70s British lead tones (Clapton, May, Iommi).",
"Red Drive":"Model of the Keeley Red Dirt, a modded Tube Screamer-style drive with more gain and a fuller low end. Use as an always-on crunch or a tightening boost for rock.",
"Rodent Drive":"Model of the ProCo RAT: gritty hard-clipping distortion with a unique Filter control. Covers everything from bluesy crunch to buzzy fuzz-like grind; loved in grunge and alt-rock.",
"Thunderpaw":"Model of the Mr Black Thunderclaw, a vintage Tone Bender MkI-style fuzz with a raw, splatty, ripping character. For garage rock and '60s psych fuzz tones.",
"Vemural Ray":"Model of the Vemuram Jan Ray: a transparent, dynamic 'Blackface Fender in a box' overdrive. Ideal for sparkly edge-of-breakup and a touch-sensitive always-on drive.",
})
add("bass_overdrive",{
"BDDI":"Model of the Tech 21 SansAmp Bass Driver DI: amp-style preamp, drive and DI in one. The studio/live staple for gritty, punchy bass straight to the desk.",
"Exotic Bass Z Boost":"Model of the Xotic RC Bass Booster: a clean boost with active EQ tailored to bass. Adds level and shape for fills or a fuller bass presence.",
"Douglas MT 3K":"Model of the Darkglass Microtubes B3K: aggressive, modern bass distortion that blends drive with the clean low end. The go-to for metal and punchy grind bass.",
"Douglas Vintage MT":"Model of the Darkglass Vintage Microtubes: a warmer, more vintage-flavoured bass overdrive with blend. Good for classic rock grit that keeps the bass fundamental intact.",
"Soviet Fuzz":"Model of the Electro-Harmonix 'Russian' Big Muff: darker, bassier, smoother fuzz than the US version. A favourite for fuzz bass and fat stoner/doom guitar.",
})
add("delay",{
"Analog Delay":"Neural DSP emulation of a bucket-brigade analog delay: warm, darkened repeats that degrade as they decay. Great for sitting behind leads without cluttering the mix.",
"Slapback Delay":"Short single-repeat delay voiced for classic rockabilly and country slapback. Adds depth and thickness to rhythm and chicken-picking parts.",
"Digital Delay":"Clean, pristine digital delay with accurate repeats. Use for rhythmic dotted-eighth parts, clear echoes and modern ambient layers.",
"Dual Delay":"Two independent delay lines in one block, each with its own time and feedback. Useful for complex rhythmic patterns or wide stereo echoes.",
"Dual Reverse Delay":"Two reverse delay lines, playing chunks of your signal backwards. Creates swelling, psychedelic, backwards-guitar textures with extra width.",
"Simple Ping Pong Delay":"Straightforward stereo delay whose repeats bounce between left and right. Great for wide, spacious rhythmic echoes.",
"Reverse Delay":"Records and plays back your signal in reverse. Delivers backwards swells for psychedelic leads and ambient textures.",
"Simple Delay":"No-frills digital delay with the essential controls. Quick to dial for everyday echo duties.",
"Tape Delay":"Emulation of a tape echo with warm, saturated, slightly wobbly repeats. Ideal for vintage slapback, dub echoes and lo-fi character.",
"Circular Delay":"Delay that outputs a patterned 'chunk' of syncopated repeats chosen by a Tap Preset, circling gradually around the stereo field. For rhythmic patterns a normal single delay can't produce.",
"Arpeggio Delay":"New in 4.1.0: a multi-tap delay where each repeat gets its own pitch and stereo position. Turns single notes into melodic echoes and evolving arpeggiated patterns.",
"Crystal Delay":"New in 4.1.0: produces bright, shimmering, pitched-up repeats that sit above the original signal. Great for ethereal leads and ambient swells.",
})
add("reverb",{
"Ambience":"Short, subtle reverb that adds space without an obvious tail. Use it to make a dry tone sound like it's in a real room.",
"Blossom (ST)":"Stereo reverb inspired by the Strymon BigSky's Bloom mode: lush tails that swell and 'bloom' after the note. For ambient pads and cinematic textures.",
"Cave":"Large, dark, cavernous reverb with long reflections. Ideal for atmospheric and dramatic effects.",
"Hall":"Classic concert-hall reverb with smooth, long decay. A versatile choice for leads, cleans and ballads.",
"Mind Hall":"Large, lush, modulated hall-style reverb with an expansive, dreamy character. Suited to ambient and post-rock soundscapes.",
"Modulated":"Reverb with modulation in the tail for a chorused, swirling decay. Adds movement to cleans and ambient parts.",
"Nordic Concert Hall (ST)":"Stereo reverb inspired by Valhalla VintageVerb's Concert Hall mode: a smooth, vintage-digital hall. Big, polished space for leads and cleans.",
"Plate":"Emulation of a classic studio plate reverb: bright, dense, smooth. The studio standard for vocals and guitar.",
"Plate Lush":"Plate reverb variant with a longer, richer, more lush tail. For big, washy ballad and ambient sounds.",
"Plate Tight":"Plate reverb variant with a shorter, tighter decay. Adds sheen without clutter for rhythm parts.",
"Room":"Natural room reverb simulating small-to-medium spaces. Makes an amp sound 'in the room' rather than direct.",
"Shimmer":"Reverb with pitch-shifted (typically octave-up) feedback for an angelic, choir-like shimmer. A staple of ambient and worship guitar.",
"Spring (M)":"Mono spring reverb emulating the drippy, splashy tank in vintage amps. For surf, rockabilly and classic Fender-style cleans.",
"Spring (ST)":"Stereo version of the spring reverb emulation: vintage amp-tank drip with width.",
"Spring Reverb Engine (M)":"Mono, more detailed and tweakable spring reverb engine with extended controls over the spring tank's behaviour. For authentic vintage spring sounds.",
"Spring Reverb Engine (ST)":"Stereo version of the advanced spring reverb engine, with deep control over tank character and spread.",
"Studio Plate 70 (ST)":"Stereo reverb based on the Lexicon PCM70 Rich Plate programs: that '80s studio-rack plate sheen. Classic for polished lead and clean tones.",
"Vintage Digital":"New in 4.1.0: based on the OTO Machines BAM Space Generator, recreating vintage digital reverb with lo-fi character, plus a Freeze function for infinite sustain pads.",
})
add("compressor",{
"Chief CS3":"Model of the BOSS CS-3 Compression Sustainer: squishy pedal compression with added sustain. Classic for funk, country chicken-picking and even-sounding cleans.",
"Jewel":"Model of the Diamond Compressor: a transparent optical-style pedal comp with a tilt EQ. Evens out dynamics subtly while keeping pick attack.",
"Legendary 87":"Model of the Universal Audio 1176 FET studio compressor: fast, punchy, aggressive. Great for snappy attack and in-your-face guitar or bass.",
"Legendary 87 (ST)":"Stereo version of the 1176-based compressor, for stereo rigs and post-effects compression.",
"Legendary 87 (S/C)":"Sidechain version of the 1176-based compressor: its detector can be triggered by another signal (e.g. a separate input), for ducking and pumping effects.",
"Opto Comp":"Optical-style compressor with smooth, program-dependent, musical response (LA-2A-flavoured). Gentle levelling for cleans and bass.",
"Opto Comp (ST)":"Stereo version of the optical-style compressor.",
"Opto Comp (S/C)":"Sidechain version of the optical-style compressor, triggered by another signal source for ducking effects.",
"Solid State Comp":"Model of the SSL Bus compressor: the classic 'glue' compressor from SSL consoles. Adds cohesion and punch at the end of a chain.",
"Solid State Comp (ST)":"Stereo version of the SSL Bus-based compressor, ideal as a final stereo glue stage.",
"Solid State Comp (S/C)":"Sidechain version of the SSL Bus-based compressor, keyed from another signal for ducking/pumping.",
"VCA Comp":"Clean, precise VCA-style compressor with fast, controlled response. Good for tightening dynamics transparently.",
"VCA Comp (ST)":"Stereo version of the VCA-style compressor.",
"VCA Comp (S/C)":"Sidechain version of the VCA-style compressor, driven by an external/secondary signal.",
"Douglas Shining Comp (M)":"New in 4.1.0 (mono): based on the Darkglass Hyper Luminal, a bass-focused compressor with VCA/FET-style modes. Handles both subtle levelling and pronounced squash.",
})
add("pitch",{
"Aggi Sub Octaver":"Model of the Aguilar Octamizer: an analog-style octave-down that adds a clean sub octave. Fattens bass and baritone-style riffs.",
"Chief OC2":"Model of the BOSS OC-2 Octave: classic analog one- and two-octave-down tracking. Thick, synthy low end for bass and guitar riffs.",
"Minivoicer":"Compact harmonizer adding intelligent pitch-shifted voices to your signal. For quick harmony leads and thickening.",
"Pitch Correction":"Pitch-correcting effect that snaps notes toward a chosen key/scale, including hard auto-tune-style robotic effects.",
"Pitch Shifter":"General pitch shifter to transpose your signal by fixed intervals, mixed with the dry signal. For octaves, fifths, and harmony layers.",
"Poly Octaver":"Model of the Electro-Harmonix POG: polyphonic octave generator with sub and upper octaves. Creates organ-like, 12-string and huge layered tones.",
"Subharmonic Synth":"Model of the DOD Meatbox SubSynth: generates deep subharmonic frequencies under your notes. Massive sub bass for bass guitar and drop tunings.",
"Transpose":"Full-wet pitch shift of your whole signal, like a virtual capo or drop-tuning. Play in a different key or tuning without retuning.",
"Wham":"Model of the DigiTech Whammy: expression-controlled pitch bends, dive bombs and harmonies. The classic Tom Morello/Jack White pitch pedal.",
"Multivoicer":"New in 4.1.0: from Archetype: Tim Henson X, now free. Adds up to four pitch-shifted voices for rich, layered harmonies and arpeggios.",
})
add("modulation",{
"Chief CE2W":"Model of the BOSS CE-2W (Waza Craft CE-2): warm, lush, analog BBD chorus. The classic '80s chorus for cleans and shimmering leads.",
"Chief CE2W (M)":"Mono version of the BOSS CE-2W-based chorus.",
"Chief DC2W":"Model of the BOSS DC-2W Dimension C: subtle, spacious stereo chorus without obvious wobble. Widens tones while staying clean and natural.",
"Chief DC2W (M)":"Mono version of the BOSS DC-2W Dimension-based chorus.",
"Chorus 229T":"Model of the TC Electronic TC 2290's chorus: the pristine, hi-fi rack chorus of '80s session players. Clean, wide shimmer.",
"Chorus Engine":"Neural DSP's deep, fully tweakable chorus engine. Dial anything from subtle thickening to heavy warble.",
"Digital Flanger":"Clean digital flanger with a crisp, jet-like sweep. For classic swoosh effects and metallic textures.",
"Dream Chorus":"Model of the TC Electronic Dreamscape (John Petrucci's signature chorus/flanger pedal): lush, wide chorus. Great for clean arpeggios.",
"Dream Chorus (M)":"Mono version of the TC Dreamscape-based chorus.",
"Dual Chorus":"Two chorus voices for a thicker, wider stereo chorus. For big, lush clean tones.",
"Flanger Engine":"Neural DSP's deep, tweakable flanger engine. From subtle comb-filter movement to extreme jet sweeps.",
"Flangerish":"Neural DSP's flanger with a classic, musical sweep. Quick-to-dial flanging for rock and psych tones.",
"Harmonic Tremolo":"Emulation of the harmonic tremolo in early-'60s Brownface Fender amps: splits highs and lows and modulates them out of phase for a phasey, swirling pulse.",
"Micro Processor (ST)":"Stereo effect based on the Eventide MicroPitch Delay: micro pitch detune plus delay for wide, doubled, chorus-like widening. A studio favourite for stereo width.",
"MX Flanger":"Model of the MXR M117R Flanger: rich, analog, jet-plane flanging. Classic Van Halen-era swoosh.",
"MX Phase 95":"Model of the MXR Phase 95, combining the Phase 45 and Phase 90 (plus script mode). Classic swirling phase for funk, rock and leads.",
"MX Vibes":"Model of the MXR Uni-Vibe: throbbing, chorus/phaser-like pulse with a lopsided sweep. The Hendrix/Trower/Gilmour vibe sound.",
"Pattern Tremolo":"Tremolo that chops volume in programmable rhythmic step patterns rather than a smooth wave. For stuttering, sequenced gate-like rhythms.",
"Phaser":"Neural DSP's phaser with adjustable stages and sweep. Classic swirling phase-shift modulation.",
"Rotary":"Emulation of a rotating Leslie-style speaker cabinet with slow/fast rotor. For organ-like swirl on guitar and keys.",
"Tremolo":"Classic amplitude tremolo that pulses your volume. For vintage surf, country and atmospheric parts.",
"Vibrato":"Pitch vibrato that wobbles the pitch periodically (fully wet). For warbly, seasick, lo-fi and vintage vibrato tones.",
"Vintage Chorus":"Warm, analog-flavoured chorus. Simple, classic chorus for cleans.",
})
add("morph",{
"Bit-Crusher (ST)":"Stereo bit-crusher that reduces bit depth and sample rate for lo-fi, digital grit. For glitchy, 8-bit and destroyed textures.",
"Bit-Crusher Engine (M)":"Mono bit-crusher engine with deeper control over sample-rate and bit reduction. For lo-fi and aliasing effects.",
"Freeze":"Captures and holds a slice of your sound indefinitely as a sustained pad. Play over a frozen chord or create ambient drones.",
"Phase-Locked Loop":"Based on the EarthQuaker Devices Data Corrupter: a PLL harmonizing fuzz/synth that tracks your pitch and generates square-wave synth voices. Wild, glitchy monophonic synth tones.",
"Glitch":"New in 4.1.0: from Archetype: Misha Mansoor X, now free. A granular delay that chops your signal into repeating patterns, from subtle movement to heavily distorted textures.",
"Ring Modulator":"New in 4.1.0: multiplies your signal with a carrier oscillator for metallic, bell-like, inharmonic tones. For sci-fi and experimental effects.",
})
add("filter",{
"Env. Filter":"Envelope filter (auto-wah) whose sweep follows your picking dynamics. For funk 'quack' and bass synth tones.",
"Env. filter (S/C)":"Sidechain version of the envelope filter: the sweep is triggered by a different signal than the one being filtered.",
"Foog":"Model of the Moog Moogerfooger MF-101 Low-Pass Filter: resonant Moog ladder filter with envelope follower. For synthy, funky and vowel-like filtering.",
"Love Meat":"Model of the Lovetone Meatball: a highly tweakable envelope filter. Deep, squelchy funk and synth-like auto-wah sounds.",
})
add("eq",{
"Graphic-9":"9-band graphic EQ for broad tone shaping. Sculpt mids, tame fizz or add low end quickly.",
"Low-High Cut":"Simple high-pass and low-pass filter. Remove rumble and fizz; essential for cleaning up mixes.",
"Parametric-3":"3-band parametric EQ with adjustable frequency, gain and Q. For precise, surgical tweaks.",
"Parametric-8":"8-band parametric EQ for detailed studio-grade shaping.",
"Plugin Graphic-9":"Graphic EQ matching the exact controls/ranges of the Archetype plugins' graphic EQ. Use it to recreate plugin presets accurately.",
"Plugin Parametric-4":"New in 4.1.0: four-band parametric EQ with high-pass and low-pass filters, matching the plugins' parametric EQ, for precise tone shaping.",
})
add("wah",{
"Auto Wah":"Wah that sweeps automatically via LFO or envelope, no expression pedal needed. For funky, rhythmic wah.",
"Bad Horse":"Model of the Morley Bad Horsie (Steve Vai signature): optical, switchless wah with a wide, vocal sweep.",
"Bass Wah":"Wah voiced for bass with a lower sweep range, keeping low end intact.",
"Bubba Wah":"Model of the Dunlop Budda Budwah: smooth, vocal wah with a wide range and warm character.",
"Crying Clyde Wah":"Model of the Dunlop Cry Baby Clyde McCoy: vintage-voiced wah with a vocal, throaty sweep. Classic '60s wah.",
"Crying Wah":"Model of the Dunlop Cry Baby GCB-95: the standard, bright, classic rock wah.",
"Crying Wah From Hell":"Model of the Dunlop Crybaby From Hell (Dimebag Darrell signature): wide-range, aggressive wah with boost. Metal leads.",
})
add("looper",{
"Looper X":"Full-featured looper with overdub, undo, reverse, half-speed and quantization. For practice, songwriting and live looping.",
})
add("synth",{
"Mono Synth":"Renamed Overlord Synth in 4.1.0: a free, enhanced version of the Overlord Synth from Archetype: Rabea X. Monophonic guitar-driven synth for leads and bass lines.",
})
add("utility",{
"Adaptive Gate":"Noise gate that adapts to your signal, adjusting threshold dynamically. Keeps high-gain tones quiet between notes.",
"Adaptive Gate (S/C)":"Sidechain version of the adaptive gate: it can listen to the clean input (before the amp) to gate the distorted signal more precisely.",
"Gain":"Simple level control. Boost or cut signal level anywhere in the chain.",
"Simple Gate":"Basic noise gate with threshold. Silences hiss and hum.",
"Utility Gate":"Noise gate with fuller controls (threshold, attack, release, etc.) for precise noise control.",
"Volume":"Volume block, usually assigned to an expression pedal for volume swells and level control.",
"Phase Doctor":"Inspired by the Little Labs IBP Phase Alignment Tool: adjusts phase between parallel paths to fix phase cancellation when blending signals or cabs.",
"Plugin Gate":"Noise gate matching the Archetype plugins' gate, for accurate recreation of plugin presets.",
"Doubler":"Creates a double-tracked effect, simulating two guitar takes for width. In 4.1.0 an INPUT three-way switch was added.",
"Plugin Doubler":"Doubler matching the Archetype plugins' doubler exactly. In 4.1.0 an INPUT three-way switch was added.",
"Plugin Blend":"Blends a signal from elsewhere in the chain in parallel with the processed signal, with the plugins' fixed EQ/compression; for recreating plugin presets. 4.1.0 added a BLEND LEVEL knob.",
"Transparent Blend":"Blends a signal from another point in your chain (e.g. the direct input) with the processed signal, transparently. 4.1.0 added a BLEND LEVEL knob.",
})
d=json.load(open('next.json'))['props']['pageProps']
want=set()
types="guitar_overdrive bass_overdrive delay reverb compressor pitch modulation morph filter eq wah looper synth utility".split()
for g in d['groups']:
    if g['deviceType'] in types:
        for x in g['list']: want.add(f"{g['deviceType']}|{x['name']}")
print("missing",want-set(D)); print("extra",set(D)-want)
json.dump(D,open('desc_fx.json','w'),ensure_ascii=False,indent=1); print(len(D))
