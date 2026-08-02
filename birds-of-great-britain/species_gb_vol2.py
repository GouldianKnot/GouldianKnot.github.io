# Birds of Great Britain (Gould, 1862-73), Volume II.
# Reconnaissance + OCR + heading-extraction pass completed 2026-08-01. Source:
# birdsgreatbrita2goul.pdf (Internet Archive scan, 324 pages). 78 plates identified
# by a centre-cropped colourfulness heuristic, covering 76 distinct species/forms.
#
# Fields: same schema as species_gb_vol1.py -- see that file's header for the full
# field-by-field explanation. Short version: plate_page/text_page are PDF page
# numbers; shares_with points at the plate_page whose text_page also covers this
# entry (two plates, one combined account); modern_en/modern_latin/status/note
# record how Gould's 1873 name maps onto current usage.
#
# IMPORTANT SOURCING NOTE: "latin"/"author" below are always taken from the
# actual printed heading line (the bold caps genus+species at the top of the
# text page, plus whatever authority is printed directly on that same line) --
# NOT from the older synonyms listed further down the synonymy block. Several
# of Gould's headings already use a genus that reads as strikingly "modern"
# (e.g. Poecile, Troglodytes, Luscinia, Acrocephalus) while the synonymy line
# beneath cites an even older Linnaean placement; where that happens it is
# called out explicitly, since it is one of the more interesting findings of
# this pass.
#
# ONE NOTEWORTHY SCAN QUIRK in this volume (flagged honestly rather than
# glossed over):
#   1. Plate 121 (MECISTURA CAUDATA, "Young") has a blank would-be text page
#      (122) -- confirmed by viewing the plate's own printed caption, it shares
#      its account with plate 118 (the adult Long-tailed Tit, text page 119).
#      Same pattern as plate 39/40 below and as several Volume I entries.
#   2. Plate 152 (MERULA VULGARIS, the Blackbird), text page 153: this pass's
#      automated page-by-page render/OCR judged the heading/synonymy block
#      missing -- every neighbouring page was individually rendered and
#      inspected at high resolution and still came up empty above the visible
#      "without such manifestations..." paragraph. Jan went back to the actual
#      source PDF directly and found the heading was there after all, just
#      rendering too faintly for this pass's OCR/render pipeline to pick up,
#      and transcribed it by hand. So this was a pipeline miss, not a missing
#      or misbound leaf as first suspected -- corrected below with the
#      heading Jan supplied.
#
# NOT YET DONE: German/French names, Gould's running prose beyond what informed
# the modern-name research, thumbnail+hires image linkage (pending), Volumes
# III-V.

SPECIES_GB_V2 = [
  dict(plate_page=12, text_page=13, english="Nightjar, or Goatsucker", latin="Caprimulgus europaeus", author="Linn.",
       modern_en="European Nightjar", modern_latin="Caprimulgus europaeus", status="stable"),

  dict(plate_page=16, text_page=17, english="Red-necked Goatsucker", latin="Caprimulgus ruficollis", author="Temm.",
       modern_en="Red-necked Nightjar", modern_latin="Caprimulgus ruficollis", status="stable"),

  dict(plate_page=20, text_page=21, english="Swift", latin="Cypselus apus", author="",
       modern_en="Common Swift", modern_latin="Apus apus", status="reclassified",
       resolved_by="The old genus Cypselus was absorbed into Apus, the currently recognised swift genus."),

  dict(plate_page=24, text_page=25, english="Alpine Swift", latin="Cypselus melba", author="",
       modern_en="Alpine Swift", modern_latin="Tachymarptis melba", status="reclassified",
       resolved_by="Split out of Cypselus/Apus into its own genus Tachymarptis on the basis of size and structure, later confirmed by DNA phylogenetics."),

  dict(plate_page=28, text_page=29, english="Swallow", latin="Hirundo rustica", author="Linn.",
       modern_en="Barn Swallow", modern_latin="Hirundo rustica", status="stable"),

  dict(plate_page=32, text_page=33, english="House-Martin", latin="Chelidon urbica", author="",
       modern_en="Common House Martin", modern_latin="Delichon urbicum", status="reclassified",
       resolved_by="Moved from Chelidon into Delichon, with the species epithet's gender corrected to match (urbica to urbicum)."),

  dict(plate_page=36, text_page=37, english="Sand-Martin", latin="Cotyle riparia", author="",
       modern_en="Sand Martin", modern_latin="Riparia riparia", status="reclassified",
       resolved_by="Moved from Cotyle into Riparia, the currently recognised genus."),

  dict(plate_page=39, text_page=None, shares_with=36, plate_note="in a sand-bank, showing nesting burrows",
       english="Sand-Martin", latin="Cotyle riparia", author="",
       modern_en="Sand Martin", modern_latin="Riparia riparia", status="reclassified",
       resolved_by="Same species as plate 36; this plate shows the birds at their nesting burrows and shares that plate's text.",
       note="Text page 40 is genuinely blank -- confirmed by viewing the plate itself (rotated caption reads COTYLE RIPARIA), matching Gould's practice elsewhere of giving one combined account to two related plates."),

  dict(plate_page=42, text_page=43, english="Bee-eater", latin="Merops apiaster", author="Linn.",
       modern_en="European Bee-eater", modern_latin="Merops apiaster", status="stable"),

  dict(plate_page=46, text_page=47, english="Kingfisher", latin="Alcedo ispida", author="Linn.",
       modern_en="Common Kingfisher", modern_latin="Alcedo atthis", status="reclassified",
       resolved_by="The species epithet was standardised from ispida to atthis (Linnaeus's own alternative name, later given priority)."),

  dict(plate_page=50, text_page=51, english="Roller", latin="Coracias garrula", author="Linn.",
       modern_en="European Roller", modern_latin="Coracias garrulus", status="stable",
       note="Only the ending of the species epithet was corrected for grammatical gender, garrula to garrulus."),

  dict(plate_page=54, text_page=55, english="Hoopoe", latin="Upupa epops", author="Linn.",
       modern_en="Eurasian Hoopoe", modern_latin="Upupa epops", status="stable"),

  dict(plate_page=58, text_page=59, english="Great Grey Shrike", latin="Lanius excubitor", author="Linn.",
       modern_en="Great Grey Shrike", modern_latin="Lanius excubitor", status="stable",
       note="The heading's genus/species line was lost to OCR (only the English name and synonymy survived clearly); the binomial is taken from the first synonym listed, Lanius excubitor, Linn., which is also Gould's usual heading form."),

  dict(plate_page=62, text_page=63, english="Rose-breasted Shrike", latin="Lanius minor", author="Gmel.",
       modern_en="Lesser Grey Shrike", modern_latin="Lanius minor", status="stable",
       note="Only the English name has shifted, from Gould's 'Rose-breasted Shrike' to the modern 'Lesser Grey Shrike'; the binomial is unchanged."),

  dict(plate_page=66, text_page=67, english="Butcher Bird", latin="Enneoctonus collurio", author="",
       modern_en="Red-backed Shrike", modern_latin="Lanius collurio", status="reclassified",
       resolved_by="The genus Enneoctonus was absorbed back into Lanius; the modern English name is 'Red-backed Shrike' rather than the old folk name 'Butcher Bird'."),

  dict(plate_page=70, text_page=71, english="Woodchat", latin="Enneoctonus rufus", author="",
       modern_en="Woodchat Shrike", modern_latin="Lanius senator", status="reclassified",
       resolved_by="Moved from Enneoctonus into Lanius, and the species epithet was standardised to senator."),

  dict(plate_page=74, text_page=75, english="Pied Flycatcher", latin="Muscicapa atricapilla", author="Linn.",
       modern_en="European Pied Flycatcher", modern_latin="Ficedula hypoleuca", status="reclassified",
       resolved_by="Moved out of Muscicapa into Ficedula (the genus for Old World flycatchers with distinct plumage patterns), with the species epithet standardised to hypoleuca."),

  dict(plate_page=78, text_page=79, english="White-collared Flycatcher", latin="Muscicapa collaris", author="Bechst.",
       modern_en="Collared Flycatcher", modern_latin="Ficedula albicollis", status="reclassified",
       resolved_by="Moved into Ficedula alongside the Pied Flycatcher, with the species epithet standardised to albicollis."),

  dict(plate_page=82, text_page=83, english="Spotted Flycatcher", latin="Butalis grisola", author="",
       modern_en="Spotted Flycatcher", modern_latin="Muscicapa striata", status="reclassified",
       resolved_by="Moved from Gould's genus Butalis back into Muscicapa, with the species epithet standardised from grisola to striata."),

  dict(plate_page=86, text_page=87, english="Red-breasted Flycatcher", latin="Erythrosterna parva", author="",
       modern_en="Red-breasted Flycatcher", modern_latin="Ficedula parva", status="reclassified",
       resolved_by="Moved from Gould's genus Erythrosterna into Ficedula, along with the other spotted-breasted flycatchers of this account."),

  dict(plate_page=90, text_page=91, english="Waxen Chatterer", latin="Ampelis garrulus", author="",
       modern_en="Bohemian Waxwing", modern_latin="Bombycilla garrulus", status="reclassified",
       resolved_by="Moved from Ampelis into Bombycilla, the currently recognised waxwing genus; the modern English name is 'Bohemian Waxwing' rather than the old 'Waxen Chatterer'."),

  dict(plate_page=94, text_page=95, english="Nuthatch", latin="Sitta cesia", author="Wolf et Meyer",
       modern_en="Eurasian Nuthatch", modern_latin="Sitta europaea", status="reclassified",
       resolved_by="The species epithet cesia (caesia) is now treated as a synonym/subspecies name; the accepted binomial is Sitta europaea."),

  dict(plate_page=98, text_page=99, english="Great Tit", latin="Parus major", author="Linn.",
       modern_en="Great Tit", modern_latin="Parus major", status="stable"),

  dict(plate_page=102, text_page=103, english="Blue Tit", latin="Parus caeruleus", author="",
       modern_en="Eurasian Blue Tit", modern_latin="Cyanistes caeruleus", status="reclassified",
       resolved_by="Split out of Parus into Cyanistes along with the other 'blue tit' relatives, based on DNA phylogenetics."),

  dict(plate_page=106, text_page=107, english="Coal Tit", latin="Parus ater", author="Linn.",
       modern_en="Coal Tit", modern_latin="Periparus ater", status="reclassified",
       resolved_by="Split out of Parus into Periparus, based on DNA phylogenetics."),

  dict(plate_page=110, text_page=111, english="Crested Tit", latin="Parus cristatus", author="Linn.",
       modern_en="European Crested Tit", modern_latin="Lophophanes cristatus", status="reclassified",
       resolved_by="Split out of Parus into Lophophanes, based on DNA phylogenetics."),

  dict(plate_page=114, text_page=115, english="Marsh-Tit", latin="Poecile palustris", author="",
       modern_en="Marsh Tit", modern_latin="Poecile palustris", status="stable",
       note="Gould's own heading already reads 'PŒCILE PALUSTRIS' -- modern taxonomy uses exactly this genus and spelling today. Only the synonymy line beneath it, 'Parus palustris, Linn.', reflects the older placement; Poecile was revived for the 'brown/grey' tits by 21st-century DNA work, so Gould's heading choice, whether by chance or by following an existing alternative usage, anticipated it by more than a century."),

  dict(plate_page=118, text_page=119, english="Long-tailed Tit", latin="Mecistura caudata", author="",
       modern_en="Long-tailed Tit", modern_latin="Aegithalos caudatus", status="reclassified",
       resolved_by="Moved from Gould's genus Mecistura into Aegithalos, its own family (Aegithalidae) distinct from the true tits; the synonymy line's older placement, Parus caudatus, Linn., had already been superseded by Gould's own day."),

  dict(plate_page=121, text_page=None, shares_with=118, plate_note="young",
       english="Long-tailed Tit", latin="Mecistura caudata", author="",
       modern_en="Long-tailed Tit", modern_latin="Aegithalos caudatus", status="reclassified",
       resolved_by="Same species as plate 118; this plate shows a family party of young birds and shares that plate's text.",
       note="Text page 122 is genuinely blank -- confirmed by viewing the plate itself, captioned 'MECISTURA CAUDATA. Young'."),

  dict(plate_page=124, text_page=125, english="Bearded Tit", latin="Calamophilus biarmicus", author="",
       modern_en="Bearded Reedling", modern_latin="Panurus biarmicus", status="reclassified",
       resolved_by="Moved from Gould's genus Calamophilus into Panurus, its own monotypic family (Panuridae); no longer considered a true tit at all, hence the modern English name 'Bearded Reedling' rather than 'Bearded Tit'."),

  dict(plate_page=128, text_page=129, english="Golden Oriole", latin="Oriolus galbula", author="Linn.",
       modern_en="Eurasian Golden Oriole", modern_latin="Oriolus oriolus", status="reclassified",
       resolved_by="The species epithet was standardised from galbula to oriolus."),

  dict(plate_page=132, text_page=133, english="Thrush", latin="Turdus musicus", author="Linn.",
       modern_en="Song Thrush", modern_latin="Turdus philomelos", status="reclassified",
       resolved_by="The name Turdus musicus was dropped for this species (the epithet had also been mis-applied to the Redwing by other authors, causing real confusion); the accepted binomial is now Turdus philomelos."),

  dict(plate_page=136, text_page=137, english="Missel-Thrush", latin="Turdus viscivorus", author="Linn.",
       modern_en="Mistle Thrush", modern_latin="Turdus viscivorus", status="stable"),

  dict(plate_page=140, text_page=141, english="Redwing", latin="Turdus iliacus", author="Linn.",
       modern_en="Redwing", modern_latin="Turdus iliacus", status="stable"),

  dict(plate_page=144, text_page=145, english="Fieldfare", latin="Turdus pilaris", author="Linn.",
       modern_en="Fieldfare", modern_latin="Turdus pilaris", status="stable"),

  dict(plate_page=148, text_page=149, english="Black-throated Thrush", latin="Turdus atrogularis", author="Temm.",
       modern_en="Black-throated Thrush", modern_latin="Turdus atrogularis", status="stable"),

  dict(plate_page=152, text_page=153, english="Blackbird", latin="Merula vulgaris", author="Ray",
       modern_en="Common Blackbird", modern_latin="Turdus merula", status="reclassified",
       resolved_by="Moved from Merula back into Turdus, and the species epithet standardised to merula.",
       note="The heading/synonymy block that this pass's page-by-page render had judged missing was in fact present on the page -- Jan located and transcribed it directly from the source PDF (it had rendered too faintly for the earlier OCR pass to pick up). It reads 'MERULA VULGARIS, / Blackbird. / Merula vulgaris, Ray.' followed by the usual synonymy list (Turdus merula, Linn.; Merula merula, Boie; and several Brehm-era subspecies names). Correcting the volume-level note above accordingly."),

  dict(plate_page=156, text_page=157, english="Ring-Ousel", latin="Merula torquata", author="",
       modern_en="Ring Ouzel", modern_latin="Turdus torquatus", status="reclassified",
       resolved_by="Gould's own heading uses the genus Merula (Merula torquata); modern taxonomy reverted to the original Linnaean placement, Turdus torquatus -- which the synonymy line on this same page already lists as the older alternative, 'Turdus torquatus, Linn.', and that turned out to be the name that stuck."),

  dict(plate_page=160, text_page=161, english="White's Thrush", latin="Oreocincla aurea", author="",
       modern_en="White's Thrush", modern_latin="Zoothera dauma", status="reclassified",
       resolved_by="Moved from Gould's genus Oreocincla into Zoothera, the genus for large ground-thrushes with scalloped plumage, and the species epithet standardised to dauma (an older available name given priority)."),

  dict(plate_page=164, text_page=165, english="Siberian Thrush", latin="Cichloselys sibiricus", author="",
       modern_en="Siberian Thrush", modern_latin="Geokichla sibirica", status="reclassified",
       resolved_by="Moved from Gould's genus Cichloselys into Geokichla, based on DNA phylogenetics."),

  dict(plate_page=168, text_page=169, english="Water-Ouzel or Dipper", latin="Cinclus aquaticus", author="",
       modern_en="White-throated Dipper", modern_latin="Cinclus cinclus", status="reclassified",
       resolved_by="The species epithet was standardised from aquaticus to cinclus."),

  dict(plate_page=172, text_page=173, english="Black-bellied Water-Ouzel", latin="Cinclus melanogaster", author="Temm.",
       modern_en="Black-bellied Dipper", modern_latin="Cinclus cinclus", status="lumped",
       resolved_by="No longer treated as a distinct species; it is now considered a Scandinavian/continental subspecies of the White-throated Dipper, Cinclus cinclus melanogaster."),

  dict(plate_page=176, text_page=177, english="Blue Rock-Thrush", latin="Petrocossyphus cyanus", author="",
       modern_en="Blue Rock Thrush", modern_latin="Monticola solitarius", status="reclassified",
       resolved_by="Moved from Petrocossyphus into Monticola, and the species epithet standardised to solitarius."),

  dict(plate_page=180, text_page=181, english="Rock-Thrush", latin="Petrocincla saxatilis", author="",
       modern_en="Common Rock Thrush", modern_latin="Monticola saxatilis", status="reclassified",
       resolved_by="Moved from Petrocincla into Monticola alongside the Blue Rock Thrush."),

  dict(plate_page=184, text_page=185, english="Wheatear", latin="Saxicola oenanthe", author="",
       modern_en="Northern Wheatear", modern_latin="Oenanthe oenanthe", status="reclassified",
       resolved_by="Split out of Saxicola into its own genus Oenanthe (the wheatears), separate from the chats."),

  dict(plate_page=188, text_page=189, english="Whinchat", latin="Pratincola rubetra", author="",
       modern_en="Whinchat", modern_latin="Saxicola rubetra", status="reclassified",
       resolved_by="Moved from Pratincola into Saxicola, the currently recognised chat genus."),

  dict(plate_page=192, text_page=193, english="Stone-chat or Furze-chat", latin="Pratincola rubicola", author="",
       modern_en="European Stonechat", modern_latin="Saxicola rubicola", status="reclassified",
       resolved_by="Moved from Pratincola into Saxicola; the European Stonechat was also later split from the Siberian and African Stonechats, which now form separate species."),

  dict(plate_page=196, text_page=197, english="Robin, or Redbreast", latin="Erythacus rubecula", author="",
       modern_en="European Robin", modern_latin="Erithacus rubecula", status="stable",
       note="Only the spelling of the genus name has since been standardised, Erythacus to Erithacus; Gould's heading had already moved the bird into the right genus, well past the outdated Linnaean 'Motacilla rubecula' still cited in his own synonymy line."),

  dict(plate_page=200, text_page=201, english="Red-throated Bluebreast", latin="Cyanecula suecica", author="",
       modern_en="Bluethroat", modern_latin="Luscinia svecica", status="reclassified",
       resolved_by="Moved from Gould's genus Cyanecula into Luscinia, with the species epithet's spelling standardised to svecica; the red-spotted form Gould illustrates is now treated as a subspecies, Luscinia svecica svecica."),

  dict(plate_page=204, text_page=205, english="White-throated Bluebreast", latin="Cyanecula leucocyana", author="Brehm",
       modern_en="Bluethroat", modern_latin="Luscinia svecica", status="lumped",
       resolved_by="No longer treated as a separate species from the Red-throated Bluebreast; the white-spotted form is now considered the subspecies Luscinia svecica cyanecula of a single Bluethroat species."),

  dict(plate_page=208, text_page=209, english="Redstart", latin="Ruticilla phoenicura", author="",
       modern_en="Common Redstart", modern_latin="Phoenicurus phoenicurus", status="reclassified",
       resolved_by="Moved from Ruticilla into Phoenicurus, the currently recognised redstart genus."),

  dict(plate_page=212, text_page=213, english="Black Redstart", latin="Ruticilla tithys", author="",
       modern_en="Black Redstart", modern_latin="Phoenicurus ochruros", status="reclassified",
       resolved_by="Moved from Ruticilla (Gould's genus, matching the Common Redstart above) into Phoenicurus, with the species epithet standardised to ochruros."),

  dict(plate_page=216, text_page=217, english="Rufous Sedge-Warbler", latin="Aedon galactodes", author="",
       modern_en="Rufous-tailed Scrub Robin", modern_latin="Cercotrichas galactotes", status="reclassified",
       resolved_by="Moved from Aedon into Cercotrichas, and the species epithet's spelling standardised to galactotes; the modern English name 'Rufous-tailed Scrub Robin' has replaced Gould's 'Rufous Sedge-Warbler', which mis-suggested a relationship to the true sedge-warblers."),

  dict(plate_page=220, text_page=221, english="Alpine Accentor", latin="Accentor alpinus", author="",
       modern_en="Alpine Accentor", modern_latin="Prunella collaris", status="reclassified",
       resolved_by="Moved from Accentor into Prunella, the currently recognised accentor genus, with the species epithet standardised to collaris."),

  dict(plate_page=224, text_page=225, english="Hedge-Accentor, or Hedgesparrow", latin="Accentor modularis", author="",
       modern_en="Dunnock", modern_latin="Prunella modularis", status="reclassified",
       resolved_by="Moved from Accentor (Gould's genus, matching the Alpine Accentor above) into Prunella; the modern English name 'Dunnock' has replaced the misleading old folk name 'Hedgesparrow' (it is not a sparrow)."),

  dict(plate_page=228, text_page=229, english="Nightingale", latin="Luscinia philomela", author="",
       modern_en="Common Nightingale", modern_latin="Luscinia megarhynchos", status="reclassified",
       resolved_by="Gould's own heading already places this bird in the modern genus, Luscinia -- but under the epithet philomela, which today denotes a different, closely related species (the Thrush Nightingale, a scarce vagrant to Britain). The bird breeding in England that Gould describes here is the Common Nightingale, whose accepted binomial is Luscinia megarhynchos.",
       note="A genuine false-friend case: 'philomela' in Gould's heading and 'Luscinia luscinia' in modern taxonomy sound like they should match but refer to different species; the Latin epithets do not track cleanly across the two systems."),

  dict(plate_page=232, text_page=233, english="Whitethroat", latin="Sylvia cinerea", author="",
       modern_en="Common Whitethroat", modern_latin="Curruca communis", status="reclassified",
       resolved_by="A large recent revision (2020s) of the Old World warblers split most Sylvia species into a restored genus Curruca; the Whitethroat's accepted binomial is now Curruca communis. Gould's own heading already uses Sylvia (Sylvia cinerea); the older Linnaean synonym, Motacilla sylvia, printed in his synonymy line, reflects a placement that was outdated even in his own day."),

  dict(plate_page=236, text_page=237, english="Lesser Whitethroat", latin="Sylvia curruca", author="",
       modern_en="Lesser Whitethroat", modern_latin="Curruca curruca", status="reclassified",
       resolved_by="Moved from Sylvia (Gould's genus) into the restored genus Curruca along with the Common Whitethroat; strikingly, the species epithet curruca is unchanged, so Gould's own heading already contained the modern binomial's second half."),

  dict(plate_page=240, text_page=241, english="Dartford Warbler", latin="Melizophilus provincialis", author="",
       modern_en="Dartford Warbler", modern_latin="Curruca undata", status="reclassified",
       resolved_by="Moved from Melizophilus (and later Sylvia) into the restored genus Curruca, with the species epithet standardised to undata."),

  dict(plate_page=244, text_page=245, english="Blackcap", latin="Curruca atricapilla", author="",
       modern_en="Eurasian Blackcap", modern_latin="Sylvia atricapilla", status="reclassified",
       resolved_by="Gould's own heading already uses the genus Curruca -- exactly the genus recently revived for most of this volume's other Sylvia warblers. But the Blackcap itself was NOT moved into Curruca during that 2020s revision; it stayed in Sylvia (Sylvia atricapilla), so for this one species Gould's own choice of genus turned out not to match modern usage, even though it anticipated the general direction taken for its relatives.",
       note="A neat mirror-image of the Whitethroat and Lesser Whitethroat entries above, where Gould used the OLDER genus and modern taxonomy moved TO Curruca: here Gould already used Curruca, and modern taxonomy stayed in Sylvia."),

  dict(plate_page=248, text_page=249, english="Orphean Warbler", latin="Curruca orphea", author="",
       modern_en="Western Orphean Warbler", modern_latin="Curruca hortensis", status="contested",
       resolved_by="Gould's own heading already uses the modern genus, Curruca -- only the species epithet has since changed. The Orphean Warbler complex was later split into Western (Curruca hortensis) and Eastern (Curruca crassirostris) species; Gould's British-context record most likely refers to the western form.",
       note="Confusingly, the modern binomial for this species, Curruca hortensis, reuses the exact Latin epithet Gould gave to the Garden-Warbler (Curruca hortensis, per Gould's own heading) below -- the two are unrelated species; see that entry's note."),

  dict(plate_page=252, text_page=253, english="Garden-Warbler", latin="Curruca hortensis", author="",
       modern_en="Garden Warbler", modern_latin="Sylvia borin", status="reclassified",
       resolved_by="Gould's own heading places this bird in Curruca (Curruca hortensis) -- but the Garden Warbler stayed in Sylvia during the 2020s genus revision, becoming Sylvia borin; the species epithet also changed entirely, from hortensis to borin.",
       note="A false-friend case worth flagging: the epithet 'hortensis' that Gould gave this bird is now the modern binomial's second half for a completely different species, the Orphean Warbler (see the entry above) -- while this bird, the actual Garden Warbler, now carries the unrelated epithet 'borin'. Anyone matching by Latin epithet alone would connect the wrong two birds."),

  dict(plate_page=256, text_page=257, english="Common Wren", latin="Troglodytes europaeus", author="",
       modern_en="Eurasian Wren", modern_latin="Troglodytes troglodytes", status="reclassified",
       resolved_by="Gould's own heading already prints the modern genus, 'TROGLODYTES EUROPAUS'; the synonymy's older 'Passer troglodytes, Will.' reflects an even earlier, pre-Linnaean-tradition placement (John Willughby's 17th-century Ornithology). The accepted binomial today is Troglodytes troglodytes -- only the species epithet has changed."),

  dict(plate_page=260, text_page=261, english="Tree-Creeper", latin="Certhia familiaris", author="Linn.",
       modern_en="Eurasian Treecreeper", modern_latin="Certhia familiaris", status="stable",
       note="A second, very similar species (Short-toed Treecreeper, Certhia brachydactyla) was only later confirmed as a separate British-region bird; Gould's single 'Tree-Creeper' account corresponds to what is now specifically the Eurasian Treecreeper."),

  dict(plate_page=264, text_page=265, english="Willow-Wren", latin="Phyllopneuste trochilus", author="",
       modern_en="Willow Warbler", modern_latin="Phylloscopus trochilus", status="reclassified",
       resolved_by="Moved from Gould's genus Phyllopneuste into Phylloscopus, the currently recognised leaf-warbler genus."),

  dict(plate_page=268, text_page=269, english="Chiff-chaff", latin="Phyllopneuste rufa", author="",
       modern_en="Common Chiffchaff", modern_latin="Phylloscopus collybita", status="reclassified",
       resolved_by="Moved from Phyllopneuste (Gould's genus, matching the Willow Warbler above) into Phylloscopus, with the species epithet standardised to collybita."),

  dict(plate_page=272, text_page=273, english="Wood-Wren", latin="Phyllopneuste sibilatrix", author="",
       modern_en="Wood Warbler", modern_latin="Phylloscopus sibilatrix", status="reclassified",
       resolved_by="Moved from Phyllopneuste into Phylloscopus alongside its two relatives above; the species epithet, sibilatrix, is unchanged."),

  dict(plate_page=276, text_page=277, english="Yellow-browed Warbler", latin="Reguloides superciliosus", author="",
       modern_en="Yellow-browed Warbler", modern_latin="Phylloscopus inornatus", status="reclassified",
       resolved_by="Moved from Gould's genus Reguloides into Phylloscopus, with the species epithet standardised to inornatus."),

  dict(plate_page=280, text_page=281, english="Golden-crested Wren, or Kinglet", latin="Regulus cristatus", author="Ray",
       modern_en="Goldcrest", modern_latin="Regulus regulus", status="reclassified",
       resolved_by="The species epithet was standardised from cristatus to regulus, matching the genus (Regulus regulus); the modern English name has settled on 'Goldcrest'."),

  dict(plate_page=284, text_page=285, english="Fire-crested Wren", latin="Regulus ignicapillus", author="",
       modern_en="Common Firecrest", modern_latin="Regulus ignicapilla", status="stable",
       note="Only the species epithet's ending was standardised for grammatical gender, ignicapillus to ignicapilla; the genus placement, Regulus alongside the Goldcrest, was already correct in Gould's own heading."),

  dict(plate_page=288, text_page=289, english="Melodious Warbler", latin="Ficedula hypolais", author="",
       modern_en="Melodious Warbler", modern_latin="Hippolais polyglotta", status="reclassified",
       resolved_by="Gould's own heading genus, Ficedula, is now reserved for the true (spotted) flycatchers elsewhere in this volume; the Melodious Warbler instead belongs in Hippolais, with the species epithet standardised to polyglotta."),

  dict(plate_page=292, text_page=293, english="Thrush Warbler", latin="Acrocephalus turdoides", author="",
       modern_en="Great Reed Warbler", modern_latin="Acrocephalus arundinaceus", status="reclassified",
       resolved_by="Gould's own heading already places this bird in Acrocephalus; only the species epithet has changed, from turdoides to arundinaceus. The modern English name 'Great Reed Warbler' has replaced Gould's 'Thrush Warbler'.",
       note="Both this species and the smaller Reed Warbler below were, in older 18th-century literature, called by the same synonym, Motacilla arundinacea (both synonymy lines on these two pages cite it) -- a real historical source of confusion, even though Gould's own two headings correctly distinguish them (Acrocephalus turdoides here, Calamoherpe arundinacea there)."),

  dict(plate_page=296, text_page=297, english="Reed Warbler", latin="Calamoherpe arundinacea", author="",
       modern_en="Eurasian Reed Warbler", modern_latin="Acrocephalus scirpaceus", status="reclassified",
       resolved_by="Moved from Gould's genus Calamoherpe into Acrocephalus, but the species epithet changed entirely, from arundinacea to scirpaceus.",
       note="See the Thrush Warbler / Great Reed Warbler entry above: both species were once cited under the same old synonym, Motacilla arundinacea, a genuine source of historical confusion between a much larger and a much smaller reed-warbler."),

  dict(plate_page=300, text_page=301, english="Marsh Warbler", latin="Calamoherpe palustris", author="",
       modern_en="Marsh Warbler", modern_latin="Acrocephalus palustris", status="reclassified",
       resolved_by="Moved from Calamoherpe into Acrocephalus, the currently recognised reed-warbler genus."),

  dict(plate_page=304, text_page=305, english="Sedge Warbler or Chat", latin="Calamodyta phragmitis", author="",
       modern_en="Sedge Warbler", modern_latin="Acrocephalus schoenobaenus", status="reclassified",
       resolved_by="Moved from Gould's genus Calamodyta into Acrocephalus, with the species epithet standardised to schoenobaenus."),

  dict(plate_page=308, text_page=309, english="Aquatic Warbler", latin="Calamodyta aquatica", author="",
       modern_en="Aquatic Warbler", modern_latin="Acrocephalus paludicola", status="reclassified",
       resolved_by="Moved from Calamodyta (Gould's genus, matching the Sedge Warbler above) into Acrocephalus, with the species epithet standardised to paludicola."),

  dict(plate_page=312, text_page=313, english="Savi's Warbler", latin="Lusciniopsis luscinioides", author="",
       modern_en="Savi's Warbler", modern_latin="Locustella luscinioides", status="reclassified",
       resolved_by="Moved from Gould's genus Lusciniopsis into Locustella, the currently recognised genus for this group of skulking warblers, alongside the Grasshopper Warbler below; the species epithet, luscinioides, is unchanged."),

  dict(plate_page=316, text_page=317, english="Grasshopper Warbler", latin="Locustella avicula", author="Ray",
       modern_en="Common Grasshopper Warbler", modern_latin="Locustella naevia", status="reclassified",
       resolved_by="Gould's own heading already places this bird correctly in Locustella; only the species epithet has changed, from Ray's old avicula to the currently accepted naevia (Boddaert)."),
]

assert len(SPECIES_GB_V2) == 78
