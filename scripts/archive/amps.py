import json
D={}
g='guitar_amps'; b='bass_amps'
def s(t,n,x): D[f"{t}|{n}"]=x
uc="Bogner's Uberschall is a brutally tight, saturated high-gain head built for modern metal. "
s(g,"Bogna Uber Clean",uc+"This is its clean channel: firm, punchy cleans with plenty of low end, handy for metal songs' quiet parts.")
s(g,"Bogna Uber Lead",uc+"The lead channel delivers thick, compressed, aggressive distortion for down-tuned riffing and chugs.")
s(g,"Bogna Vishnu 20th Clean","Clean channel of Bogner's Shiva 20th Anniversary: rich, touch-sensitive cleans that break up gently when pushed. Great for worship, pop, blues and edge-of-breakup rhythm parts.")
s(g,"Brit 2203","The Marshall JCM800 2203, the defining '80s rock and metal head. Tight, bright, crunchy single-channel master-volume gain that loves a Tube Screamer in front; classic hard rock, punk and thrash.")
for v,t in [("Clean","Its clean channel is bright and crisp, and fine for chimey rhythm or as a pedal platform."),("Lead","The lead channel adds a heavier, more compressed '90s Marshall distortion for hard rock, grunge and solos.")]:
    s(g,f"Brit 900 {v}","Marshall JCM900 4100, the dual-channel '90s Marshall. "+t)
pl={"Bright":"the Bright (high treble) input: more sparkle and bite, good for humbuckers or dark cabs.","Normal":"the Normal input: warmer and fuller, suits bright single-coils.","Patch":"both inputs jumpered (patched) together, blending Bright and Normal for the classic full-bodied plexi roar."}
for n,v in pl.items():
    s(g,f"Brit Plexi 100 {n}","Marshall Super Lead 100 'Plexi', the loud, open non-master-volume sound of classic rock. This version uses "+v)
    s(g,f"Brit Plexi 50 {n}","Marshall 50W Plexi-era head: like the 100W but compresses and breaks up earlier, for AC/DC-style crunch and '60s–'70s rock. This version uses "+v)
    s(g,f"Brit TM45 {n}","Marshall JTM45, the first Marshall (Bassman-derived, KT66 power tubes). Warm, round, bluesy breakup for classic blues-rock. This version uses "+v)
s(g,"Brit UBL Lead","Marshall Silver Jubilee (2555) lead mode: smooth, saturated, mid-forward Marshall gain made famous by Slash. Great for '80s–'90s hard rock rhythm and singing solos.")
s(g,"Brit UBL Lead Clip","Marshall Silver Jubilee with the diode clipping ('rhythm clip') engaged: more gain and compression than the standard lead mode, for thicker hard-rock rhythms and sustaining leads.")
ls="Mesa/Boogie Lone Star, a boutique-leaning Mesa built for clean and blues tones. "
for w in ["100W","50W"]:
    for m,mt in [("Normal","Normal mode is fuller and tighter"),("Tweed","Tweed mode loosens and warms the response like a vintage Fender")]:
        s(g,f"CA 1Star Clean {w} {m}",ls+f"Channel 1 clean at {w}: lush, glassy cleans with lots of headroom (less at 50W). {mt}.")
        s(g,f"CA 1Star Drive {w} {m}",ls+f"Channel 2 drive at {w}: smooth, vocal overdrive for blues, country and classic rock leads. {mt}.")
rec="Mesa/Boogie Dual Rectifier channel 3, the heaviest channel of the '90s nu-metal and modern-rock staple. "
s(g,"CA Duo Ch3 Modern",rec+"Modern mode is the famous scooped, saturated, aggressive high-gain sound for drop-tuned metal.")
s(g,"CA Duo Ch3 Raw",rec+"Raw mode has less gain and a looser, more open voice for gritty hard rock and crunch.")
s(g,"CA Duo Ch3 Vintage",rec+"Vintage mode is tighter and more mid-focused with less saturation; great for classic metal and cutting leads.")
jp="Mesa/Boogie JP-2C, John Petrucci's Mark IIC+-based signature head. "
s(g,"CA John’s 2C Ch1",jp+"Channel 1 is the clean: sparkling, hi-fi cleans with a pull-bright character, ideal for arpeggios and ambient parts.")
s(g,"CA John’s 2C Ch2",jp+"Channel 2 is the IIC+ lead voice: tight, focused, mid-forward high gain for progressive metal rhythm.")
s(g,"CA John’s 2C Ch3",jp+"Channel 3 is the lead channel: the same IIC+ core with extra saturation and sustain for singing, fluid solos.")
s(g,"CA Tremo Orange","Mesa/Boogie Trem-O-Verb, orange (lead) channel: Rectifier-family gain, looser and vintage-voiced for crunchy rock and '90s alternative.")
s(g,"CA Tremo Red","Mesa/Boogie Trem-O-Verb, red channel: the higher-gain side of this Rectifier-family combo, for saturated modern rock and heavy rhythm.")
s(g,"Captain 50","Morgan SW50, Steve Wariner's signature: a boutique, Fender blackface-inspired design with sparkling, articulate cleans and sweet breakup. Suits country, blues and pop.")
vh="Diezel VH4, the German four-channel high-gain benchmark, tight and articulate with a distinctive midrange. "
s(g,"D-Cell H4 Ch1 Bright",vh+"Channel 1 clean with the bright switch on: crisp, glassy cleans.")
s(g,"D-Cell H4 Ch1 Normal",vh+"Channel 1 clean in normal mode: warm, full, big-headroom cleans.")
s(g,"D-Cell H4 Ch2 Bright",vh+"Channel 2 crunch, bright: edgy rhythm crunch with extra top end for classic rock.")
s(g,"D-Cell H4 Ch2 Normal",vh+"Channel 2 crunch, normal voicing: warmer rock crunch that cleans up with volume.")
s(g,"D-Cell H4 Ch3",vh+"Channel 3 is the famous heavy rhythm sound: dense, focused, modern metal saturation with huge low end.")
s(g,"D-Cell H4 Ch4",vh+"Channel 4 is the lead: more gain and a mid-boosted voice for singing solos.")
hb="Diezel Herbert, a three-channel high-gain head, a bit looser and more aggressive than the VH4. "
s(g,"D-Cell Hisbert Ch1",hb+"Channel 1: big clean-to-crunch channel for cleans and light breakup.")
s(g,"D-Cell Hisbert Ch2",hb+"Channel 2: thick, heavy rhythm crunch, great for alt-metal and hard rock.")
s(g,"D-Cell Hisbert Ch3",hb+"Channel 3: highest-gain, saturated lead/rhythm tone for modern metal.")
s(g,"Dumbbell ODS","Dumble Overdrive Special, the holy-grail boutique amp. Warm, singing, hugely touch-sensitive overdrive and fat cleans: think Robben Ford or John Mayer blues and fusion leads.")
e5="EVH 5150 III 100S, Eddie Van Halen's three-channel modern high-gain head. "
s(g,"EV101IIIS Blue 6L6 100W",e5+"Blue (crunch) channel with 6L6 power tubes: tight, punchy crunch for classic hard rock and Van Halen-style rhythm.")
s(g,"EV101IIIS Red 6L6 100W",e5+"Red (lead) channel with 6L6 tubes: tight, aggressive, heavily saturated metal tones with firm lows.")
s(g,"EV101IIIS Blue EL34 100W","EVH 5150 III EL34 version, blue (crunch) channel: EL34s bring a more British, mid-forward bite to the 5150 III crunch; great for rock rhythm.")
s(g,"EV101IIIS Red EL34 100W","EVH 5150 III EL34 version, red (lead) channel: thick, saturated high gain with the grindier EL34 midrange, for metal rhythms and leads.")
fr="Friedman HBE-100 (Hairy Brown Eye), a hot-rodded Marshall-style boutique head. "
s(g,"Freeman 100 Clean",fr+"Clean channel: Plexi-flavored cleans that crunch up as you dig in.")
s(g,"Freeman 100 Rhythm",fr+"The BE channel in rhythm mode: tight, aggressive modded-Marshall crunch for hard rock riffs.")
s(g,"Freeman 100 Lead",fr+"The HBE lead mode: more gain, compression and sustain for leads and heavier rock.")
s(g,"Matchmore D30 Ch1","Matchless DC30, channel 1: the EL84, class-A Vox-inspired boutique voice. Chimey, harmonically rich cleans and crunch, a studio favorite for jangle and indie rock.")
s(g,"Matchmore D30 Ch2","Matchless DC30, channel 2: the EF86-driven channel, thicker and more complex than channel 1, with rich, touch-sensitive breakup.")
s(g,"Matchmore Jefe","Matchless Chieftain: EL34 class-A boutique amp, chimey like the DC30 but with more headroom and punch. Great for clean-to-crunch rock, country and blues.")
s(g,"PV-505 Lead","Peavey 6505 (5150) lead channel: the definitive metalcore/modern metal rhythm tone, tight, aggressive and saturated, especially with an overdrive boost in front.")
s(g,"PV-505 Rhythm","Peavey 6505 rhythm channel: cleans at low gain, raw crunch as you turn it up; with the gain maxed it's a gritty, lower-gain metal and punk tone.")
s(g,"Rols Jazz CH120","Roland JC-120 Jazz Chorus, the solid-state clean king. Ultra-clear, stiff cleans with loads of headroom: jazz, new wave, funk, ambient and a clean pedal platform.")
sl="Soldano SLO-100, the classic '80s hot-rod high-gain head. "
s(g,"Solo 100 Crunch Bright",sl+"Crunch channel with bright on: snappy, sparkly rock crunch.")
s(g,"Solo 100 Crunch Normal",sl+"Crunch channel, normal voicing: warmer, fuller crunch and cleans that clean up with the guitar's volume.")
s(g,"Solo 100 Lead",sl+"Overdrive channel: smooth, saturated, singing high gain famous on '80s–'90s rock and metal leads.")
s(g,"UK C15 Normal","Vox AC15, normal channel: the EL84 class-A British chime in a 15W package, sweet and slightly darker. Breaks up early, ideal for Beatles-style jangle and indie.")
s(g,"UK C15 TopBoost","Vox AC15, top boost channel: brighter, more gain and treble/bass tone controls, for chimey crunch and indie/Britpop rhythm.")
s(g,"UK C30 Normal","Vox AC30, normal channel: 30W of class-A EL84 chime, simpler and warmer than the top boost. Classic British pop/rock cleans and crunch.")
s(g,"UK C30 TopBoost","Vox AC30 Top Boost channel: the iconic bright, jangly, compressed British chime (Queen, U2, Radiohead). Superb cleans and rich crunch when pushed.")
s(g,"US DLX 64 Vintage","Fender '64 Deluxe Reverb, vintage-spec: a 22W blackface combo that breaks up sweetly at moderate volume. Warm, sparkly cleans and bluesy grit; a studio staple.")
s(g,"US DLX 65 Reissue","Fender '65 Deluxe Reverb Reissue: classic blackface cleans with a slightly brighter, more modern feel. Touch-sensitive breakup, excellent pedal platform for country, blues and pop.")
tw="Fender high-power Tweed Twin (5F8-A), a big, loud late-'50s tweed with more headroom than a Bassman. "
s(g,"US HP Tweed TWN Bright",tw+"Bright channel: punchy, cutting tweed tone.")
s(g,"US HP Tweed TWN Bright Patch",tw+"Bright channel jumpered to Normal, blending both for fuller, gnarlier tweed grind.")
s(g,"US HP Tweed TWN Normal",tw+"Normal channel: warmer and rounder, with thicker lows.")
s(g,"US HP Tweed TWN Normal Patch",tw+"Normal channel jumpered to Bright: a fat, blended tweed tone that roars when pushed.")
s(g,"US Prince","Fender blackface Princeton Reverb: a small 12W, 10\" combo loved in studios. Sweet cleans that break up early with a warm, compressed grit; great for blues, country and indie.")
s(g,"US SPR Normal","Fender Super Reverb '65, normal channel: 4x10 blackface combo with bright, detailed cleans and a sparkly, blues-friendly breakup. No reverb/vibrato on this channel.")
s(g,"US SPR Vibrato","Fender Super Reverb '65, vibrato channel: the classic blackface Stevie Ray Vaughan-era clean-to-crunch tone, slightly more gain and sparkle than Normal.")
bm="Fender tweed Bassman (5F6-A), the late-'50s circuit that inspired the Marshall JTM45. Fat, raw, rich breakup for blues and roots rock. "
s(g,"US Tweed Basslad Bright",bm+"Bright channel: brighter and more cutting.")
s(g,"US Tweed Basslad Bright Patch",bm+"Bright channel jumpered with Normal: the classic full-bodied 'jumped' tweed Bassman sound.")
s(g,"US Tweed Basslad Normal",bm+"Normal channel: warmer and darker with thicker lows.")
s(g,"US Tweed Basslad Normal Patch",bm+"Normal channel jumpered with Bright: fat blended tweed grind, balance leaning warmer.")
s(g,"US TWN Normal","Fender Twin Reverb, normal channel: huge, pristine, high-headroom cleans. The go-to for loud, sparkling country, funk and jazz cleans and a clean pedal platform.")
s(g,"US TWN Vibrato","Fender Twin Reverb, vibrato channel: the classic sparkling blackface/silverface Twin clean with a touch more gain; stays clean until very loud.")
s(g,"Victor Squid Ch1","Victory Kraken (VX The Kraken), channel 1: the lower-gain, crunchier side of this compact British high-gain head, for rock rhythm and edgy crunch.")
s(g,"Victor Squid Ch2","Victory Kraken, channel 2: aggressive, tight, modern British high gain with a fierce midrange, ideal for modern metal and djent.")
s(g,"Watt D103 Bright","Hiwatt DR103, bright input: huge-headroom, loud and articulate British cleans with a bright edge (Pete Townshend, David Gilmour). A great pedal platform, especially for fuzz.")
s(g,"Watt D103 Normal","Hiwatt DR103, normal input: the same massive, clean, powerful Hiwatt voice, warmer and rounder. Thick clean rock and a superb platform for drive and fuzz pedals.")
# bass
ft="Ampeg Heritage B-15N Portaflex 'flip-top', the classic Motown/studio bass tone: warm, round and woody. "
for n,t in [("6464","This variant uses the '64 circuit on both channel and tone setting, for a warm, vintage round tone."),("6466","This variant mixes the '64 circuit with the '66 settings for a slightly brighter, more modern voice."),("6664","This variant uses the '66 circuit with '64 settings, blending the two eras' voices."),("6666","This variant uses the '66 circuit throughout, a bit brighter and punchier than the '64.")]:
    s(b,f"Amped Flip-Top {n}",ft+"The number denotes which of the amp's '64/'66 circuit and voicing options are selected; try each to taste.")
s(b,"Amped Super Valve","Ampeg SVT-CL, the classic all-tube rock bass head: big, warm, growling low end that grinds when pushed. The standard for rock, punk and metal bass.")
bb="Marshall Super Bass 50, a Plexi-era bass head that guitarists also love for its raw, aggressive breakup. "
s(b,"Brit Bass 50 Bright",bb+"Bright input: cutting top end for bass or guitar.")
s(b,"Brit Bass 50 Normal",bb+"Normal input: warmer and fuller, ideal for vintage rock bass.")
s(b,"Brit Bass 50 Patch",bb+"Inputs jumpered: full, gnarly blend for raw rock bass or plexi-style guitar crunch.")
s(b,"CA 400+ Ch1","Mesa/Boogie Bass 400+, channel 1: huge tube bass head with warm, punchy, clean-leaning tone; great for rock and fingerstyle.")
s(b,"CA 400+ Ch2","Mesa/Boogie Bass 400+, channel 2: brighter and more aggressive with extra drive, famous with Cliff Burton-era and heavy rock bass.")
s(b,"G800K","Gallien-Krueger 800RB, the solid-state bass workhorse: punchy, bright, articulate, with a signature midrange growl. A go-to for punk, pop-punk and slap.")
s(b,"Watt Bass Mod Bright","Hiwatt DR103 modified for bass, bright input: loud, clean, articulate bass with sparkle and plenty of headroom; also works for guitar.")
s(b,"Watt Bass Mod Normal","Hiwatt DR103 modified for bass, normal input: big, clean, warm bass tone with enormous headroom.")
json.dump(D,open('desc_amps.json','w'),ensure_ascii=False,indent=1)
d=json.load(open('next.json'))['props']['pageProps']
need={f"{gr['deviceType']}|{x['name']}" for gr in d['groups'] if gr['deviceType'] in(g,b) for x in gr['list']}
print(len(D),len(need),need-set(D),set(D)-need)
