# Birds of Great Britain (Gould, 1862-73), Volume I.
# Reconnaissance + OCR pass completed 2026-07-31. Source: birdsgreatbrita1goul.pdf
# (Internet Archive scan, ~308 pages). 34 plates identified in this volume by a
# colourfulness heuristic (see build notes), covering 32 distinct species/forms.
#
# Fields:
#   plate_page   - PDF page number of the plate itself (1-indexed, matches the source PDF)
#   text_page    - PDF page number carrying this plate's written account, OR None if
#                  this plate shares its account with another plate (see shares_with)
#   shares_with  - plate_page of the entry whose text_page also covers this plate
#                  (Gould sometimes gave two or three plates - e.g. adult/young,
#                  light/dark race - a single combined text account; the intervening
#                  page(s) are then genuinely blank, not an OCR failure)
#   plate_note   - the qualifier printed under the plate title, if any (e.g. "light
#                  race, adult and young"), distinguishing multiple plates of one species
#   english      - Gould's English name as printed
#   latin        - Gould's binomial as printed on the plate/heading
#   author       - authority as printed after the binomial
#   modern_en / modern_latin - current accepted English/scientific name
#   status       - stable | reclassified | lumped | contested (same vocabulary as
#                  the Birds of Europe data files)
#   note / resolved_by - explanatory text for the card, honest and specific
#
# NOT YET DONE: German/French names, Gould's running prose (Gen. Char. / species
# text), thumbnail+hires image linkage into the gallery build, Volumes II-V.

SPECIES_GB_V1 = [
  dict(plate_page=162, text_page=163, english="Egyptian Vulture", latin="Neophron percnopterus", author="Sav.",
       modern_en="Egyptian Vulture", modern_latin="Neophron percnopterus", status="stable"),

  dict(plate_page=166, text_page=167, english="Golden Eagle", latin="Aquila chrysaetos", author="Briss.",
       modern_en="Golden Eagle", modern_latin="Aquila chrysaetos", status="stable"),

  dict(plate_page=170, text_page=171, english="Spotted Eagle", latin="Aquila naevia", author="Meyer.",
       modern_en="Greater Spotted Eagle", modern_latin="Clanga clanga", status="reclassified",
       resolved_by="Genus revision split the spotted eagles out of Aquila into Clanga, based on DNA phylogenetics."),

  dict(plate_page=174, text_page=175, english="Sea-Eagle", latin="Haliaetus albicilla", author="",
       modern_en="White-tailed Eagle", modern_latin="Haliaeetus albicilla", status="stable",
       note="Only the spelling of the genus was standardised, from Haliaetus to Haliaeetus; the English name has shifted from “Sea-Eagle” to “White-tailed Eagle.”"),

  dict(plate_page=178, text_page=179, english="Osprey", latin="Pandion haliaetus", author="",
       modern_en="Osprey", modern_latin="Pandion haliaetus", status="stable"),

  dict(plate_page=182, text_page=183, english="Common Buzzard", latin="Buteo vulgaris", author="Bechst.",
       modern_en="Common Buzzard", modern_latin="Buteo buteo", status="reclassified",
       resolved_by="The species epithet was standardised from vulgaris to buteo."),

  dict(plate_page=186, text_page=187, english="Rough-legged Buzzard", latin="Archibuteo lagopus", author="",
       modern_en="Rough-legged Buzzard", modern_latin="Buteo lagopus", status="reclassified",
       resolved_by="Gould placed this species in its own genus, Archibuteo; that genus was later folded back into Buteo."),

  dict(plate_page=190, text_page=191, english="Honey-Buzzard", latin="Pernis apivorus", author="",
       modern_en="Honey Buzzard", modern_latin="Pernis apivorus", status="stable"),

  dict(plate_page=194, text_page=195, english="Goshawk", latin="Astur palumbarius", author="",
       modern_en="Northern Goshawk", modern_latin="Accipiter gentilis", status="reclassified",
       resolved_by="Genus revision folded Astur into Accipiter for most of the 20th and early 21st centuries; some recent DNA-based classifications have proposed reviving Astur for this species, so the genus placement is not entirely settled."),

  dict(plate_page=198, text_page=199, english="Sparrow-hawk", latin="Accipiter nisus", author="",
       modern_en="Sparrowhawk", modern_latin="Accipiter nisus", status="stable"),

  dict(plate_page=205, text_page=None, shares_with=208, plate_note="",
       english="Iceland Falcon", latin="Falco islandus", author="",
       modern_en="Gyrfalcon", modern_latin="Falco rusticolus", status="lumped",
       note="This plate has no independent written account in the volume; Gould discusses it as a close ally within the Greenland Falcon (Falco candicans) account that follows. The Iceland Falcon, Greenland Falcon and Norwegian/Gyrfalcon are today all treated as colour morphs of one wide-ranging species, Falco rusticolus — which is exactly the “three very similar birds, one long combined discussion” structure Gould gave them here."),

  dict(plate_page=208, text_page=209, plate_note="light race, adult and young",
       english="Greenland Falcon", latin="Falco candicans", author="Gmel.",
       modern_en="Gyrfalcon", modern_latin="Falco rusticolus", status="reclassified",
       resolved_by="Now treated as a colour morph of the single, wide-ranging Gyrfalcon, Falco rusticolus, rather than a distinct species. This plate's account (pp. 209-210) also covers the Iceland Falcon plate (p. 205) and the dark-race plate (p. 215)."),

  dict(plate_page=215, text_page=None, shares_with=208, plate_note="dark race, young",
       english="Greenland Falcon", latin="Falco candicans", author="Gmel.",
       modern_en="Gyrfalcon", modern_latin="Falco rusticolus", status="reclassified",
       note="Second plate of the Greenland Falcon (dark race, young); shares its written account with the light-race plate at p. 208 (text on pp. 209-210)."),

  dict(plate_page=218, text_page=219, english="Norwegian or Gyrfalcon", latin="Falco gyrfalco", author="Linn.",
       modern_en="Gyrfalcon", modern_latin="Falco rusticolus", status="reclassified",
       resolved_by="Along with the Iceland and Greenland Falcons, this form is now treated as part of one variable species, Falco rusticolus; Gould's gyrfalco is a synonym rather than a separate taxon."),

  dict(plate_page=222, text_page=223, english="Peregrine Falcon", latin="Falco peregrinus", author="",
       modern_en="Peregrine Falcon", modern_latin="Falco peregrinus", status="stable"),

  dict(plate_page=226, text_page=227, english="Hobby", latin="Falco subbuteo", author="Linn.",
       modern_en="Hobby", modern_latin="Falco subbuteo", status="stable"),

  dict(plate_page=230, text_page=231, english="Merlin", latin="Falco aesalon", author="Gmel.",
       modern_en="Merlin", modern_latin="Falco columbarius", status="reclassified",
       resolved_by="The species epithet Gould used, aesalon, is now treated as a synonym (and sometimes a subspecies name) within Falco columbarius."),

  dict(plate_page=234, text_page=235, english="Orange-legged Hobby", latin="Erythropus vespertinus", author="",
       modern_en="Red-footed Falcon", modern_latin="Falco vespertinus", status="reclassified",
       resolved_by="Genus revision folded Erythropus back into Falco."),

  dict(plate_page=238, text_page=239, english="Kestrel", latin="Tinnunculus alaudarius", author="",
       modern_en="Common Kestrel", modern_latin="Falco tinnunculus", status="reclassified",
       resolved_by="Genus revision folded Tinnunculus back into Falco."),

  dict(plate_page=242, text_page=243, english="Kite or Glead", latin="Milvus regalis", author="",
       modern_en="Red Kite", modern_latin="Milvus milvus", status="reclassified",
       resolved_by="The species epithet Gould used, regalis, is now treated as a synonym; the accepted name is Milvus milvus."),

  dict(plate_page=246, text_page=247, english="Black Kite", latin="Milvus migrans", author="",
       modern_en="Black Kite", modern_latin="Milvus migrans", status="stable"),

  dict(plate_page=250, text_page=251, english="Marsh-Harrier", latin="Circus aeruginosus", author="",
       modern_en="Western Marsh Harrier", modern_latin="Circus aeruginosus", status="stable",
       note="Genus and species already match the modern name here; only the English common name has shifted, to “Western Marsh Harrier.”"),

  dict(plate_page=253, text_page=None, shares_with=250, plate_note="young",
       english="Marsh-Harrier", latin="Circus aeruginosus", author="",
       modern_en="Western Marsh Harrier", modern_latin="Circus aeruginosus", status="stable",
       note="Second plate of the Marsh Harrier (young, in the nest); shares its written account with the adult plate at p. 250 (text on p. 251)."),

  dict(plate_page=256, text_page=257, english="Hen Harrier", latin="Circus cyaneus", author="",
       modern_en="Hen Harrier", modern_latin="Circus cyaneus", status="stable"),

  dict(plate_page=260, text_page=261, english="Ash-coloured Harrier", latin="Circus cineraceus", author="",
       modern_en="Montagu's Harrier", modern_latin="Circus pygargus", status="reclassified",
       resolved_by="The species epithet Gould used, cineraceus, is now treated as a synonym; the accepted name is Circus pygargus."),

  dict(plate_page=264, text_page=265, english="Barn-Owl", latin="Strix flammea", author="Linn.",
       modern_en="Barn Owl", modern_latin="Tyto alba", status="reclassified",
       resolved_by="Genus revision separated the barn owls from the typical owls, moving this species from Strix to Tyto."),

  dict(plate_page=268, text_page=269, english="Tawny or Brown Owl", latin="Syrnium aluco", author="",
       modern_en="Tawny Owl", modern_latin="Strix aluco", status="reclassified",
       resolved_by="Genus revision moved this species from Syrnium back into Strix."),

  dict(plate_page=272, text_page=273, english="Eagle Owl", latin="Bubo maximus", author="Sib.",
       modern_en="Eagle-Owl", modern_latin="Bubo bubo", status="reclassified",
       resolved_by="The species epithet Gould used, maximus, is now treated as a synonym; the accepted name is Bubo bubo."),

  dict(plate_page=276, text_page=277, english="Long-eared Owl", latin="Otus vulgaris", author="",
       modern_en="Long-eared Owl", modern_latin="Asio otus", status="reclassified",
       resolved_by="Genus revision moved this species from Otus to Asio."),

  dict(plate_page=280, text_page=281, english="Short-eared Owl", latin="Brachyotus palustris", author="",
       modern_en="Short-eared Owl", modern_latin="Asio flammeus", status="reclassified",
       resolved_by="Genus revision moved this species from Brachyotus to Asio, alongside the Long-eared Owl."),

  dict(plate_page=284, text_page=285, english="Scops Eared Owl", latin="Scops zorca", author="",
       modern_en="Eurasian Scops Owl", modern_latin="Otus scops", status="reclassified",
       resolved_by="Genus revision moved this species from Scops to Otus; the species epithet Gould used, zorca, is now treated as a synonym."),

  dict(plate_page=288, text_page=289, english="Snowy Owl", latin="Nyctea nivea", author="",
       modern_en="Snowy Owl", modern_latin="Bubo scandiacus", status="reclassified",
       resolved_by="Genus revision has moved this species repeatedly — from Nyctea to its own genus, and more recently DNA evidence folded it into Bubo alongside the eagle-owls."),

  dict(plate_page=292, text_page=293, english="Hawk Owl", latin="Surnia funerea", author="Dum.",
       modern_en="Northern Hawk-Owl", modern_latin="Surnia ulula", status="reclassified",
       resolved_by="The species epithet Gould used, funerea, is now treated as a synonym; the accepted name is Surnia ulula. This is the one owl on the plate that keeps Gould's genus, Surnia, as its own."),

  dict(plate_page=300, text_page=301, english="Little Owl", latin="Athene noctua", author="",
       modern_en="Little Owl", modern_latin="Athene noctua", status="stable"),
]

# Sanity check: 34 plates, 32 unique species entries (candicans and aeruginosus
# each contribute a second plate sharing an existing account).
assert len(SPECIES_GB_V1) == 34
