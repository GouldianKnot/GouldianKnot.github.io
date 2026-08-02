# Birds of Great Britain (Gould, 1862-73), Volume III.
# Reconnaissance + OCR + heading-extraction pass completed 2026-08-01. Source:
# birdsgreatbrita3goul.pdf (Internet Archive scan, 308 pages). 76 plates identified
# by a centre-cropped colourfulness heuristic, covering 69 distinct species/forms.
# Front matter (pages 1-7, the gilt leather cover and title page) and back matter
# (pages 301-308, blank foxed endpapers and the back cover) were excluded as
# colourfulness false positives after direct visual inspection -- the leather
# binding reads as "colourful" to the detector just like blank foxed pages did
# in Volume II.
#
# Fields: same schema as species_gb_vol1.py/species_gb_vol2.py -- see those files'
# headers for the full field-by-field explanation. "latin"/"author" are always
# taken from the actual printed heading line, not the older synonyms below it.
#
# SEVEN shared-account plate pairs in this volume (adult + "Young", or two related
# forms, sharing one written account -- confirmed by viewing each blank would-be
# text page AND the extra plate's own printed caption before trusting it):
#   plate 35  (Grey Wagtail, "Winter plumage")   shares plate 32's  text (page 33)
#   plate 173 (Bullfinch, "Young")                shares plate 170's text (page 171)
#   plate 219 (Starling, "Young")                 shares plate 216's text (page 217)
#   plate 225 (Rose-coloured Pastor, "Young")      shares plate 222's text (page 223)
#   plate 263 (Nutcracker, "Young")                shares plate 260's text (page 261)
#   plate 269 (Cuckoo, "Young ejecting nestlings") shares plate 266's text (page 267)
#   plate 297 (Green Woodpecker, "Young")          shares plate 294's text (page 295)
# One near-miss worth recording: plate 192 (White-winged/Two-barred Crossbill) at
# first looked like it might share the Parrot Crossbill's account two plates
# earlier (its OCR came back 0 bytes on the first pass) -- but it turned out to be
# a genuine, fully independent account; the OCR simply failed on the first attempt
# and succeeded cleanly on retry. Recorded here as a reminder that a blank OCR
# result is not proof of a blank page -- always check the source image directly.
#
# NOT YET DONE: German/French names, Gould's running prose beyond what informed
# the modern-name research, thumbnail+hires image linkage (pending), Volumes IV-V.

SPECIES_GB_V3 = [
  dict(plate_page=12, text_page=13, english="Pied Wagtail", latin="Motacilla Yarrellii", author="Gould",
       modern_en="White Wagtail (Pied Wagtail)", modern_latin="Motacilla alba yarrellii", status="lumped",
       resolved_by="Gould treated this as its own species, distinct from the Continental White Wagtail two plates over. It is now treated as a British/Irish subspecies of the White Wagtail, Motacilla alba yarrellii, not a full species in its own right."),

  dict(plate_page=16, text_page=17, english="White Wagtail", latin="Motacilla alba", author="Linn.",
       modern_en="White Wagtail", modern_latin="Motacilla alba", status="stable",
       note="The nominate form of the same species as the Pied Wagtail above; the two were, and still are, considered close enough that Gould placed their plates back to back."),

  dict(plate_page=20, text_page=21, english="Yellow Wagtail", latin="Budytes Rayi", author="",
       modern_en="Western Yellow Wagtail (British subspecies)", modern_latin="Motacilla flava flavissima", status="lumped",
       resolved_by="The genus Budytes was absorbed into Motacilla, and this British breeding form -- named for the naturalist John Ray -- is now treated as the subspecies Motacilla flava flavissima rather than its own species."),

  dict(plate_page=24, text_page=25, english="Grey-headed Wagtail", latin="Budytes flava", author="",
       modern_en="Western Yellow Wagtail", modern_latin="Motacilla flava", status="lumped",
       resolved_by="Moved from Budytes into Motacilla; this and the next two plates (Budytes rayi, flava, cinereocapilla) are all now treated as subspecies within one wide-ranging, highly variable species, the Western Yellow Wagtail -- a striking case of Gould's three 'species' collapsing into subspecies of one."),

  dict(plate_page=28, text_page=29, english="Grey-capped Wagtail", latin="Budytes cinereocapilla", author="",
       modern_en="Western Yellow Wagtail (Ashy-headed subspecies)", modern_latin="Motacilla flava cinereocapilla", status="lumped",
       resolved_by="Moved from Budytes into Motacilla; treated today as the Ashy-headed subspecies of the Western Yellow Wagtail, Motacilla flava cinereocapilla, not a separate species -- see the note on the Grey-headed Wagtail two plates above."),

  dict(plate_page=32, text_page=33, english="Grey Wagtail", latin="Calobates sulphurea", author="",
       modern_en="Grey Wagtail", modern_latin="Motacilla cinerea", status="reclassified",
       resolved_by="Moved from Gould's genus Calobates back into Motacilla, and the species epithet standardised to cinerea."),

  dict(plate_page=35, text_page=None, shares_with=32, plate_note="winter plumage",
       english="Grey Wagtail", latin="Calobates sulphurea", author="",
       modern_en="Grey Wagtail", modern_latin="Motacilla cinerea", status="reclassified",
       resolved_by="Same species as plate 32; this plate shows the winter plumage and shares that plate's text.",
       note="Text page 34 (the expected page after this plate) belongs to the blank-verso pattern; the shared account is on page 33, before this plate."),

  dict(plate_page=38, text_page=39, english="Richard's Pipit", latin="Anthus Richardii", author="Vieill.",
       modern_en="Richard's Pipit", modern_latin="Anthus richardi", status="stable",
       note="Only the spelling of the species epithet was standardised, Richardii to richardi."),

  dict(plate_page=42, text_page=43, english="Tawny Pipit", latin="Anthus campestris", author="",
       modern_en="Tawny Pipit", modern_latin="Anthus campestris", status="stable"),

  dict(plate_page=46, text_page=47, english="Rock Pipit", latin="Anthus obscurus", author="",
       modern_en="Eurasian Rock Pipit", modern_latin="Anthus petrosus", status="reclassified",
       resolved_by="The species epithet was standardised from obscurus to petrosus; obscurus is now used only for a Scandinavian subspecies, Anthus petrosus obscurus."),

  dict(plate_page=50, text_page=51, english="Vinous Pipit", latin="Anthus spinoletta", author="",
       modern_en="Water Pipit", modern_latin="Anthus spinoletta", status="stable",
       note="Only the English name has shifted, from Gould's 'Vinous Pipit' to the modern 'Water Pipit'; the binomial is unchanged."),

  dict(plate_page=54, text_page=55, english="Red-throated Pipit", latin="Anthus cervinus", author="",
       modern_en="Red-throated Pipit", modern_latin="Anthus cervinus", status="stable"),

  dict(plate_page=58, text_page=59, english="Meadow-Pipit, or Titlark", latin="Anthus pratensis", author="",
       modern_en="Meadow Pipit", modern_latin="Anthus pratensis", status="stable"),

  dict(plate_page=62, text_page=63, english="Tree-Pipit", latin="Anthus arboreus", author="Bechst.",
       modern_en="Tree Pipit", modern_latin="Anthus trivialis", status="reclassified",
       resolved_by="The species epithet was standardised from arboreus to trivialis."),

  dict(plate_page=66, text_page=67, english="Sky-Lark", latin="Alauda arvensis", author="Linn.",
       modern_en="Eurasian Skylark", modern_latin="Alauda arvensis", status="stable"),

  dict(plate_page=70, text_page=71, english="Wood-Lark", latin="Alauda arborea", author="Linn.",
       modern_en="Woodlark", modern_latin="Lullula arborea", status="reclassified",
       resolved_by="Split out of Alauda into its own genus, Lullula, based on structural and vocal differences from the true larks."),

  dict(plate_page=74, text_page=75, english="Crested Lark", latin="Galerita cristata", author="",
       modern_en="Crested Lark", modern_latin="Galerida cristata", status="stable",
       note="Only the spelling of the genus was standardised, Galerita to Galerida."),

  dict(plate_page=78, text_page=79, english="Shore-Lark", latin="Otocoris alpestris", author="",
       modern_en="Horned Lark", modern_latin="Eremophila alpestris", status="reclassified",
       resolved_by="Moved from Otocoris into Eremophila, the currently recognised genus; the English name 'Shore Lark' is still used in Britain for the same species that is called 'Horned Lark' in North America."),

  dict(plate_page=82, text_page=83, english="Calandra Lark", latin="Melanocorypha calandra", author="",
       modern_en="Calandra Lark", modern_latin="Melanocorypha calandra", status="stable"),

  dict(plate_page=86, text_page=87, english="White-winged Lark", latin="Melanocorypha leucoptera", author="",
       modern_en="White-winged Lark", modern_latin="Melanocorypha leucoptera", status="stable"),

  dict(plate_page=90, text_page=91, english="Short-toed Lark", latin="Calandrella brachydactyla", author="",
       modern_en="Greater Short-toed Lark", modern_latin="Calandrella brachydactyla", status="stable"),

  dict(plate_page=94, text_page=95, english="Yellowhammer or Yellow Bunting", latin="Emberiza citrinella", author="Linn.",
       modern_en="Yellowhammer", modern_latin="Emberiza citrinella", status="stable"),

  dict(plate_page=98, text_page=99, english="Cirl Bunting", latin="Emberiza cirlus", author="Linn.",
       modern_en="Cirl Bunting", modern_latin="Emberiza cirlus", status="stable"),

  dict(plate_page=102, text_page=103, english="Rustic Bunting", latin="Emberiza rustica", author="Pall.",
       modern_en="Rustic Bunting", modern_latin="Emberiza rustica", status="stable"),

  dict(plate_page=106, text_page=107, english="Dwarf Bunting", latin="Emberiza pusilla", author="Pall.",
       modern_en="Little Bunting", modern_latin="Emberiza pusilla", status="stable",
       note="Only the English name has shifted, from Gould's 'Dwarf Bunting' to the modern 'Little Bunting'; the binomial is unchanged."),

  dict(plate_page=110, text_page=111, english="Common Bunting", latin="Crithophaga miliaria", author="",
       modern_en="Corn Bunting", modern_latin="Emberiza calandra", status="reclassified",
       resolved_by="Moved from Gould's genus Crithophaga back into Emberiza, with the species epithet standardised to calandra; the modern English name 'Corn Bunting' has replaced Gould's more generic 'Common Bunting'."),

  dict(plate_page=114, text_page=115, english="Ortolan Bunting", latin="Glycyspina hortulana", author="",
       modern_en="Ortolan Bunting", modern_latin="Emberiza hortulana", status="reclassified",
       resolved_by="Moved from Gould's genus Glycyspina back into Emberiza."),

  dict(plate_page=118, text_page=119, english="Black-headed Euspiza", latin="Euspiza melanocephala", author="",
       modern_en="Black-headed Bunting", modern_latin="Emberiza melanocephala", status="reclassified",
       resolved_by="Moved from Euspiza back into Emberiza; the modern English name drops Gould's genus-derived 'Euspiza' in favour of the plain 'Black-headed Bunting'."),

  dict(plate_page=122, text_page=123, english="Reed-Bunting", latin="Schoenicola arundinacea", author="",
       modern_en="Common Reed Bunting", modern_latin="Emberiza schoeniclus", status="reclassified",
       resolved_by="Moved from Gould's genus Schoenicola back into Emberiza, and the species epithet standardised to schoeniclus."),

  dict(plate_page=126, text_page=127, english="Lapland Bunting", latin="Centrophanes lapponica", author="",
       modern_en="Lapland Longspur", modern_latin="Calcarius lapponicus", status="reclassified",
       resolved_by="Moved from Gould's genus Centrophanes into Calcarius, the currently recognised longspur genus; still called 'Lapland Bunting' in British usage even though the modern genus places it with the longspurs rather than the true buntings."),

  dict(plate_page=130, text_page=131, english="Snow-Bunting, or Snowflake", latin="Plectrophanes nivalis", author="",
       modern_en="Snow Bunting", modern_latin="Plectrophenax nivalis", status="stable",
       note="Only the spelling of the genus was standardised, Plectrophanes to Plectrophenax."),

  dict(plate_page=134, text_page=135, english="Common or House Sparrow", latin="Passer domesticus", author="Ray",
       modern_en="House Sparrow", modern_latin="Passer domesticus", status="stable"),

  dict(plate_page=138, text_page=139, english="Tree-Sparrow", latin="Passer montanus", author="Ray",
       modern_en="Eurasian Tree Sparrow", modern_latin="Passer montanus", status="stable"),

  dict(plate_page=142, text_page=143, english="Chaffinch", latin="Fringilla caelebs", author="",
       modern_en="Common Chaffinch", modern_latin="Fringilla coelebs", status="stable",
       note="Only a spelling variant of the same epithet (caelebs/coelebs)."),

  dict(plate_page=146, text_page=147, english="Bramble-Finch", latin="Fringilla montifringilla", author="",
       modern_en="Brambling", modern_latin="Fringilla montifringilla", status="stable"),

  dict(plate_page=150, text_page=151, english="Goldfinch", latin="Carduelis elegans", author="",
       modern_en="European Goldfinch", modern_latin="Carduelis carduelis", status="stable",
       note="Only the species epithet was standardised, elegans to carduelis, matching the genus."),

  dict(plate_page=154, text_page=155, english="Siskin", latin="Chrysomitris spinus", author="",
       modern_en="Eurasian Siskin", modern_latin="Spinus spinus", status="reclassified",
       resolved_by="Moved from Gould's genus Chrysomitris into Spinus, the currently recognised siskin genus."),

  dict(plate_page=158, text_page=159, english="Serin Finch", latin="Serinus hortulanus", author="",
       modern_en="European Serin", modern_latin="Serinus serinus", status="stable",
       note="Only the species epithet was standardised, hortulanus to serinus, matching the genus."),

  dict(plate_page=162, text_page=163, english="Greenfinch", latin="Ligurinus chloris", author="",
       modern_en="European Greenfinch", modern_latin="Chloris chloris", status="reclassified",
       resolved_by="Moved from Gould's genus Ligurinus into Chloris, with the species epithet standardised to match the genus."),

  dict(plate_page=166, text_page=167, english="Hawfinch", latin="Coccothraustes vulgaris", author="",
       modern_en="Hawfinch", modern_latin="Coccothraustes coccothraustes", status="stable",
       note="The genus was already correct in Gould's heading; only the species epithet was standardised, vulgaris to coccothraustes, matching the genus."),

  dict(plate_page=170, text_page=171, english="Bullfinch", latin="Pyrrhula vulgaris", author="",
       modern_en="Eurasian Bullfinch", modern_latin="Pyrrhula pyrrhula", status="stable",
       note="Only the species epithet was standardised, vulgaris to pyrrhula, matching the genus."),

  dict(plate_page=173, text_page=None, shares_with=170, plate_note="young",
       english="Bullfinch", latin="Pyrrhula vulgaris", author="",
       modern_en="Eurasian Bullfinch", modern_latin="Pyrrhula pyrrhula", status="stable",
       resolved_by="Same species as plate 170; this plate shows a young pair at the nest and shares that plate's text."),

  dict(plate_page=176, text_page=177, english="Scarlet Bullfinch", latin="Carpodacus erythrinus", author="",
       modern_en="Common Rosefinch", modern_latin="Carpodacus erythrinus", status="stable",
       note="The binomial is unchanged; only the English name has shifted from Gould's 'Scarlet Bullfinch' to the modern 'Common Rosefinch', since it is not a true bullfinch."),

  dict(plate_page=180, text_page=181, english="Pine-Grosbeak", latin="Pinicola enucleator", author="",
       modern_en="Pine Grosbeak", modern_latin="Pinicola enucleator", status="stable"),

  dict(plate_page=184, text_page=185, english="Common Crossbill", latin="Loxia curvirostra", author="Linn.",
       modern_en="Red Crossbill (Common Crossbill)", modern_latin="Loxia curvirostra", status="stable"),

  dict(plate_page=188, text_page=189, english="Parrot Crossbill", latin="Loxia pityopsittacus", author="Bechst.",
       modern_en="Parrot Crossbill", modern_latin="Loxia pityopsittacus", status="stable"),

  dict(plate_page=192, text_page=193, english="White-winged Crossbill", latin="Loxia bifasciata", author="",
       modern_en="Two-barred Crossbill", modern_latin="Loxia bifasciata", status="stable",
       note="The binomial is unchanged; only the English name has shifted, from Gould's 'White-winged Crossbill' to the modern 'Two-barred Crossbill', to avoid confusion with the similarly-named American species on the next plate. Its own account (page 193) was initially misread as blank by this pass's OCR -- a retry on the same image produced clean text, a useful reminder not to trust a single failed OCR pass as proof of a blank page."),

  dict(plate_page=196, text_page=197, english="American White-winged Crossbill", latin="Loxia leucoptera", author="Gmel.",
       modern_en="White-winged Crossbill", modern_latin="Loxia leucoptera", status="stable",
       note="A genuinely different species from the previous plate's Two-barred Crossbill, despite the near-identical old English names -- Gould's heading already distinguishes them by calling this one 'American'."),

  dict(plate_page=200, text_page=201, english="Linnet", latin="Linota cannabina", author="",
       modern_en="Common Linnet", modern_latin="Linaria cannabina", status="reclassified",
       resolved_by="Moved from Gould's genus Linota into Linaria, the currently recognised genus."),

  dict(plate_page=204, text_page=205, english="Twite or Mountain-Linnet", latin="Linota montium", author="",
       modern_en="Twite", modern_latin="Linaria flavirostris", status="reclassified",
       resolved_by="Moved from Linota into Linaria alongside the Common Linnet, with the species epithet standardised to flavirostris."),

  dict(plate_page=208, text_page=209, english="Mealy Redpole", latin="Aegiothus linaria", author="",
       modern_en="Mealy Redpoll (Common Redpoll)", modern_latin="Acanthis flammea", status="contested",
       resolved_by="Moved from Gould's genus Aegiothus into Acanthis, with the species epithet standardised to flammea.",
       note="Redpoll taxonomy has gone back and forth repeatedly: Mealy and Lesser Redpolls were long treated as separate species, then as one, then split again. A large 2021 genomic study found essentially no genetic separation between them despite their plumage differences and recommended treating all redpolls as a single species -- a conclusion not every authority has yet adopted, so this is flagged as contested rather than settled."),

  dict(plate_page=212, text_page=213, english="Lesser Redpole", latin="Aegiothus rufescens", author="",
       modern_en="Lesser Redpoll", modern_latin="Acanthis cabaret", status="contested",
       resolved_by="Moved from Aegiothus into Acanthis, with the species epithet changed to cabaret.",
       note="See the Mealy Redpoll entry above: recent genomic evidence questions whether this is truly distinct from that species, though the two remain widely treated as separate for now."),

  dict(plate_page=216, text_page=217, english="Starling", latin="Sturnus vulgaris", author="Linn.",
       modern_en="Common Starling", modern_latin="Sturnus vulgaris", status="stable"),

  dict(plate_page=219, text_page=None, shares_with=216, plate_note="young",
       english="Starling", latin="Sturnus vulgaris", author="Linn.",
       modern_en="Common Starling", modern_latin="Sturnus vulgaris", status="stable",
       resolved_by="Same species as plate 216; this plate shows two young birds at the nest and shares that plate's text."),

  dict(plate_page=222, text_page=223, english="Rose-coloured Pastor", latin="Pastor roseus", author="",
       modern_en="Rosy Starling", modern_latin="Pastor roseus", status="stable",
       note="The binomial is unchanged; the modern English name 'Rosy Starling' has mostly replaced Gould's 'Rose-coloured Pastor', though 'Rose-coloured Starling' is also still used."),

  dict(plate_page=225, text_page=None, shares_with=222, plate_note="young",
       english="Rose-coloured Pastor", latin="Pastor roseus", author="",
       modern_en="Rosy Starling", modern_latin="Pastor roseus", status="stable",
       resolved_by="Same species as plate 222; this plate shows a young bird and shares that plate's text."),

  dict(plate_page=228, text_page=229, english="Raven", latin="Corvus corax", author="Linn.",
       modern_en="Common Raven", modern_latin="Corvus corax", status="stable"),

  dict(plate_page=232, text_page=233, english="Carrion-Crow", latin="Corvus corone", author="Linn.",
       modern_en="Carrion Crow", modern_latin="Corvus corone", status="stable"),

  dict(plate_page=236, text_page=237, english="Hooded Crow", latin="Corvus cornix", author="Linn.",
       modern_en="Hooded Crow", modern_latin="Corvus cornix", status="stable",
       note="Treated as a full species by Gould, then widely lumped with the Carrion Crow as one variable species for much of the 20th century, and subsequently split back out to full species status by most modern authorities on the strength of genetic and behavioural evidence -- so the current consensus has essentially returned to Gould's original treatment."),

  dict(plate_page=240, text_page=241, english="Rook", latin="Corvus frugilegus", author="Linn.",
       modern_en="Rook", modern_latin="Corvus frugilegus", status="stable"),

  dict(plate_page=244, text_page=245, english="Jackdaw", latin="Corvus monedula", author="Linn.",
       modern_en="Western Jackdaw", modern_latin="Corvus monedula", status="stable"),

  dict(plate_page=248, text_page=249, english="Chough", latin="Fregilus graculus", author="",
       modern_en="Red-billed Chough", modern_latin="Pyrrhocorax pyrrhocorax", status="reclassified",
       resolved_by="Moved from Gould's genus Fregilus into Pyrrhocorax, with the species epithet standardised to match the genus."),

  dict(plate_page=252, text_page=253, english="Magpie", latin="Pica caudata", author="",
       modern_en="Eurasian Magpie", modern_latin="Pica pica", status="stable",
       note="Only the species epithet was standardised, caudata to pica, matching the genus."),

  dict(plate_page=256, text_page=257, english="Jay", latin="Garrulus glandarius", author="",
       modern_en="Eurasian Jay", modern_latin="Garrulus glandarius", status="stable"),

  dict(plate_page=260, text_page=261, english="Nutcracker", latin="Nucifraga caryocatactes", author="",
       modern_en="Spotted Nutcracker", modern_latin="Nucifraga caryocatactes", status="stable"),

  dict(plate_page=263, text_page=None, shares_with=260, plate_note="young",
       english="Nutcracker", latin="Nucifraga caryocatactes", author="",
       modern_en="Spotted Nutcracker", modern_latin="Nucifraga caryocatactes", status="stable",
       resolved_by="Same species as plate 260; this plate shows a young bird and shares that plate's text."),

  dict(plate_page=266, text_page=267, english="Cuckoo", latin="Cuculus canorus", author="Linn.",
       modern_en="Common Cuckoo", modern_latin="Cuculus canorus", status="stable"),

  dict(plate_page=269, text_page=None, shares_with=266, plate_note="young, ejecting its nestling companions",
       english="Cuckoo", latin="Cuculus canorus", author="Linn.",
       modern_en="Common Cuckoo", modern_latin="Cuculus canorus", status="stable",
       resolved_by="Same species as plate 266; this plate illustrates the young cuckoo's famous nest-eviction behaviour and shares that plate's text -- Gould's own caption cross-references his introductory essay on the species."),

  dict(plate_page=274, text_page=275, english="Great Spotted Cuckoo", latin="Oxylophus glandarius", author="",
       modern_en="Great Spotted Cuckoo", modern_latin="Clamator glandarius", status="reclassified",
       resolved_by="Moved from Gould's genus Oxylophus into Clamator, the currently recognised genus for the crested cuckoos."),

  dict(plate_page=278, text_page=279, english="Great Spotted Woodpecker", latin="Picus major", author="Linn.",
       modern_en="Great Spotted Woodpecker", modern_latin="Dendrocopos major", status="reclassified",
       resolved_by="Moved from Picus into Dendrocopos, the genus for the black-and-white spotted woodpeckers."),

  dict(plate_page=282, text_page=283, english="White-backed Woodpecker", latin="Picus leuconotus", author="Bechst.",
       modern_en="White-backed Woodpecker", modern_latin="Dendrocopos leucotos", status="reclassified",
       resolved_by="Moved into Dendrocopos alongside the Great Spotted Woodpecker, with the species epithet's spelling standardised to leucotos."),

  dict(plate_page=286, text_page=287, english="Lesser Spotted Woodpecker", latin="Picus minor", author="Linn.",
       modern_en="Lesser Spotted Woodpecker", modern_latin="Dryobates minor", status="reclassified",
       resolved_by="Split out from Dendrocopos into its own genus, Dryobates, based on DNA phylogenetics -- a further split than its larger spotted relatives above underwent."),

  dict(plate_page=290, text_page=291, english="Great Black Woodpecker", latin="Dryocopus martius", author="",
       modern_en="Black Woodpecker", modern_latin="Dryocopus martius", status="stable"),

  dict(plate_page=294, text_page=295, english="Green Woodpecker, or Yaffle", latin="Gecinus viridis", author="",
       modern_en="European Green Woodpecker", modern_latin="Picus viridis", status="reclassified",
       resolved_by="Moved from Gould's genus Gecinus into Picus.",
       note="A neat cross-reference to the Great Spotted Woodpecker several plates above: Gould used the genus Picus for that spotted woodpecker (now Dendrocopos), while this Green Woodpecker used a different genus, Gecinus -- but modern taxonomy reassigned Picus to the green woodpeckers instead, so the genus name Gould gave to one bird now belongs to a different one entirely."),

  dict(plate_page=297, text_page=None, shares_with=294, plate_note="young",
       english="Green Woodpecker, or Yaffle", latin="Gecinus viridis", author="",
       modern_en="European Green Woodpecker", modern_latin="Picus viridis", status="reclassified",
       resolved_by="Same species as plate 294; this plate shows a young bird and shares that plate's text."),

  dict(plate_page=300, text_page=301, english="Wryneck", latin="Yunx torquilla", author="",
       modern_en="Eurasian Wryneck", modern_latin="Jynx torquilla", status="stable",
       note="Only the spelling of the genus was standardised, Yunx to Jynx. The Wryneck is the final species of Volume III, closing out the woodpecker family (Picidae) before Volume IV presumably continues into the next order."),
]

assert len(SPECIES_GB_V3) == 76
