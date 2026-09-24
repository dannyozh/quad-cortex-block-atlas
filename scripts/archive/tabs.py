t=open('template.html').read()
R=[
(".dev{display:grid;grid-template-columns:minmax(170px,1.1fr) minmax(160px,1fr) 2.3fr 70px;gap:4px 18px;padding-block:11px;",
 ".dev{display:grid;grid-template-columns:minmax(160px,1fr) minmax(150px,1fr) 2.6fr 52px;gap:2px 16px;padding-block:6px;"),
(".dev .bo{font-size:14px}", ".dev .bo{font-size:13.5px;line-height:1.4}"),
(".dev .ds{font-size:14px;color:var(--muted)}", ".dev .ds{font-size:13.5px;line-height:1.45;color:var(--muted)}"),
(".dev .nm{font-weight:600;", ".dev .nm{font-weight:600;font-size:14.5px;line-height:1.35;"),
("header.top{padding-block:40px 20px;display:grid;gap:14px}", "header.top{padding-block:24px 12px;display:grid;gap:10px}"),
("h1{font:700 clamp(40px,7vw,72px)/.92", "h1{font:700 clamp(34px,5vw,52px)/.95"),
("<h1>Quad Cortex<br><span", "<h1>Quad Cortex <span"),
(".guide{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:16px;margin-block:24px 8px}",
 ".guide{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:10px;margin-block:12px 0}"),
(".guide details{background:var(--surface);border:1px solid var(--rule);border-radius:8px;padding:12px 16px}",
 ".guide details{background:var(--surface);border:1px solid var(--rule);border-radius:8px;padding:8px 14px}"),
("section.cat{margin-top:40px;", "section.cat{margin-top:20px;"),
("h3.sub{font:600 16px var(--display);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:22px 0 4px}",
 "h3.sub{font:600 15px var(--display);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:14px 0 2px}"),
(".chip[aria-pressed=\"true\"]", ".chip[aria-selected=\"true\"]"),
(".empty{", ".hint{font-size:12.5px;color:var(--muted);min-height:1em}\n.empty{"),
('<div class="chips" id="chips" role="toolbar" aria-label="Jump to category"></div>',
 '<div class="chips" id="chips" role="tablist" aria-label="Category"></div>\n    <div class="hint" id="hint"></div>'),
]
for a,b in R:
    assert a in t, a
    t=t.replace(a,b,1)
old_js=t[t.index('// Chips'):t.index('function row(d)')]
new_js='''// Tabs
let active = "amps";
try { active = localStorage.getItem("qc-tab") || active; } catch (e) {}
if (!DATA.sections.some(s => s.id === active)) active = "amps";
$("#chips").innerHTML = DATA.sections.map(s =>
  `<button class="chip" type="button" role="tab" id="tab-${s.id}" data-target="${s.id}" style="--c:var(${s.color})"><span class="dot"></span>${esc(s.title)} <small id="cc-${s.id}"></small></button>`
).join("");
$("#chips").addEventListener("click", e => {
  const b = e.target.closest(".chip"); if (!b) return;
  active = b.dataset.target;
  try { localStorage.setItem("qc-tab", active); } catch (e) {}
  $("#q").value = ""; $("#onlyNew").checked = false;
  render();
  window.scrollTo({top: Math.min(window.scrollY, $(".bar").offsetTop)});
});

'''
t=t.replace(old_js,new_js)
old_r=t[t.index('function render(){'):t.index('for (const d of all)')]
new_r='''function render(){
  const q = $("#q").value.trim().toLowerCase();
  const terms = q.split(/\\s+/).filter(Boolean);
  const onlyNew = $("#onlyNew").checked, showPlug = $("#showPlug").checked, showCap = $("#showCap").checked;
  const searching = terms.length > 0 || onlyNew;
  if ((active === "plugins" && !showPlug) || (active === "caps" && !showCap)) active = "amps";
  let html = "", total = 0;
  for (const s of DATA.sections){
    const hiddenKind = (s.kind === "plug" && !showPlug) || (s.kind === "cap" && !showCap);
    let body = "", n = 0;
    for (const g of s.groups){
      const items = hiddenKind ? [] : g.items.filter(d => (!onlyNew || d.isNew) && terms.every(t => d.hay.includes(t)));
      if (!items.length) continue;
      n += items.length;
      body += (g.title ? `<h3 class="sub">${esc(g.title)}</h3>` : "") + (g.meta ? `<p class="plugmeta">${g.meta}</p>` : "") + `<div class="list">${HEAD}${items.map(row).join("")}</div>`;
    }
    const tab = document.getElementById("tab-" + s.id);
    document.getElementById("cc-" + s.id).textContent = n;
    tab.hidden = n === 0;
    tab.setAttribute("aria-selected", String(!searching && s.id === active));
    if (!n || (!searching && s.id !== active)) continue;
    total += n;
    html += `<section class="cat" id="${s.id}" style="--c:var(${s.color})"><div class="cat-head"><h2>${esc(s.title)}</h2><span class="n">${n} device${n>1?"s":""}</span><p>${esc(s.blurb)}</p></div>${body}</section>`;
  }
  $("#hint").textContent = searching ? `Showing ${total} match${total===1?"":"es"} across all categories. Pick a tab to clear the search.` : "Showing one category at a time. Search to look across all of them.";
  $("#out").innerHTML = html || `<div class="empty">No devices match “${esc(q)}”. Try a brand (Marshall), a pedal (Tube Screamer) or a use (ambient).</div>`;
}
'''
t=t.replace(old_r,new_r)
open('template.html','w').write(t)
print('patched')
