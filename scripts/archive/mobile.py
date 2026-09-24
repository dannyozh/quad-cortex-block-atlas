t=open('template.html').read()
old=t[t.index('@media (max-width:760px){'):t.index('@media (prefers-reduced-motion')]
new='''/* Toggles row: group the checkboxes so they wrap as one unit */
.toggles{display:flex;flex-wrap:wrap;gap:6px 16px}
.chip{min-height:34px}

/* Tablet: name | modeled on | added, description full width underneath */
@media (max-width:1024px){
  .wrap{padding-inline:16px}
  .dev{grid-template-columns:minmax(0,1fr) minmax(0,1fr) 44px;gap:2px 14px;padding-block:8px}
  .dev .ds{grid-column:1 / -1}
  .head-row .ds{display:none}
}

/* Phone: stacked rows, slimmer sticky bar */
@media (max-width:640px){
  body{font-size:14.5px}
  header.top{padding-block:16px 8px;gap:8px}
  .lede{font-size:14px}
  .stats{gap:4px 14px;font-size:12px}
  .bar{padding-block:8px;gap:8px}
  #q{font-size:16px;padding:9px 11px;flex-basis:100%} /* 16px stops iOS zooming on focus */
  .toggles{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;gap:14px;width:100%}
  .toggles::-webkit-scrollbar{display:none}
  .toggle{flex:none;font-size:13px;min-height:28px}
  .toggle input{width:18px;height:18px}
  .chips{scrollbar-width:none;margin-inline:-16px;padding-inline:16px;scroll-padding-inline:16px}
  .chips::-webkit-scrollbar{display:none}
  .hint{display:none}
  .dev{grid-template-columns:minmax(0,1fr) auto;gap:3px 12px;padding-block:10px}
  .dev .nm{grid-column:1}
  .dev .v{grid-column:2;grid-row:1}
  .dev .bo,.dev .ds{grid-column:1 / -1}
  .dev .bo{font-size:13px}
  .dev .ds{font-size:13.5px}
  .head-row{display:none}
  .cat-head h2{font-size:26px}
  .cat-head p{font-size:13px}
  .guide summary{font-size:16px;padding-block:2px}
  .guide dl{font-size:13px}
  footer{margin-top:36px;font-size:12px}
}
'''
t=t.replace(old,new)
a='''      <label class="toggle"><input type="checkbox" id="onlyNew"> New in 4.1.0 only</label>
      <label class="toggle"><input type="checkbox" id="showPlug" checked> Plugin devices</label>
      <label class="toggle"><input type="checkbox" id="showCap" checked> Factory captures</label>'''
b='''      <div class="toggles">
        <label class="toggle"><input type="checkbox" id="onlyNew"> New in 4.1.0 only</label>
        <label class="toggle"><input type="checkbox" id="showPlug" checked> Plugin devices</label>
        <label class="toggle"><input type="checkbox" id="showCap" checked> Factory captures</label>
      </div>'''
assert a in t; t=t.replace(a,b)
t=t.replace('.head-row .v{text-align:right}','.head-row .v{text-align:right}\n.head-row .ds{color:inherit}')
# keep the active tab visible in the scrolling chip strip
a='''  $("#hint").textContent'''
b='''  const cur = document.querySelector('.chip[aria-selected="true"]');
  if (cur) { const s = $("#chips"); const l = cur.offsetLeft - s.offsetLeft; if (l < s.scrollLeft || l + cur.offsetWidth > s.scrollLeft + s.clientWidth) s.scrollLeft = l - 16; }
  $("#hint").textContent'''
assert a in t; t=t.replace(a,b)
open('template.html','w').write(t)
print('ok')
