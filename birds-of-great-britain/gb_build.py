import sys, base64, os, html
sys.path.insert(0, '.')
sys.path.insert(0, 'vol1')
sys.path.insert(0, 'vol2')
sys.path.insert(0, 'vol3')
sys.path.insert(0, 'vol4')
sys.path.insert(0, 'vol5')
from species_gb_vol1 import SPECIES_GB_V1
from species_gb_vol2 import SPECIES_GB_V2
from species_gb_vol3 import SPECIES_GB_V3
from species_gb_vol4 import SPECIES_GB_V4
from species_gb_vol5 import SPECIES_GB_V5

# --- self-contained (NOT shared with the Birds of Europe build) -------------
# This script deliberately duplicates rather than imports the Europe build's
# machinery, per the "no cross-project sharing" decision -- see gb_anatomy_diagram.html
# for the same rule applied to the anatomy diagram.

STATUS_LABELS = {
    'stable': ('Stable', 'Still recognised, essentially as Gould described it.'),
    'reclassified': ('Reclassified', 'Same bird, moved to a different genus or family as relationships were reassessed.'),
    'split': ('Split', 'What Gould treated as one kind is now understood to be two or more.'),
    'lumped': ('Lumped', "What Gould treated as its own kind is now folded into another species."),
    'contested': ('Contested', 'A live, still-debated question among ornithologists today.'),
    'unresolved': ('Unresolved', "Gould's identification has never been definitively pinned down."),
}

VOLUME_META = {
    'I':   dict(order='Raptores', ready=True),
    'II':  dict(order='Insessores', ready=True),
    'III': dict(order='Insessores', ready=True),
    'IV':  dict(order='Rasores &amp; Grallatores', ready=True),
    'V':   dict(order='Natatores', ready=True),
}

def img_data_uri(path):
    with open(path, 'rb') as f:
        b = base64.b64encode(f.read()).decode('ascii')
    return f'data:image/jpeg;base64,{b}'

# --- normalise each volume into one record shape ------------------------------
ALL = []
for s in SPECIES_GB_V1:
    r = dict(s)
    r['volume'] = 'I'
    page = s['plate_page']
    r['thumb_path'] = f"images_wip/vol1_plates/cropped/{page}-{page}_thumb.jpg"
    r['hires_path'] = f"britain_images/vol1/p{page}.jpg"
    ALL.append(r)

for s in SPECIES_GB_V2:
    r = dict(s)
    r['volume'] = 'II'
    page = r['plate_page']
    r['thumb_path'] = f"images_wip/vol2_plates/cropped/{page}-{page}_thumb.jpg"
    r['hires_path'] = f"britain_images/vol2/p{page}.jpg"
    ALL.append(r)

for s in SPECIES_GB_V3:
    r = dict(s)
    r['volume'] = 'III'
    page = r['plate_page']
    r['thumb_path'] = f"images_wip/vol3_plates/cropped/{page}-{page}_thumb.jpg"
    r['hires_path'] = f"britain_images/vol3/p{page}.jpg"
    ALL.append(r)

for s in SPECIES_GB_V4:
    r = dict(s)
    r['volume'] = 'IV'
    page = r['plate_page']
    r['thumb_path'] = f"images_wip/vol4_plates/cropped/{page}-{page}_thumb.jpg"
    r['hires_path'] = f"britain_images/vol4/p{page}.jpg"
    ALL.append(r)

for s in SPECIES_GB_V5:
    r = dict(s)
    r['volume'] = 'V'
    page = r['plate_page']
    r['thumb_path'] = f"images_wip/vol5_plates/cropped/{page}-{page}_thumb.jpg"
    r['hires_path'] = f"britain_images/vol5/p{page}.jpg"
    ALL.append(r)

VOLUME_ORDER = {'I': 0, 'II': 1, 'III': 2, 'IV': 3, 'V': 4}
ALL.sort(key=lambda r: (VOLUME_ORDER[r['volume']], r['plate_page']))
total = len(ALL)

cards_html = []
for i, s in enumerate(ALL):
    uri = img_data_uri(s['thumb_path'])
    gould_en = html.escape(s['english'])
    modern_en = html.escape(s['modern_en'])
    latin = html.escape(s['latin'])
    modern_latin = html.escape(s.get('modern_latin') or '')
    latin_differs = bool(s.get('modern_latin')) and s['latin'].strip().lower() != s['modern_latin'].strip().lower()
    latin_is_current = not latin_differs and s.get('status') != 'lumped'
    author = html.escape(s.get('author','') or '')
    same_name = gould_en.lower() == modern_en.lower()
    plate_note = html.escape(s.get('plate_note') or '')

    status_key = s.get('status')
    status_html = ''
    if status_key and status_key in STATUS_LABELS:
        label, blurb = STATUS_LABELS[status_key]
        note_text = s.get('resolved_by') or s.get('note') or ''
        note_html = f'<p class="resolved-by"><strong>How we know now:</strong> {html.escape(note_text)}</p>' if note_text else ''
        status_html = f'''
        <div class="status-box status-{status_key}">
          <div class="status-label">{label}</div>
          <p>{html.escape(blurb)}</p>
          {note_html}
        </div>'''

    share_note = ''
    if s.get('shares_with'):
        share_note = f'<div class="share-note">This plate&rsquo;s written account is combined with plate {s["shares_with"]:03d} &mdash; see that card for the full text reference.</div>'

    search_blob = " ".join([
        gould_en, modern_en, latin, modern_latin, author,
        f"plate {i+1}", f"plate {i+1:03d}", f"#{i+1}",
    ]).lower()

    card = f'''
    <div class="card" data-search="{html.escape(search_blob)}" data-status="{status_key or ''}" data-volume="{s['volume']}">
      <div class="plate-frame" data-hires="{html.escape(s['hires_path'])}" data-caption="{modern_en} &mdash; {latin}" title="Click to zoom in (loads a high-resolution image)"><img src="{uri}" alt="{modern_en}" loading="lazy"><div class="vol-tag">Vol. {s['volume']}</div><div class="zoom-hint">&#128269; Click to zoom</div></div>
      <div class="card-body">
        <div class="plate-no">Plate {i+1:03d}{f' &middot; {plate_note}' if plate_note else ''}</div>
        <h2 class="en-name">{modern_en}</h2>
        {'' if same_name else f'<div class="gould-name"><span class="gould-name-label">Gould&rsquo;s plate:</span> <span class="gould-name-old">&ldquo;{gould_en}&rdquo;</span></div>'}
        <div class="latin{' latin-current' if latin_is_current else ''}">{latin} <span class="author">{author}</span>{' <span class="latin-obsolete-tag">(obsolete)</span>' if latin_differs else ''}</div>
        {f'<div class="latin-modern"><span class="latin-modern-label">now:</span> {modern_latin}</div>' if latin_differs else ''}
        {status_html}
        {share_note}
      </div>
    </div>'''
    cards_html.append(card)

grid = "\n".join(cards_html)

vol_counts = {}
for r in ALL:
    vol_counts[r['volume']] = vol_counts.get(r['volume'], 0) + 1

vol_chips = []
for vnum in ['I','II','III','IV','V']:
    meta = VOLUME_META[vnum]
    cls = 'ready' if meta['ready'] else 'pending'
    label = f"Vol. {vnum}" + (f" ({vol_counts.get(vnum, 0)})" if meta['ready'] else " &mdash; soon")
    vol_chips.append(f'<button class="vol-chip {cls}" data-volume="{vnum}" data-ready="{"1" if meta["ready"] else "0"}">{label}</button>')
vol_chips_html = "\n".join(vol_chips)

html_doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Birds of Great Britain &mdash; John Gould, in Five Volumes (complete)</title>
<style>
  :root {{
    --paper: #faf5ea; --paper-dark: #f0e6d2; --ink: #2b241b; --ink-soft: #5a4f3f;
    --accent: #7a5230; --accent-2: #8a6d3b; --border: #d8c9a8; --card-bg: #fffdf8;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: #0a1b2d; color: #dfe4ec;
    font-family: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, "Times New Roman", serif;
  }}
  header {{
    position: relative; text-align: center; padding: 56px 20px 36px;
    border-bottom: 1px solid var(--border); background: var(--paper-dark);
  }}
  header .eyebrow {{
    letter-spacing: 0.25em; text-transform: uppercase; font-size: 12px; color: var(--accent); margin-bottom: 10px;
  }}
  header h1 {{
    font-size: clamp(26px, 4vw, 40px); margin: 0 0 8px; font-weight: 400; letter-spacing: 0.02em; color: var(--ink);
  }}
  header p.sub {{
    color: var(--ink-soft); font-size: 15px; margin: 0 auto; max-width: 640px; line-height: 1.5; font-style: italic;
  }}
  .preview-note {{
    max-width: 640px; margin: 16px auto 0; padding: 10px 16px; background: rgba(122,82,48,0.12);
    border: 1px solid var(--border); border-radius: 6px; font-size: 13px; color: var(--ink-soft); font-style: normal;
  }}
  .toolbar {{ max-width: 1200px; margin: 24px auto 0; padding: 0 24px; display: flex; justify-content: center; }}
  #search {{
    width: 100%; max-width: 460px; padding: 10px 16px; font-size: 15px; border: 1px solid var(--border);
    border-radius: 999px; background: var(--card-bg); color: var(--ink); font-family: inherit; outline: none;
  }}
  #search:focus {{ border-color: var(--accent-2); }}
  .vol-row {{ display: flex; justify-content: center; flex-wrap: wrap; gap: 8px; margin: 16px auto 0; max-width: 1000px; padding: 0 24px; }}
  .vol-chip {{
    font-family: inherit; font-size: 12.5px; letter-spacing: 0.03em; padding: 7px 14px; border-radius: 999px;
    border: 1px solid var(--border); background: var(--card-bg); color: var(--ink-soft); cursor: pointer;
  }}
  .vol-chip.ready {{ background: var(--accent); color: #fbf2e2; border-color: var(--accent); }}
  .vol-chip.pending {{ opacity: 0.55; font-style: italic; cursor: default; }}
  .vol-chip.ready.selected {{ background: #a6192e; border-color: #a6192e; box-shadow: 0 0 0 2px rgba(166,25,46,0.25); }}
  .vol-chip.ready:hover {{ filter: brightness(1.08); }}
  #count {{ text-align: center; color: var(--ink-soft); font-size: 13px; margin: 14px 0 0; }}
  .grid {{
    max-width: 1300px; margin: 30px auto 80px; padding: 0 24px; display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 26px;
  }}
  .card {{
    background: var(--card-bg); border: 1px solid var(--border); border-radius: 4px; overflow: hidden;
    box-shadow: 0 1px 3px rgba(43,36,27,0.08), 0 6px 18px rgba(43,36,27,0.05);
    display: flex; flex-direction: column; transition: transform 0.18s ease, box-shadow 0.18s ease;
  }}
  .card:hover {{ transform: translateY(-3px); box-shadow: 0 4px 10px rgba(43,36,27,0.12), 0 14px 30px rgba(43,36,27,0.10); }}
  .plate-frame {{ background: #dde3ec; border-bottom: 1px solid var(--border); padding: 10px; position: relative; cursor: zoom-in; }}
  .plate-frame img {{ width: 100%; display: block; aspect-ratio: 3/4; object-fit: contain; object-position: center center; border: 1px solid #c7d0e0; }}
  .zoom-hint {{
    position: absolute; left: 8px; bottom: 8px; background: rgba(43,36,27,0.72); color: #fbf2e2; font-size: 10px;
    letter-spacing: 0.03em; padding: 4px 8px; border-radius: 3px; opacity: 0; transition: opacity 0.15s ease; pointer-events: none;
  }}
  .plate-frame:hover .zoom-hint {{ opacity: 1; }}
  .vol-tag {{
    position: absolute; top: 8px; right: 8px; background: rgba(43,36,27,0.72); color: #fbf2e2; font-size: 10px;
    letter-spacing: 0.06em; text-transform: uppercase; padding: 4px 8px; border-radius: 3px;
  }}
  .card-body {{ padding: 14px 16px 18px; flex: 1; display: flex; flex-direction: column; }}
  .plate-no {{ font-size: 10.5px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--accent); margin-bottom: 4px; }}
  .en-name {{ font-size: 19px; font-weight: 600; margin: 0 0 4px; line-height: 1.25; color: var(--ink); }}
  .gould-name {{ font-size: 12px; color: var(--ink-soft); font-style: italic; margin-bottom: 6px; }}
  .gould-name-label {{ font-size: 12px; }}
  .gould-name-old {{ font-size: 16px; color: #a3a3a3; font-weight: 400; }}
  .latin {{ font-style: italic; color: var(--accent); font-size: 14px; margin-bottom: 4px; }}
  .latin.latin-current {{ color: #a6192e; }}
  .latin .author {{ font-style: normal; color: var(--ink-soft); font-size: 12px; }}
  .latin-obsolete-tag {{ font-style: normal; color: #a37a4a; font-size: 11px; }}
  .latin-modern {{ font-style: italic; color: #a6192e; font-size: 14px; font-weight: 600; margin-bottom: 10px; }}
  .latin-modern-label {{ font-style: normal; font-weight: 600; color: var(--ink-soft); font-size: 12px; }}
  .status-box {{ margin-top: 10px; padding: 8px 10px; border-radius: 6px; background: var(--paper); border: 1px solid var(--border); font-size: 12.5px; }}
  .status-label {{ font-weight: 700; color: var(--accent); font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 3px; }}
  .status-box p {{ margin: 0 0 4px; color: var(--ink-soft); line-height: 1.5; }}
  .resolved-by {{ margin-top: 4px !important; }}
  .share-note {{ margin-top: 10px; font-size: 11.5px; color: var(--ink-soft); font-style: italic; }}
  .no-results {{ text-align: center; color: #aeb8ca; margin: 40px 0; }}
  .lightbox-overlay {{
    display: none; position: fixed; inset: 0; background: rgba(10,8,4,0.92); z-index: 2000;
    align-items: center; justify-content: center; flex-direction: column; padding: 32px; cursor: zoom-out;
  }}
  .lightbox-overlay.open {{ display: flex; }}
  .lightbox-overlay img {{ max-width: 100%; max-height: calc(100vh - 120px); object-fit: contain; box-shadow: 0 10px 40px rgba(0,0,0,0.6); background: #efe6d6; cursor: default; }}
  .lightbox-caption {{ color: #fbf2e2; font-size: 15px; margin-top: 16px; text-align: center; font-style: italic; }}
  .lightbox-close {{ position: absolute; top: 20px; right: 28px; color: #fbf2e2; font-size: 34px; line-height: 1; cursor: pointer; background: none; border: none; padding: 6px 10px; }}
  footer {{ text-align: center; color: #aeb8ca; font-size: 12px; padding: 20px; }}
</style>
</head>
<body>
<header>
  <div class="header-inner">
    <div class="eyebrow">John Gould &middot; 1862&ndash;1873</div>
    <h1>The Birds of Great Britain</h1>
    <p class="sub">A student gallery of Gould&rsquo;s complete five-volume folio &mdash; the Raptores (birds of prey), the Insessores (perching birds), the Rasores &amp; Grallatores (game birds, waders, herons and their allies), and now the Natatores (ducks, geese and swans, divers, grebes, auks, gulls, terns and petrels), reproduced here in one online gallery, with each plate&rsquo;s name checked against current taxonomy so you always know what to call it today.</p>
    <div class="preview-note">All five volumes are now here ({total} plates) &mdash; every plate from Gould&rsquo;s 1862&ndash;1873 <em>Birds of Great Britain</em>, cropped, catalogued, and checked against modern taxonomy.</div>
  </div>
</header>
<div class="toolbar"><input id="search" type="search" placeholder="Search by name, Latin binomial, or plate number&hellip;"></div>
<div class="vol-row">{vol_chips_html}</div>
<div id="count"></div>
<div class="grid" id="grid">
{grid}
</div>
<div class="no-results" id="noResults" style="display:none;">No plates match your search.</div>
<div class="lightbox-overlay" id="lightbox">
  <button class="lightbox-close" id="lightboxClose">&times;</button>
  <img id="lightboxImg" src="" alt="">
  <div class="lightbox-caption" id="lightboxCaption"></div>
</div>
<footer>The Birds of Great Britain &middot; student gallery &middot; complete, Volumes I&ndash;V &middot; sourced from Gould&rsquo;s original 1862&ndash;1873 plates and text</footer>
<script>
(function() {{
  var cards = Array.prototype.slice.call(document.querySelectorAll('.card'));
  var search = document.getElementById('search');
  var count = document.getElementById('count');
  var noResults = document.getElementById('noResults');
  var volChips = Array.prototype.slice.call(document.querySelectorAll('.vol-chip.ready'));
  var activeVolume = null;
  function applyFilter() {{
    var q = search.value.trim().toLowerCase();
    var shown = 0;
    cards.forEach(function(c) {{
      var matchesSearch = !q || c.getAttribute('data-search').indexOf(q) !== -1;
      var matchesVolume = !activeVolume || c.getAttribute('data-volume') === activeVolume;
      var match = matchesSearch && matchesVolume;
      c.style.display = match ? '' : 'none';
      if (match) shown++;
    }});
    count.textContent = shown + ' of ' + cards.length + ' plates shown';
    noResults.style.display = shown === 0 ? 'block' : 'none';
  }}
  search.addEventListener('input', applyFilter);
  volChips.forEach(function(chip) {{
    chip.addEventListener('click', function() {{
      var vol = chip.getAttribute('data-volume');
      if (activeVolume === vol) {{
        activeVolume = null;
      }} else {{
        activeVolume = vol;
      }}
      volChips.forEach(function(c) {{ c.classList.toggle('selected', c.getAttribute('data-volume') === activeVolume); }});
      applyFilter();
    }});
  }});
  applyFilter();

  var lightbox = document.getElementById('lightbox');
  var lightboxImg = document.getElementById('lightboxImg');
  var lightboxCaption = document.getElementById('lightboxCaption');
  document.querySelectorAll('.plate-frame').forEach(function(frame) {{
    frame.addEventListener('click', function() {{
      lightboxImg.src = frame.getAttribute('data-hires');
      lightboxCaption.textContent = frame.getAttribute('data-caption').replace(/&mdash;/g, '\\u2014');
      lightbox.classList.add('open');
    }});
  }});
  function closeLightbox() {{ lightbox.classList.remove('open'); lightboxImg.src=''; }}
  document.getElementById('lightboxClose').addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', function(e) {{ if (e.target === lightbox) closeLightbox(); }});
  document.addEventListener('keydown', function(e) {{ if (e.key === 'Escape') closeLightbox(); }});
}})();
</script>
</body>
</html>'''

with open('britannia.html', 'w', encoding='utf-8') as f:
    f.write(html_doc)

print(f"Wrote britannia.html — {total} species, Volumes I-V (complete)")
