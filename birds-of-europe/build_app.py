import sys, base64, os, html, json, re
sys.path.insert(0, '.')
sys.path.insert(0, 'vol3')
sys.path.insert(0, 'vol1')
sys.path.insert(0, 'vol4')
sys.path.insert(0, 'vol5')
from species import SPECIES
from species_vol3 import SPECIES_V3
from species_vol1 import SPECIES_V1
from species_vol4 import SPECIES_V4
from species_vol5 import SPECIES_V5
from glossary import GLOSSARY
from genus_family import FAMILY_MAP
from artist_credits import get_credit as get_artist_credit
from genus_char import CHAR as GEN_CHAR_ALL
from authorities import AUTHORITIES
from etymology import ETYMOLOGY
from artist_bios import ARTIST_BIOS

def etymology_tip_html(word_key):
    e = ETYMOLOGY[word_key]
    parts = [
        f'<span class="auth-name">{html.escape(word_key)}</span>',
        f'<span class="auth-meta">{html.escape(e["origin"])}</span>',
        html.escape(e["explanation"]),
    ]
    conf = e.get('confidence', '')
    if conf and conf != 'high':
        parts.append(f'<span class="auth-notable">Etymology confidence: {html.escape(conf)} &mdash; some details here are disputed or reconstructed rather than certain.</span>')
    return ''.join(parts)

def etymology_wrap(name_raw):
    """Wrap the LAST word of a common English bird name (e.g. 'Goose' in
    'Snow Goose') in a hoverable etymology-term span, if that word's origin
    has been researched. Everything else in the name is left as plain
    (html-escaped) text. Operates on the raw, unescaped name."""
    words = name_raw.split(' ')
    last = words[-1]
    last_clean = last.strip('.,;:')
    entry_key = None
    for k in ETYMOLOGY:
        if k.lower() == last_clean.lower():
            entry_key = k
            break
    if not entry_key:
        return html.escape(name_raw)
    prefix = html.escape(' '.join(words[:-1]) + (' ' if len(words) > 1 else ''))
    suffix = html.escape(last[len(last_clean):])  # trailing punctuation, if any
    b64 = base64.b64encode(etymology_tip_html(entry_key).encode('utf-8')).decode('ascii')
    return f'{prefix}<span class="authority-term etymology-term" tabindex="0" data-bio-b64="{b64}">{html.escape(last_clean)}</span>{suffix}'

# --- Taxonomic-authority normalization --------------------------------------
# The 'author' field stores whatever abbreviation/format happened to survive
# transcription for that species ("Linn.", "(Linnaeus)", "Linnaeus", "Pall.",
# ...) -- AUTHOR_NORMALIZE maps every observed raw variant (lowercased) down
# to the canonical key used in authorities.py, so all of them share one bio.
AUTHOR_NORMALIZE = {
    'linn.': 'Linnaeus', '(linnaeus)': 'Linnaeus', 'linnaeus': 'Linnaeus', '(linnaeus) subsp.': 'Linnaeus',
    'temm.': 'Temminck', '(temminck)': 'Temminck', 'temminck': 'Temminck', 'tem.': 'Temminck',
    'temminck, 1820 (specimen: natterer)': 'Temminck', 'temminck, c. 1820': 'Temminck',
    'steph.': 'Stephens',
    'lath.': 'Latham', 'latham': 'Latham', '(latham)': 'Latham',
    'meyer.': 'Meyer',
    'leach.': 'Leach',
    'bechst.': 'Bechstein', '(bechstein)': 'Bechstein',
    'flem.': 'Fleming',
    '(pallas)': 'Pallas', 'pall.': 'Pallas', 'pallas': 'Pallas',
    'briss.': 'Brisson',
    'selby.': 'Selby',
    'cuv.': 'Cuvier',
    'ray.': 'Ray', 'will. & ray.': 'Willughby & Ray',
    '(gmelin)': 'Gmelin', 'gmel.': 'Gmelin', 'gimel.': 'Gmelin',
    '(vieillot)': 'Vieillot', 'vieill.': 'Vieillot', 'vieillot': 'Vieillot',
    'leisl.': 'Leisler',
    'dum.': 'Dumont',
    '(boddaert)': 'Boddaert',
    'swains.': 'Swainson',
    'bonap.': 'Bonaparte',
    'brunn.': 'Brünnich',
    'savigny.': 'Savigny', 'sav.': 'Savigny', 'savig.': 'Savigny',
    'natt.': 'Natterer',
    'vig.': 'Vigors',
    '(scopoli)': 'Scopoli',
    'c. l. brehm': 'C. L. Brehm',
    'sparrm.': 'Sparrman',
    'bellon.': 'Bellon',
    'payr.': 'Payraudeau',
    'montag.': 'Montagu',
    'storr.': 'Storr',
    'sykes.': 'Sykes',
    'sibb.': 'Sibbald',
    'nils.': 'Nilsson',
    '(laxmann)': 'Laxmann',
    '(lepechin)': 'Lepechin',
    '(güldenstädt)': 'Güldenstädt',
    '(wolf)': 'Wolf',
    '(savi)': 'Savi', 'savi.': 'Savi',
    '(strickland)': 'Strickland',
    '(hermann)': 'Hermann',
    '(rafinesque)': 'Rafinesque',
    'gould': 'Gould',
    'billberg': 'Billberg',
    'tunstall': 'Tunstall',
    'wagl.': 'Wagler',
    'briss. & cuv.': 'Brisson',
    'yarr.': 'Yarrell',
    'eyton.': 'Eyton',
    'lafr.': 'Lafresnaye',
    'sab.': 'Sabine',
    'linn. / ray.': 'Linnaeus',
    'bruch.': 'Bruch',
    'meissn. et schinz.': 'Meissner',
    'faber.': 'Faber',
}

def author_key(raw):
    """Normalize a raw author-citation string to the canonical key used in
    AUTHORITIES, or None if unrecognized (a handful of one-off/unclear
    citations have no matching bio and are left as plain text)."""
    if not raw:
        return None
    return AUTHOR_NORMALIZE.get(raw.strip().lower())

def author_tip_html(canon):
    """Build the tooltip's inner HTML for a given canonical authority key."""
    a = AUTHORITIES[canon]
    parts = [
        f'<span class="auth-name">{html.escape(a["full_name"])}</span>',
        f'<span class="auth-meta">{html.escape(a["dates"])} · {html.escape(a["nationality"])}</span>',
        html.escape(a["bio"]),
    ]
    notable = a.get('notable', '')
    if notable and notable.lower() != 'none found':
        parts.append(f'<span class="auth-notable">{html.escape(notable)}</span>')
    wiki = a.get('wikipedia', '')
    if wiki.startswith('http'):
        parts.append(f'<a href="{html.escape(wiki)}" target="_blank" rel="noopener">Wikipedia &rarr;</a>')
    return ''.join(parts)

# --- Gen. Char. genus-name mapping -----------------------------------------
# genus_char.py is keyed by GOULD'S OWN 1832-1837 printed genus name for each
# volume. For Volumes I, III and IV the stored 'latin' field's genus already
# matches Gould's printed genus directly. Volumes II and V need a bit more
# help:
#
#  - Volume II (species.py): most 'latin' genus names already match Gould's
#    printed genus (species he never had reclassified), but every species
#    flagged status='reclassified' or 'split' stores the MODERN genus in
#    'latin' instead -- these need mapping back to whichever of Gould's 26
#    printed genera they were originally grouped under. Some modern genera
#    (Muscicapa/Ficedula flycatchers, Saxicola/Oenanthe chats & wheatears,
#    among a few others) could not be confidently matched to one of the 26
#    printed genera actually verified in genus_char.py's VOL2 -- those are
#    left unmapped, so those species simply show no Gen. Char. box rather
#    than a guessed/possibly-wrong one.
#  - Volume V (species_vol5.py): a handful of species sit under one of
#    Gould's finer printed genus splits (Chauliodes, Harelda, Mergulus,
#    Viralva) that aren't reflected in the stored 'latin' field's broader
#    genus. Mapped here by page number, the only reliable key.
MODERN_TO_GOULD_V2 = {
    'Apus': 'Cypselus',
    'Tachymarptis': 'Cypselus',
    'Cecropis': 'Hirundo',
    'Ptyonoprogne': 'Hirundo',
    'Delichon': 'Hirundo',
    'Riparia': 'Hirundo',
    'Ceryle': 'Alcedo',
    'Erithacus': 'Erythaca',
    'Phoenicurus': 'Phoenicura',
    'Prunella': 'Accentor',
    'Monticola': 'Petrocincla',
    'Luscinia': 'Philomela',
    'Curruca': 'Sylvia',
    'Zoothera': 'Turdus',
    'Geokichla': 'Turdus',
}

VOL5_GENUS_BY_PAGE = {
    94: 'Chauliodes',    # Gadwall -- Anas strepera in species_vol5.py
    158: 'Harelda',      # Long-tailed Duck -- Anas glacialis in species_vol5.py
    238: 'Mergulus',     # Little Auk -- Alca alle / Mergulus alle
    318: 'Viralva',      # Black Tern -- Sterna nigra in species_vol5.py
}

def lookup_gen_char(volume_num, latin, page):
    """Look up the real Gen. Char. paragraph for a species, returning
    (genus_name_to_display, text_or_None). Returns (None, None) if we can't
    confidently place this species under one of the volume's checked genera."""
    vol_char = GEN_CHAR_ALL.get(volume_num, {})
    g = genus_of(latin)
    if not g:
        return None, None
    if volume_num == 5 and page in VOL5_GENUS_BY_PAGE:
        g = VOL5_GENUS_BY_PAGE[page]
    elif volume_num == 2 and g not in vol_char:
        g = MODERN_TO_GOULD_V2.get(g, g)
    if g in vol_char:
        return g, vol_char[g]
    return None, None

# --- genus / family helpers --------------------------------------------
def genus_of(latin):
    """Pull a genus name out of a (possibly messy) Latin binomial string.
    Handles Gould's plain 'Genus species' as well as the handful of
    uncertain modern identifications recorded as 'cf. Genus species' or
    'cf. Genus (Alt1/Alt2)'."""
    if not latin:
        return None
    s = latin.strip()
    s = re.sub(r'^cf\.\s*', '', s, flags=re.I)
    s = re.split(r'[\/(]', s)[0].strip()
    m = re.match(r'[A-Za-zÆæŒœ]+', s)
    return m.group(0).title() if m else None

def family_of(modern_latin):
    """Look up the modern Family for a species, keyed first by the exact
    (possibly 'cf. ...') modern_latin string, then by its extracted genus."""
    if not modern_latin:
        return None
    if modern_latin in FAMILY_MAP:
        return FAMILY_MAP[modern_latin]
    return FAMILY_MAP.get(genus_of(modern_latin))

# --- glossary hover-term linking ----------------------------------------
# Sort longest-first so multi-word phrases (e.g. "binomial nomenclature")
# match before their component words ("nomenclature") would otherwise grab
# a shorter, less precise slice of the text.
_GLOSSARY_TERMS = sorted(GLOSSARY.keys(), key=len, reverse=True)
_GLOSSARY_PATTERN = re.compile(
    r'\b(' + '|'.join(re.escape(t) for t in _GLOSSARY_TERMS) + r')\b',
    re.IGNORECASE
)

def linkify_glossary(escaped_text):
    """Wrap glossary terms found in already-HTML-escaped text with a
    hoverable span carrying its definition. Safe to run on text that
    already contains simple tags like <br> (no term can span a tag)."""
    if not escaped_text:
        return escaped_text
    def _repl(m):
        term = m.group(0)
        defn = GLOSSARY.get(term.lower())
        if not defn:
            return term
        return f'<span class="gloss-term" tabindex="0" data-def="{html.escape(defn)}">{term}</span>'
    return _GLOSSARY_PATTERN.sub(_repl, escaped_text)

# Gould's own account text, transcribed from the user's fresh full-text OCR of
# each volume (much cleaner than the page-image OCR used elsewhere in this
# build). Matched to species by anchoring on a distinctive word from the
# heading, positionally bounded, then a fuzzy sanity check before being kept
# -- so coverage is partial (a species with a fragile OCR heading is left
# without a "read the original" section rather than risk showing the wrong
# bird's account). Keyed by each species' index in its original list.
def load_gould_text(path, species_list):
    if not os.path.exists(path):
        return
    with open(path, encoding='utf-8') as f:
        mapping = json.load(f)
    for k, txt in mapping.items():
        species_list[int(k)]['gould_text'] = txt

load_gould_text('vol1/gould_text.json', SPECIES_V1)
load_gould_text('gould_text_v2.json', SPECIES)
load_gould_text('vol3/gould_text.json', SPECIES_V3)
load_gould_text('vol4/gould_text.json', SPECIES_V4)
load_gould_text('vol5/gould_text.json', SPECIES_V5)

def img_data_uri(path):
    with open(path, 'rb') as f:
        b = base64.b64encode(f.read()).decode('ascii')
    return f'data:image/jpeg;base64,{b}'

def uri_for(path):
    return img_data_uri(path)

V2_TITLE_URI = uri_for('assets/v2_title.jpg')
V3_TITLE_URI = uri_for('assets/v3_title.jpg')
V4_TITLE_URI = uri_for('assets/v4_title.jpg')
V5_TITLE_URI = uri_for('assets/v5_title.jpg')
V1_TITLE_URI = uri_for('assets/v1_title.jpg')

# --- normalise both volumes into one shared record shape --------------------
ALL = []
for s in SPECIES_V1:
    r = dict(s)
    r['volume'] = 'I'
    r['card_path'] = f"vol1/cards/p{s['page']}.jpg"
    _artist, _printer = get_artist_credit(1, s['page'])
    r.setdefault('artist', _artist)
    r['printer'] = _printer
    r.setdefault('resolved_by', None)
    r['gen_char_genus'], r['gen_char'] = lookup_gen_char(1, s.get('latin'), s['page'])
    ALL.append(r)
for s in SPECIES:
    r = dict(s)
    r['volume'] = 'II'
    r['card_path'] = f"cards/p{s['page']}.jpg"
    _artist, _printer = get_artist_credit(2, s['page'])
    r.setdefault('artist', _artist)
    r['printer'] = _printer
    r.setdefault('modern_latin', None)
    r.setdefault('resolved_by', None)
    # Override whatever species.py's old embedded (garbled-OCR) GEN_CHAR
    # lookup set -- genus_char.py's vision-transcribed text replaces it.
    r['gen_char_genus'], r['gen_char'] = lookup_gen_char(2, s.get('latin'), s['page'])
    ALL.append(r)
for s in SPECIES_V3:
    r = dict(s)
    r['volume'] = 'III'
    r['card_path'] = f"vol3/cards/p{s['page']}.jpg"
    _artist, _printer = get_artist_credit(3, s['page'])
    r['artist'] = _artist
    r['printer'] = _printer
    r['gen_char_genus'], r['gen_char'] = lookup_gen_char(3, s.get('latin'), s['page'])
    ALL.append(r)
for s in SPECIES_V4:
    r = dict(s)
    r['volume'] = 'IV'
    r['card_path'] = f"vol4/cards/p{s['page']}.jpg"
    _artist, _printer = get_artist_credit(4, s['page'])
    r.setdefault('artist', _artist)
    r['printer'] = _printer
    r.setdefault('resolved_by', None)
    r['gen_char_genus'], r['gen_char'] = lookup_gen_char(4, s.get('latin'), s['page'])
    ALL.append(r)
for s in SPECIES_V5:
    r = dict(s)
    r['volume'] = 'V'
    r['card_path'] = f"vol5/cards/p{s['page']}.jpg"
    _artist, _printer = get_artist_credit(5, s['page'])
    r.setdefault('artist', _artist)
    r['printer'] = _printer
    r.setdefault('resolved_by', None)
    r['gen_char_genus'], r['gen_char'] = lookup_gen_char(5, s.get('latin'), s['page'])
    ALL.append(r)

ALL.sort(key=lambda r: (r['volume'], r['page']))

VOLUME_META = {
    'I':   dict(order='Raptores', ready=True,  count=sum(1 for r in ALL if r['volume']=='I')),
    'II':  dict(order='Insessores', ready=True,  count=sum(1 for r in ALL if r['volume']=='II')),
    'III': dict(order='Insessores', ready=True,  count=sum(1 for r in ALL if r['volume']=='III')),
    'IV':  dict(order='Rasores &amp; Grallatores', ready=True,  count=sum(1 for r in ALL if r['volume']=='IV')),
    'V':   dict(order='Natatores', ready=True,  count=sum(1 for r in ALL if r['volume']=='V')),
}

STATUS_LABELS = {
    'stable': ('Stable', 'Still recognised, essentially as Gould described it.'),
    'reclassified': ('Reclassified', 'Same bird, moved to a different genus or family as relationships were reassessed.'),
    'split': ('Split', 'What Gould treated as one kind is now understood to be two or more.'),
    'lumped': ('Lumped', "What Gould treated as its own kind is now folded into another species."),
    'contested': ('Contested', 'A live, still-debated question among ornithologists today.'),
    'unresolved': ('Unresolved', "Gould's identification has never been definitively pinned down."),
}

cards_html = []
obsolete_count = 0
for i, s in enumerate(ALL):
    uri = img_data_uri(s['card_path'])
    gould_en = html.escape(s['english'])
    modern_en = html.escape(s['modern_en'])
    modern_en_html = etymology_wrap(s['modern_en'])
    latin = html.escape(s['latin'])
    modern_latin = html.escape(s.get('modern_latin') or '')
    author_raw = s.get('author','') or ''
    author = html.escape(author_raw)
    _auth_canon = author_key(author_raw)
    if _auth_canon:
        _bio_b64 = base64.b64encode(author_tip_html(_auth_canon).encode('utf-8')).decode('ascii')
        author_html = f'<span class="authority-term" tabindex="0" data-bio-b64="{_bio_b64}">{author}</span>'
    else:
        author_html = author
    de = html.escape(s['de'])
    fr = html.escape(s['fr'])
    same_name = gould_en.lower() == modern_en.lower()
    is_obsolete = s.get('obsolete', False)
    if is_obsolete:
        obsolete_count += 1

    history_box = ''
    if is_obsolete:
        gould_account = linkify_glossary(html.escape(s.get('gould_account', '')))
        modern_verdict = linkify_glossary(html.escape(s.get('modern_verdict', '')))
        history_box = f'''
        <div class="history-box">
          <div class="history-label">A note on the history of science</div>
          <p><strong>What Gould believed:</strong> {gould_account}</p>
          <p><strong>What we now think it was:</strong> {modern_verdict}</p>
        </div>'''

    status_key = s.get('status')
    status_html = ''
    if status_key and status_key in STATUS_LABELS:
        label, blurb = STATUS_LABELS[status_key]
        resolved_by = s.get('resolved_by')
        resolved_html = f'<p class="resolved-by"><strong>How we know now:</strong> {linkify_glossary(html.escape(resolved_by))}</p>' if resolved_by else ''
        status_html = f'''
        <div class="status-box status-{status_key}">
          <div class="status-label">{label}</div>
          <p>{linkify_glossary(html.escape(blurb))}</p>
          {resolved_html}
        </div>'''

    gen_char_html = ''
    if s.get('gen_char'):
        genus = html.escape(s.get('gen_char_genus',''))
        full_char_text = linkify_glossary(html.escape(s['gen_char']))
        gen_char_html = f'''
        <details class="gen-char">
          <summary>Gould&rsquo;s own genus description ({genus})</summary>
          <p class="gen-char-text">&ldquo;{full_char_text}&rdquo;</p>
        </details>'''

    gould_text_html = ''
    if s.get('gould_text'):
        full_text = linkify_glossary(html.escape(s['gould_text'])).replace('\n', '<br>')
        gould_text_html = f'''
        <details class="gould-text">
          <summary>Read Gould&rsquo;s original 1832&ndash;1837 account</summary>
          <p class="gould-text-body">{full_text}</p>
        </details>'''

    badge = '<div class="badge">Not a valid species today</div>' if is_obsolete else ''
    artist_raw = s.get('artist', 'J. & E. Gould')
    artist = html.escape(artist_raw)
    _artist_bio = ARTIST_BIOS.get(artist_raw)
    if _artist_bio:
        _abio_html = ''.join([
            f'<span class="auth-name">{_artist_bio["heading"]}</span>',
            _artist_bio["bio"],
            f'<span class="auth-notable">{_artist_bio["notable"]}</span>',
            f'<a href="{html.escape(_artist_bio["wikipedia"])}" target="_blank" rel="noopener">Wikipedia &rarr;</a>',
        ])
        _abio_b64 = base64.b64encode(_abio_html.encode('utf-8')).decode('ascii')
        artist_credit_html = f'<span class="authority-term artist-term" tabindex="0" data-bio-b64="{_abio_b64}">{artist}</span>'
    else:
        artist_credit_html = artist
    printer = html.escape(s.get('printer', '')) if s.get('printer') else ''
    vol = s['volume']

    # --- Family / Genus (1837 vs today) / Artist chips ------------------
    genus_1837 = genus_of(s.get('latin'))
    genus_modern = genus_of(s.get('modern_latin'))
    family_modern = family_of(s.get('modern_latin'))

    chips = []
    if family_modern:
        chips.append(f'<button class="tag-chip family-chip" data-type="family" data-value="{html.escape(family_modern)}">{html.escape(family_modern)}</button>')
    if genus_1837 and genus_modern and genus_1837.lower() == genus_modern.lower():
        chips.append(f'<button class="tag-chip genus-chip genus-same" data-type="genusModern" data-value="{html.escape(genus_modern)}">Genus: {html.escape(genus_modern)}</button>')
    else:
        if genus_1837:
            chips.append(f'<button class="tag-chip genus-chip genus-1837" data-type="genus1837" data-value="{html.escape(genus_1837)}">1837: {html.escape(genus_1837)}</button>')
        if genus_modern:
            chips.append(f'<button class="tag-chip genus-chip genus-today" data-type="genusModern" data-value="{html.escape(genus_modern)}">Today: {html.escape(genus_modern)}</button>')
    if artist:
        chips.append(f'<button class="tag-chip artist-chip" data-type="artist" data-value="{artist}">{artist}</button>')
    chips_html = f'<div class="tag-chips">{"".join(chips)}</div>' if chips else ''

    # Full-text search: everything actually printed on the card, not just the
    # name fields — status blurbs, the "how we know now" note, Gould's own
    # genus excerpt, the history-of-science account, the artist credit, and
    # (where we have it) Gould's own full account text.
    status_label_text = STATUS_LABELS.get(status_key, ('',''))[0] if status_key else ''
    status_blurb_text = STATUS_LABELS.get(status_key, ('',''))[1] if status_key else ''
    plate_no = i + 1
    search_parts = [
        gould_en, modern_en, latin, modern_latin, de, fr,
        f"vol {vol.lower()}", f"volume {vol.lower()}",
        artist, family_modern or '', genus_1837 or '', genus_modern or '',
        status_label_text, status_blurb_text, s.get('resolved_by') or '',
        s.get('gen_char') or '', s.get('gen_char_genus') or '',
        s.get('gould_account') or '', s.get('modern_verdict') or '',
        s.get('gould_text') or '',
        author,
        f"plate {plate_no}", f"plate {plate_no:03d}", f"plate no {plate_no}",
        f"plate no. {plate_no}", f"#{plate_no}", f"{plate_no:03d}",
    ]
    search_blob = " ".join(search_parts).lower()

    card = f'''
    <div class="card{' card-obsolete' if is_obsolete else ''}" data-search="{html.escape(search_blob)}" data-obsolete="{'1' if is_obsolete else '0'}" data-status="{status_key or ''}" data-volume="{vol}" data-family="{html.escape(family_modern or '')}" data-genus1837="{html.escape(genus_1837 or '')}" data-genusmodern="{html.escape(genus_modern or '')}" data-artist="{artist}">
      <div class="plate-frame"><img src="{uri}" alt="{modern_en}" loading="lazy">{badge}<div class="vol-tag">Vol. {vol}</div></div>
      <div class="card-body">
        <div class="plate-no">Plate {i+1:03d}</div>
        <h2 class="en-name">{modern_en_html}</h2>
        {'' if same_name else f'<div class="gould-name">Gould&rsquo;s plate: &ldquo;{gould_en}&rdquo;</div>'}
        <div class="latin">{latin} <span class="author">{author_html}</span></div>
        <table class="names">
          <tr><th>DE</th><td>{de}</td></tr>
          <tr><th>FR</th><td>{fr}</td></tr>
        </table>
        {chips_html}
        <div class="artist-credit">Plate drawn &amp; lithographed by {artist_credit_html}{f' &middot; printed by {printer}' if printer and printer != 'C. Hullmandel' else ''}</div>
        {status_html}
        {gen_char_html}
        {gould_text_html}
        {history_box}
      </div>
    </div>'''
    cards_html.append(card)

grid = "\n".join(cards_html)

vol_chips = []
for vnum in ['I','II','III','IV','V']:
    meta = VOLUME_META[vnum]
    cls = 'ready' if meta['ready'] else 'pending'
    label = f"Vol. {vnum}" + (f" ({meta['count']})" if meta['ready'] else " &mdash; soon")
    # Pending volumes are clickable too — not to filter (there's nothing to
    # filter yet), but to preview that volume's own title page in the header,
    # shown inverted as an "undeveloped plate" placeholder.
    vol_chips.append(f'<button class="vol-chip {cls}" data-volume="{vnum}" data-ready="{"1" if meta["ready"] else "0"}">{label}</button>')
vol_chips_html = "\n".join(vol_chips)

total = len(ALL)

glossary_entries = []
for term in sorted(GLOSSARY.keys()):
    display = term[:1].upper() + term[1:]
    glossary_entries.append(f'<dt>{html.escape(display)}</dt><dd>{html.escape(GLOSSARY[term])}</dd>')
glossary_list_html = "\n".join(glossary_entries)

html_doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Birds of Europe &mdash; John Gould, in Five Volumes</title>
<style>
  :root {{
    --paper: #faf5ea;
    --paper-dark: #f0e6d2;
    --ink: #2b241b;
    --ink-soft: #5a4f3f;
    --accent: #7a5230;
    --accent-2: #8a6d3b;
    --border: #d8c9a8;
    --card-bg: #fffdf8;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    /* EXPERIMENT: the actual sampled colour of the inverted title page
       (#0a1b2d), used as a real background rather than a translucent tint
       over the cream — a much bigger swing, just to see how it reads. */
    background: #0a1b2d;
    color: #dfe4ec;
    font-family: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, "Times New Roman", serif;
  }}
  .about, .about p {{ color: #c3cad8; }}
  .about summary {{ color: #9bb3d9; }}
  #count, .filter-row, .vol-chip.pending {{ color: #aeb8ca; }}
  .no-results {{ color: #aeb8ca; }}
  footer {{ color: #aeb8ca; }}
  .body-watermark {{
    position: fixed;
    inset: 0;
    z-index: -1;
    background-size: cover;
    background-position: center top;
    background-repeat: no-repeat;
    filter: grayscale(100%) contrast(0.85);
    opacity: 0;
    transition: opacity 1.1s ease;
    pointer-events: none;
  }}
  .body-watermark.showing {{ opacity: 0.06; }}
  header {{
    position: relative;
    text-align: center;
    padding: 64px 20px 40px;
    min-height: 420px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-bottom: 1px solid var(--border);
    background: var(--paper-dark);
    overflow: hidden;
  }}
  .header-bg {{
    position: absolute;
    inset: 0;
    background-size: cover;
    background-position: top center;
    background-repeat: no-repeat;
    transition: opacity 0.9s ease;
  }}
  .header-overlay {{
    position: absolute;
    inset: 0;
    background: linear-gradient(rgba(240,230,210,0.55), rgba(240,230,210,0.82));
    z-index: 1;
    transition: opacity 0.9s ease;
  }}
  .header-overlay.dimmed {{
    background: linear-gradient(rgba(240,230,210,0.25), rgba(240,230,210,0.5));
  }}
  /* Not-yet-digitised volumes, previewed as a negative: much less contrast
     than the "dimmed" state above — a hint of the page, not a wall of dark
     navy. Refine further once the overall tone feels right. */
  .header-overlay.negative {{
    background: linear-gradient(rgba(240,230,210,0.78), rgba(240,230,210,0.88));
  }}
  .header-inner {{
    position: relative;
    z-index: 2;
  }}
  header .eyebrow {{
    letter-spacing: 0.25em;
    text-transform: uppercase;
    font-size: 12px;
    color: var(--accent);
    margin-bottom: 10px;
  }}
  header h1 {{
    font-size: clamp(28px, 4vw, 44px);
    margin: 0 0 8px;
    font-weight: 400;
    letter-spacing: 0.02em;
    color: var(--ink);
  }}
  header p.sub {{
    color: var(--ink-soft);
    font-size: 15px;
    margin: 0 auto;
    max-width: 680px;
    line-height: 1.5;
  }}
  .about {{
    max-width: 760px;
    margin: 0 auto;
    padding: 30px 24px 6px;
    line-height: 1.7;
    color: var(--ink);
  }}
  .about summary {{
    cursor: pointer;
    color: var(--accent);
    font-weight: 600;
    font-size: 14px;
    margin-bottom: 10px;
    text-align: center;
  }}
  .about p {{ margin: 0 0 14px; font-size: 14.5px; }}
  .about details + details {{ margin-top: 4px; }}
  .glossary-list {{
    columns: 2;
    column-gap: 32px;
    font-size: 13.5px;
    margin: 10px 0 0;
  }}
  .glossary-list dt {{
    font-weight: 700;
    color: #d9b98a;
    break-inside: avoid;
    margin-top: 10px;
  }}
  .glossary-list dd {{
    margin: 2px 0 0;
    color: #c3cad8;
    break-inside: avoid;
  }}
  @media (max-width: 640px) {{
    .glossary-list {{ columns: 1; }}
  }}
  .toolbar {{
    max-width: 1200px;
    margin: 24px auto 0;
    padding: 0 24px;
    display: flex;
    justify-content: center;
  }}
  #search {{
    width: 100%;
    max-width: 460px;
    padding: 10px 16px;
    font-size: 15px;
    border: 1px solid var(--border);
    border-radius: 999px;
    background: var(--card-bg);
    color: var(--ink);
    font-family: inherit;
    outline: none;
  }}
  #search:focus {{ border-color: var(--accent-2); }}
  .vol-row {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 8px;
    margin: 16px auto 0;
    max-width: 1000px;
    padding: 0 24px;
  }}
  .vol-chip {{
    font-family: inherit;
    font-size: 12.5px;
    letter-spacing: 0.03em;
    padding: 7px 14px;
    border-radius: 999px;
    border: 1px solid var(--border);
    background: var(--card-bg);
    color: var(--ink-soft);
    cursor: pointer;
    transition: opacity 0.2s ease, border-color 0.2s ease, background 0.2s ease;
  }}
  .vol-chip.active {{
    background: var(--accent);
    color: #fbf2e2;
    border-color: var(--accent);
  }}
  .vol-chip.has-match:not(.active) {{
    border-color: var(--accent-2);
    border-width: 2px;
    color: var(--accent-2);
    font-weight: 700;
  }}
  .vol-chip.no-match:not(.active) {{
    opacity: 0.35;
  }}
  .vol-chip.pending {{
    opacity: 0.6;
    font-style: italic;
  }}
  .vol-chip.pending.active {{
    opacity: 1;
    font-style: normal;
    background: var(--card-bg);
    color: #4a5f8a;
    border: 2px solid #4a5f8a;
    font-weight: 700;
  }}
  #count {{
    text-align: center;
    color: var(--ink-soft);
    font-size: 13px;
    margin: 14px 0 0;
  }}
  .grid {{
    max-width: 1300px;
    margin: 30px auto 80px;
    padding: 0 24px;
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 26px;
  }}
  .card {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 4px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(43,36,27,0.08), 0 6px 18px rgba(43,36,27,0.05);
    display: flex;
    flex-direction: column;
    transition: transform 0.18s ease, box-shadow 0.18s ease;
  }}
  .card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 4px 10px rgba(43,36,27,0.12), 0 14px 30px rgba(43,36,27,0.10);
  }}
  .plate-frame {{
    /* A cool, muted blue-grey mat — the complementary of the warm buff
       paper — around each plate, the way a gallery mat is chosen to make
       a warm-toned print read more vividly than a same-tone mount would. */
    background: #dde3ec;
    border-bottom: 1px solid var(--border);
    padding: 10px;
    position: relative;
  }}
  .plate-frame img {{
    width: 100%;
    display: block;
    aspect-ratio: 3/4;
    object-fit: contain;
    object-position: center center;
    border: 1px solid #c7d0e0;
  }}
  .vol-tag {{
    position: absolute;
    top: 8px;
    right: 8px;
    background: rgba(43,36,27,0.72);
    color: #fbf2e2;
    font-size: 10px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 4px 8px;
    border-radius: 3px;
  }}
  .card-body {{
    padding: 14px 16px 18px;
    flex: 1;
    display: flex;
    flex-direction: column;
  }}
  .plate-no {{
    font-size: 10.5px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 4px;
  }}
  .en-name {{
    font-size: 19px;
    font-weight: 600;
    margin: 0 0 4px;
    line-height: 1.25;
    color: var(--ink);
  }}
  .gould-name {{
    font-size: 12px;
    color: var(--ink-soft);
    font-style: italic;
    margin-bottom: 6px;
  }}
  .latin {{
    font-style: italic;
    color: var(--accent);
    font-size: 14px;
    margin-bottom: 10px;
  }}
  .latin .author {{
    font-style: normal;
    color: var(--ink-soft);
    font-size: 12px;
  }}
  table.names {{
    border-collapse: collapse;
    font-size: 13.5px;
    margin-top: auto;
  }}
  table.names th {{
    text-align: left;
    color: var(--ink-soft);
    font-weight: 600;
    padding: 2px 8px 2px 0;
    width: 28px;
    vertical-align: top;
  }}
  table.names td {{
    padding: 2px 0;
    color: var(--ink);
  }}
  .tag-chips {{
    display: flex;
    flex-wrap: wrap;
    gap: 5px;
    margin-top: 10px;
  }}
  .tag-chip {{
    font-family: inherit;
    font-size: 10.5px;
    letter-spacing: 0.02em;
    padding: 3px 9px;
    border-radius: 999px;
    border: 1px solid var(--border);
    background: var(--paper);
    color: var(--ink-soft);
    cursor: pointer;
    transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease;
  }}
  .tag-chip:hover {{
    border-color: var(--accent-2);
    color: var(--accent-2);
  }}
  .tag-chip.active-tag {{
    background: var(--accent);
    border-color: var(--accent);
    color: #fbf2e2;
  }}
  .family-chip {{ font-weight: 600; }}
  .genus-chip {{ font-style: italic; }}
  .genus-chip.genus-1837 {{ border-style: dashed; }}
  .artist-chip {{ opacity: 0.85; }}
  /* Glossary hover terms: a soft dotted underline that reads as "there's
     more here" without shouting like a hyperlink would. */
  .gloss-term {{
    border-bottom: 1px dotted var(--accent-2);
    cursor: help;
    position: relative;
  }}
  /* The tip is reparented to <body> at runtime (see JS) and positioned with
     JS-computed fixed coordinates, so it isn't a descendant of .card at
     display time and can't be clipped by .card's overflow:hidden -- even
     while .card:hover's transform is active, which would otherwise make a
     plain position:fixed child of .card resolve against .card instead of
     the viewport. Visibility is toggled with the .tip-visible class instead
     of :hover/:focus, since the tip is no longer inside .gloss-term. */
  .gloss-tip {{
    display: none;
    position: fixed;
    width: max-content;
    max-width: 260px;
    background: #2b241b;
    color: #fbf2e2;
    font-size: 12px;
    line-height: 1.4;
    font-style: normal;
    padding: 8px 10px;
    border-radius: 6px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.25);
    z-index: 500;
    text-align: left;
  }}
  .gloss-tip.tip-visible {{
    display: block;
  }}
  .gloss-tip::after {{
    content: '';
    position: absolute;
    left: var(--arrow-left, 50%);
    transform: translateX(-50%);
    border: 5px solid transparent;
  }}
  .gloss-tip.tip-above::after {{
    top: 100%;
    border-top-color: #2b241b;
  }}
  .gloss-tip.tip-below::after {{
    bottom: 100%;
    border-bottom-color: #2b241b;
  }}
  /* Taxonomic-authority hover terms (the "Pall." / "Temm." / etc. after a
     Latin binomial) -- same dotted-underline affordance and viewport-safe
     tooltip mechanics as .gloss-term, but a wider tip since a bio runs
     longer than a glossary definition, plus room for a name line and an
     optional Wikipedia link. */
  .authority-term {{
    border-bottom: 1px dotted var(--accent-2);
    cursor: help;
  }}
  .authority-tip {{
    max-width: 320px;
  }}
  .authority-tip .auth-name {{
    font-weight: 600;
    color: #fbf2e2;
  }}
  .authority-tip .auth-meta {{
    display: block;
    color: #cdbfa4;
    font-size: 11px;
    margin: 1px 0 6px;
  }}
  .authority-tip .auth-notable {{
    display: block;
    margin-top: 6px;
    font-style: italic;
    color: #e4d9c2;
  }}
  .authority-tip a {{
    display: inline-block;
    margin-top: 6px;
    color: #f3c98b;
    text-decoration: none;
    font-size: 11.5px;
  }}
  .authority-tip a:hover {{
    text-decoration: underline;
  }}
  .active-filter-bar {{
    text-align: center;
    margin: 10px 0 0;
  }}
  .active-filter-bar button {{
    font-family: inherit;
    font-size: 12px;
    padding: 5px 12px;
    border-radius: 999px;
    border: 1px solid var(--accent);
    background: var(--accent);
    color: #fbf2e2;
    cursor: pointer;
  }}
  .artist-credit {{
    font-size: 10.5px;
    color: var(--ink-soft);
    margin-top: 8px;
    letter-spacing: 0.02em;
  }}
  .status-box {{
    margin-top: 12px;
    padding: 8px 12px;
    border-radius: 3px;
    font-size: 12.5px;
    line-height: 1.5;
    border-left: 3px solid var(--accent-2);
    background: #f3ede1;
  }}
  .status-label {{
    font-size: 10px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 4px;
    color: var(--accent-2);
  }}
  .status-box p {{ margin: 0 0 4px; color: var(--ink); }}
  .status-box p:last-child {{ margin-bottom: 0; }}
  .status-split .status-label, .status-contested .status-label {{ color: #9a4a2a; }}
  .status-unresolved .status-label {{ color: #7a5230; }}
  .gen-char {{ margin-top: 10px; font-size: 12px; }}
  .gen-char summary {{ cursor: pointer; color: var(--accent); font-size: 11.5px; }}
  .gen-char-text {{ margin: 6px 0 0; font-style: italic; color: var(--ink-soft); line-height: 1.5; }}
  .gould-text {{ margin-top: 10px; font-size: 12px; }}
  .gould-text summary {{ cursor: pointer; color: var(--accent); font-size: 11.5px; font-weight: 600; }}
  .gould-text-body {{ margin: 8px 0 0; font-style: italic; color: var(--ink-soft); line-height: 1.6; max-height: 340px; overflow-y: auto; padding-right: 6px; }}
  footer {{
    text-align: center;
    padding: 30px 20px 60px;
    color: var(--ink-soft);
    font-size: 12.5px;
  }}
  .no-results {{
    text-align: center;
    color: var(--ink-soft);
    padding: 60px 20px;
    display: none;
  }}
  .card-obsolete {{ border-color: #c9a876; }}
  .badge {{
    position: absolute;
    top: 8px;
    left: 8px;
    background: #6b3f2a;
    color: #fbf2e2;
    font-size: 10px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 4px 8px;
    border-radius: 3px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.25);
  }}
  .history-box {{
    margin-top: 12px;
    padding: 10px 12px;
    background: #f6ecd9;
    border: 1px solid #d9c298;
    border-left: 3px solid var(--accent);
    border-radius: 3px;
    font-size: 12.5px;
    line-height: 1.5;
    color: var(--ink);
  }}
  .history-label {{
    font-size: 10px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent);
    font-weight: 600;
    margin-bottom: 6px;
  }}
  .history-box p {{ margin: 0 0 6px; }}
  .history-box p:last-child {{ margin-bottom: 0; }}
  .filter-row {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    margin-top: 12px;
    font-size: 13px;
    color: var(--ink-soft);
  }}
  .filter-row label {{ display: flex; align-items: center; gap: 6px; cursor: pointer; }}
</style>
</head>
<body>

<div class="body-watermark" id="bodyBgA"></div>
<div class="body-watermark" id="bodyBgB"></div>

<header id="mainHeader">
  <div class="header-bg" id="headerBgA" style="opacity:1; background-image:url('{V1_TITLE_URI}');"></div>
  <div class="header-bg" id="headerBgB" style="opacity:0;"></div>
  <div class="header-overlay" id="headerOverlay"></div>
  <div class="header-inner">
    <div class="eyebrow" id="eyebrowText">John Gould &middot; 1832&ndash;1837 &middot; In Five Volumes</div>
    <h1>The Birds of Europe</h1>
    <p class="sub">One gallery for the whole set. All {total} plates across all five volumes
    (Raptores, Insessores, Rasores &amp; Grallatores, and Natatores) &mdash; search and filter across all of them at once.</p>
  </div>
</header>

<div class="about">
  <details>
    <summary>About this gallery &mdash; why it exists, and how to read it</summary>
    <p>This gallery began as a wish to see John Gould's hand-coloured plates of European birds gathered
    in one place, each paired with its name in English, German, French and Latin. It became something
    more while building it &mdash; a way of holding two centuries side by side.</p>
    <p>Every card marks a small scientific claim Gould made in the 1830s and 40s, and what has happened
    to that claim since. Most held up. Some were quietly moved to a different genus as relationships
    were reassessed; a few were split into two or more species once modern tools could tell them apart;
    a couple never resolved at all, and Gould's uncertainty is still, honestly, ours. Where we know
    <em>how</em> a question was settled &mdash; a DNA study, a close study of song, a hybrid zone tracked
    for decades &mdash; that's noted too, so the change reads as a method, not a verdict from nowhere.
    Gould worked before Darwin's <em>Origin of Species</em>, decades before Mendel, a century and a half
    before anyone could read a bird's DNA. His plates aren't wrong where they differ from today's
    understanding; they're an earlier stage of the same enquiry, using the only tools his century had.</p>
    <p>Where the original text survived clearly enough, some cards also carry a short excerpt from
    Gould's own genus description &mdash; notice how much of it is anatomy read from a dead specimen in
    a drawer, and how little is song, behaviour, migration or habitat. That shift is arguably the
    biggest change in how ornithology is practised, driven by tools Gould never had: DNA sequencing,
    satellite tags and geolocators, and sound recording and analysis (the same basic technique apps like
    the Cornell Lab's Merlin now put in anyone's pocket).</p>
    <p>The plates are credited, on almost every one, to &ldquo;J. &amp; E. Gould&rdquo;. The second
    initial is Elizabeth Gould, John's wife, who drew nearly every one of these lithographs from his
    field sketches. She died in 1841, at 37, and her name has mostly been folded into her husband's ever
    since. This gallery names her on every plate she drew.</p>
    <p>Released under the MIT License: use it, adapt it, teach from it. The historical plates themselves
    are in the public domain.</p>
  </details>
  <details>
    <summary>Terminology glossary &mdash; anatomy &amp; taxonomy terms explained</summary>
    <p>Every underlined term you see on a card &mdash; in a genus description, a status note, or Gould's
    own account &mdash; can be hovered (or tapped, on a phone or tablet) to show its definition right where
    you're reading. This is the same list, gathered in one place, for browsing or classroom use. It covers
    two kinds of vocabulary: the anatomical language Gould uses to describe a bird's bill, feathers and feet,
    and the taxonomy and history-of-science language this gallery uses to describe how a name or
    classification has changed since 1837.</p>
    <dl class="glossary-list">
      {glossary_list_html}
    </dl>
  </details>
</div>

<div class="toolbar">
  <input type="text" id="search" placeholder="Search by name (English, German, French, or Latin)&hellip;">
</div>
<div class="vol-row">
{vol_chips_html}
</div>
<div class="filter-row">
  <label><input type="checkbox" id="obsoleteOnly"> Show only the {obsolete_count} plates later found not to be valid species</label>
</div>
<p id="count"></p>
<div class="active-filter-bar" id="activeFilterBar" style="display:none;"></div>

<div class="grid" id="grid">
{grid}
</div>
<p class="no-results" id="noResults">No plates match your search.</p>

<footer>
  Digitised from Internet Archive scans of <em>The Birds of Europe</em> by John Gould, drawn and
  lithographed almost entirely by Elizabeth Gould from John&rsquo;s field sketches. Gould&rsquo;s
  original English names are shown where they differ from the modern common name; modern scientific
  names and German/French common names reflect current usage. A handful of plates are included as
  Gould described and figured them even though they're not valid species today &mdash; a small case
  study in how species concepts get revised as evidence accumulates.
  <br><br>
  This gallery &mdash; its code, data and commentary &mdash; is released under the MIT License. The
  historical plates themselves are in the public domain.
</footer>

<script>
  const search = document.getElementById('search');
  const obsoleteOnly = document.getElementById('obsoleteOnly');
  const volChips = Array.from(document.querySelectorAll('.vol-chip'));
  const cards = Array.from(document.querySelectorAll('.card'));
  const countEl = document.getElementById('count');
  const noResults = document.getElementById('noResults');
  const activeFilterBar = document.getElementById('activeFilterBar');
  let activeVolume = 'ALL';

  // Family / Genus(1837) / Genus(today) / Artist chips: clicking one filters
  // the whole gallery down to every plate sharing that exact value — the
  // "before vs after" view for genus, since a card can carry a different
  // chip for its 1837 genus than for today's.
  const TAG_DATA_KEY = {{ family: 'family', genus1837: 'genus1837', genusModern: 'genusmodern', artist: 'artist' }};
  const TAG_LABEL = {{ family: 'Family', genus1837: 'Genus (1837)', genusModern: 'Genus (today)', artist: 'Artist' }};
  let activeTag = null; // {{ type, value }}

  function renderActiveFilterBar() {{
    if (!activeTag) {{
      activeFilterBar.style.display = 'none';
      activeFilterBar.innerHTML = '';
      return;
    }}
    activeFilterBar.style.display = 'block';
    activeFilterBar.innerHTML = `<button id="clearTagFilter">${{TAG_LABEL[activeTag.type]}}: ${{activeTag.value}} &times;</button>`;
    document.getElementById('clearTagFilter').addEventListener('click', () => {{
      activeTag = null;
      refreshTagChipStates();
      renderActiveFilterBar();
      update();
    }});
  }}

  function refreshTagChipStates() {{
    document.querySelectorAll('.tag-chip').forEach(chip => {{
      const isActive = !!activeTag && chip.dataset.type === activeTag.type && chip.dataset.value === activeTag.value;
      chip.classList.toggle('active-tag', isActive);
    }});
  }}

  document.getElementById('grid').addEventListener('click', (e) => {{
    const chip = e.target.closest('.tag-chip');
    if (!chip) return;
    const type = chip.dataset.type, value = chip.dataset.value;
    if (activeTag && activeTag.type === type && activeTag.value === value) {{
      activeTag = null;
    }} else {{
      activeTag = {{ type, value }};
    }}
    refreshTagChipStates();
    renderActiveFilterBar();
    update();
  }});

  // Title-page images per volume, for the header background. Ready volumes
  // show their real title page normally; volumes not yet digitised show
  // theirs inverted — a placeholder that's still real content, not a blank
  // swatch, evoking an undeveloped photographic negative waiting to "come
  // into the light" once that volume is actually built.
  const TITLE_PAGES = {{
    'I': '{V1_TITLE_URI}',
    'II': '{V2_TITLE_URI}',
    'III': '{V3_TITLE_URI}',
    'IV': '{V4_TITLE_URI}',
    'V': '{V5_TITLE_URI}',
  }};
  const READY_VOLUMES = new Set(['I', 'II', 'III', 'IV', 'V']);
  const headerBgA = document.getElementById('headerBgA');
  const headerBgB = document.getElementById('headerBgB');
  const headerOverlay = document.getElementById('headerOverlay');
  const eyebrowText = document.getElementById('eyebrowText');
  const bodyBgA = document.getElementById('bodyBgA');
  const bodyBgB = document.getElementById('bodyBgB');
  let bgToggle = false;     // tracks which header layer is currently on top
  let bodyBgToggle = false; // tracks which body-watermark layer is currently on top

  function setHeaderBg(vol) {{
    const uri = TITLE_PAGES[vol] || TITLE_PAGES['II'];

    const showing = bgToggle ? headerBgB : headerBgA;
    const hidden = bgToggle ? headerBgA : headerBgB;
    hidden.style.backgroundImage = `url('${{uri}}')`;
    hidden.style.opacity = '1';
    showing.style.opacity = '0';
    bgToggle = !bgToggle;

    const bodyShowing = bodyBgToggle ? bodyBgB : bodyBgA;
    const bodyHidden = bodyBgToggle ? bodyBgA : bodyBgB;
    bodyHidden.style.backgroundImage = `url('${{uri}}')`;
    bodyHidden.classList.add('showing');
    bodyShowing.classList.remove('showing');
    bodyBgToggle = !bodyBgToggle;

    const isPending = vol !== 'ALL' && !READY_VOLUMES.has(vol);
    headerOverlay.classList.toggle('dimmed', vol !== 'ALL' && !isPending);
    headerOverlay.classList.toggle('negative', isPending);
    if (vol === 'ALL') {{
      eyebrowText.textContent = 'John Gould · 1832–1837 · In Five Volumes';
    }} else if (READY_VOLUMES.has(vol)) {{
      eyebrowText.textContent = `Now showing the title page of Volume ${{vol}}`;
    }} else {{
      eyebrowText.textContent = `Editor's Note: Volume ${{vol}} isn't digitised yet — shown here as a negative until it's ready.`;
    }}
  }}

  volChips.forEach(chip => {{
    chip.addEventListener('click', () => {{
      activeVolume = (activeVolume === chip.dataset.volume) ? 'ALL' : chip.dataset.volume;
      volChips.forEach(c => c.classList.toggle('active', c.dataset.volume === activeVolume));
      setHeaderBg(activeVolume);
      update();
    }});
  }});

  function update() {{
    const q = search.value.trim().toLowerCase();
    const onlyObsolete = obsoleteOnly.checked;
    let visible = 0;
    const volumesWithMatches = new Set();
    cards.forEach(c => {{
      const matchesSearch = !q || c.dataset.search.includes(q);
      const matchesObsolete = !onlyObsolete || c.dataset.obsolete === '1';
      if (matchesSearch && matchesObsolete) volumesWithMatches.add(c.dataset.volume);
      const matchesVolume = activeVolume === 'ALL' || c.dataset.volume === activeVolume;
      const matchesTag = !activeTag || c.dataset[TAG_DATA_KEY[activeTag.type]] === activeTag.value;
      const match = matchesSearch && matchesObsolete && matchesVolume && matchesTag;
      c.style.display = match ? '' : 'none';
      if (match) visible++;
    }});
    countEl.textContent = visible + ' of ' + cards.length + ' plates';
    if (visible === 0 && activeVolume !== 'ALL' && !READY_VOLUMES.has(activeVolume)) {{
      noResults.textContent = `Editor's Note: Volume ${{activeVolume}} hasn't been digitised yet — that's a first look at its title page above.`;
    }} else {{
      noResults.textContent = 'No plates match your search.';
    }}
    noResults.style.display = visible === 0 ? 'block' : 'none';

    // Chips act as a live legend of where matches live, not just filters:
    // a chip lights up when its volume has at least one match for the
    // current search, and dims when it has none — whether or not that
    // chip is the active filter. Pending volumes never get a match.
    volChips.forEach(chip => {{
      const vol = chip.dataset.volume;
      if (!READY_VOLUMES.has(vol)) return;
      const has = volumesWithMatches.has(vol);
      chip.classList.toggle('has-match', !!q && has);
      chip.classList.toggle('no-match', !!q && !has);
    }});
  }}
  search.addEventListener('input', () => {{
    // Typing a search always starts from a cross-volume view — an active
    // volume filter left over from earlier browsing shouldn't silently
    // hide matches in other volumes.
    if (activeVolume !== 'ALL') {{
      activeVolume = 'ALL';
      volChips.forEach(c => c.classList.remove('active'));
      setHeaderBg('ALL');
    }}
    update();
  }});
  obsoleteOnly.addEventListener('change', update);
  setHeaderBg('ALL');
  update();

  // Glossary + taxonomic-authority hover tooltips. A .gloss-term carries its
  // definition in data-def (plain text); an .authority-term carries a
  // base64-encoded HTML bio (name/dates/bio/Wikipedia link) in data-bio-b64,
  // since a bio needs real markup (bold name, a link) rather than plain
  // text. Both share the same tip mechanics: the tip bubble is appended
  // directly to <body> (not to the term) and positioned in JS with fixed
  // coordinates clamped to the viewport, so it always shows in full
  // regardless of where the term sits inside a card -- a plain CSS
  // position:absolute/fixed child of the term would get clipped by the
  // card's overflow:hidden whenever it crossed the card's edge. Shown on
  // hover/focus (desktop) and toggled by tap (touch, since there's no
  // hover there).
  document.querySelectorAll('.gloss-term, .authority-term').forEach(term => {{
    const isAuthority = term.classList.contains('authority-term');
    const tip = document.createElement('span');
    tip.className = isAuthority ? 'gloss-tip authority-tip' : 'gloss-tip';
    if (isAuthority) {{
      // atob() gives a byte-per-char "binary string" -- decode it as UTF-8
      // properly (rather than passing straight through, which mangles the
      // en-dashes and middot in these bios into mojibake) before injecting.
      const bin = atob(term.dataset.bioB64);
      const bytes = Uint8Array.from(bin, c => c.charCodeAt(0));
      tip.innerHTML = new TextDecoder('utf-8').decode(bytes);
    }} else {{
      tip.textContent = term.dataset.def;
    }}
    document.body.appendChild(tip);
    term._glossTip = tip;

    const positionTip = () => {{
      const margin = 10;
      const gap = 8;
      const termRect = term.getBoundingClientRect();
      // Measure the tip's natural size by showing it off-position first.
      tip.classList.add('tip-visible');
      const tipRect = tip.getBoundingClientRect();

      let left = termRect.left + termRect.width / 2 - tipRect.width / 2;
      left = Math.max(margin, Math.min(left, window.innerWidth - tipRect.width - margin));

      const spaceAbove = termRect.top;
      const showBelow = spaceAbove < tipRect.height + gap + margin;
      let top;
      if (showBelow) {{
        top = termRect.bottom + gap;
        tip.classList.remove('tip-above');
        tip.classList.add('tip-below');
      }} else {{
        top = termRect.top - tipRect.height - gap;
        tip.classList.remove('tip-below');
        tip.classList.add('tip-above');
      }}
      top = Math.max(margin, Math.min(top, window.innerHeight - tipRect.height - margin));

      tip.style.left = left + 'px';
      tip.style.top = top + 'px';
      // Point the little arrow at the term's own center, not the tip's
      // (they can differ once the tip has been shifted to stay on-screen).
      const arrowLeft = Math.max(10, Math.min(termRect.left + termRect.width / 2 - left, tipRect.width - 10));
      tip.style.setProperty('--arrow-left', arrowLeft + 'px');
    }};
    const showTip = () => positionTip();
    const hideTip = () => {{
      if (!term.classList.contains('tip-open')) tip.classList.remove('tip-visible');
    }};

    term.addEventListener('mouseenter', showTip);
    term.addEventListener('mouseleave', hideTip);
    term.addEventListener('focus', showTip);
    term.addEventListener('blur', hideTip);
    term.addEventListener('click', (e) => {{
      e.stopPropagation();
      const wasOpen = term.classList.contains('tip-open');
      document.querySelectorAll('.gloss-term.tip-open, .authority-term.tip-open').forEach(t => {{
        t.classList.remove('tip-open');
        if (t._glossTip) t._glossTip.classList.remove('tip-visible');
      }});
      if (!wasOpen) {{
        term.classList.add('tip-open');
        positionTip();
      }}
    }});
  }});
  document.addEventListener('click', () => {{
    document.querySelectorAll('.gloss-term.tip-open, .authority-term.tip-open').forEach(t => {{
      t.classList.remove('tip-open');
      if (t._glossTip) t._glossTip.classList.remove('tip-visible');
    }});
  }});
  window.addEventListener('scroll', () => {{
    document.querySelectorAll('.gloss-term.tip-open, .authority-term.tip-open').forEach(t => t.classList.remove('tip-open'));
    document.querySelectorAll('.gloss-tip.tip-visible').forEach(tip => tip.classList.remove('tip-visible'));
  }}, {{ passive: true }});
</script>

</body>
</html>
'''

with open('app.html', 'w', encoding='utf-8') as f:
    f.write(html_doc)

print("Wrote app.html", os.path.getsize('app.html')/1024/1024, "MB")
print("Total records:", total, "obsolete:", obsolete_count)
