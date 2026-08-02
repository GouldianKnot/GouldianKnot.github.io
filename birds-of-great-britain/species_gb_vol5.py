# Birds of Great Britain -- Volume V (Gould, 1873)
# Natatores: geese, swans, shelducks and dabbling ducks, diving ducks and
# sawbills, grebes, divers/loons, auks, cormorants, the gannet, gulls, terns,
# skuas, and the petrels and shearwaters -- the fifth and final volume.
#
# Schema matches the earlier volumes: plate_page, text_page (or None),
# shares_with, plate_note, english, latin, author, modern_en, modern_latin,
# status, resolved_by/note.
#
# Sourcing discipline (as in every prior volume): every `latin`/`author` pair
# below is taken from the actual printed heading line at the top of the
# species' own text page, read directly off rendered page images and
# cross-checked against the OCR dump at /tmp/vol5_all_headings.txt -- never
# from an older name buried in the synonymy.
#
# Plate/text pairing was established the same way as before: rendering every
# page, running the colourfulness-heuristic candidate detector
# (detect_vol5_plates.py), and then visually inspecting every irregular gap
# in the candidate list rather than assuming a fixed cadence. Several
# candidates turned out to be heavily foxed blank versos or faint set-off
# (ink bleed-through from the facing plate) rather than real plates, and were
# excluded after direct image inspection: pages 55, 251, 255, 335, 347, 349
# and 350 (the last two are in fact the Leach's Storm-Petrel account's own
# text pages, not a separate plate -- caught because they scored just over
# the detector's colourfulness threshold from the printed text block itself).
#
# One plate the heuristic missed outright: page 120 (Common Scoter, Oidemia
# nigra) is printed almost entirely in matte black, which falls under the
# saturation threshold the detector uses to flag "colourful" pages. It was
# only found by manually inspecting the unusually wide (8-page) gap between
# its neighbouring candidates at 116 and 124.
#
# Unlike Volumes II-IV, this volume turned out to have NO shared-account
# plates -- every one of the 86 confirmed plates has its own full species
# text page (confirmed by checking that every text page OCR'd to a
# substantial, non-blank result).

SPECIES_GB_V5 = [

    dict(plate_page=12, text_page=13, english="Grey Lag Goose", latin="Anser ferus", author=None,
         modern_en="Greylag Goose", modern_latin="Anser anser", status="reclassified",
         resolved_by="Epithet standardised to the tautonym anser, replacing Gould's ferus; the genus was already correct in Gould's own heading."),

    dict(plate_page=16, text_page=17, english="Bean-Goose", latin="Anser segetum", author=None,
         modern_en="Taiga Bean Goose", modern_latin="Anser fabalis", status="reclassified",
         resolved_by="Epithet standardised to fabalis, replacing Gould's segetum.",
         note="Gould treated the Bean-Goose as a single species; it is now usually split into the Taiga Bean Goose (Anser fabalis) and the Tundra Bean Goose (Anser serrirostris), which likely both occurred among the birds he knew simply as \"the Bean-Goose.\""),

    dict(plate_page=20, text_page=21, english="Pink-footed Goose", latin="Anser brachyrhynchus", author="Bai.",
         modern_en="Pink-footed Goose", modern_latin="Anser brachyrhynchus", status="stable"),

    dict(plate_page=24, text_page=25, english="White-fronted Goose", latin="Anser albifrons", author=None,
         modern_en="Greater White-fronted Goose", modern_latin="Anser albifrons", status="stable"),

    dict(plate_page=28, text_page=29, english="Bernicle Goose", latin="Bernicla leucopsis", author=None,
         modern_en="Barnacle Goose", modern_latin="Branta leucopsis", status="reclassified",
         resolved_by="Moved from Bernicla into Branta, the genus now used for all the black geese."),

    dict(plate_page=32, text_page=33, english="Red-breasted Goose", latin="Bernicla ruficollis", author=None,
         modern_en="Red-breasted Goose", modern_latin="Branta ruficollis", status="reclassified",
         resolved_by="Moved from Bernicla into Branta, alongside the Barnacle and Brent Geese."),

    dict(plate_page=36, text_page=37, english="Brent Goose", latin="Bernicla brenta", author=None,
         modern_en="Brant Goose", modern_latin="Branta bernicla", status="reclassified",
         resolved_by="Moved from Bernicla into Branta -- so the genus and species names have effectively traded spellings with Gould's heading."),

    dict(plate_page=40, text_page=41, english="Mute Swan", latin="Cygnus olor", author=None,
         modern_en="Mute Swan", modern_latin="Cygnus olor", status="stable"),

    dict(plate_page=44, text_page=45, english="Wild Swan or Whooper", latin="Cygnus ferus", author=None,
         modern_en="Whooper Swan", modern_latin="Cygnus cygnus", status="reclassified",
         resolved_by="Epithet standardised to the tautonym cygnus, replacing Gould's ferus."),

    dict(plate_page=48, text_page=49, english="Bewick's Swan", latin="Cygnus minor", author=None,
         modern_en="Tundra Swan (Bewick's Swan)", modern_latin="Cygnus columbianus bewickii", status="contested",
         resolved_by="Epithet standardised to bewickii, replacing Gould's minor.",
         note="Most current authorities treat Bewick's Swan as the Eurasian subspecies of the Tundra Swan (Cygnus columbianus), whose nominate subspecies breeds in arctic North America; a minority still prefer to split it back out as the full species Cygnus bewickii."),

    dict(plate_page=52, text_page=53, english="Sheldrake", latin="Tadorna vulpanser", author=None,
         modern_en="Common Shelduck", modern_latin="Tadorna tadorna", status="reclassified",
         resolved_by="Epithet standardised to the tautonym tadorna, replacing Gould's vulpanser; the genus was already correct in Gould's own heading."),

    dict(plate_page=56, text_page=57, english="Ruddy Sheldrake", latin="Casarca rutila", author=None,
         modern_en="Ruddy Shelduck", modern_latin="Tadorna ferruginea", status="reclassified",
         resolved_by="Moved from Casarca into Tadorna, with the epithet changed to ferruginea."),

    dict(plate_page=60, text_page=61, english="Widgeon", latin="Mareca penelope", author=None,
         modern_en="Eurasian Wigeon", modern_latin="Mareca penelope", status="stable",
         note="Gould's genus Mareca spent most of the twentieth century submerged inside the broad genus Anas, along with the Shoveller, Gadwall, and Garganey below; DNA evidence in the 2010s split the dabbling ducks back apart along very nearly the lines Gould was already using in 1873."),

    dict(plate_page=64, text_page=65, english="Shoveller Duck", latin="Spatula clypeata", author=None,
         modern_en="Northern Shoveler", modern_latin="Spatula clypeata", status="stable",
         note="As with the Wigeon above, Gould's genus Spatula was folded into Anas for most of the twentieth century before being revived by recent molecular work -- so this heading is, again, already the modern name."),

    dict(plate_page=68, text_page=69, english="Mallard or Wild Duck", latin="Anas boschas", author="Linn.",
         modern_en="Mallard", modern_latin="Anas platyrhynchos", status="reclassified",
         resolved_by="Epithet standardised to platyrhynchos, replacing Gould's boschas; the genus was already correct in Gould's own heading."),

    dict(plate_page=72, text_page=73, english="Teal", latin="Querquedula crecca", author=None,
         modern_en="Eurasian Teal", modern_latin="Anas crecca", status="reclassified",
         resolved_by="Moved from Querquedula into Anas; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=76, text_page=77, english="Garganey", latin="Querquedula circia", author=None,
         modern_en="Garganey", modern_latin="Spatula querquedula", status="reclassified",
         resolved_by="Moved from Querquedula into Spatula (alongside the Shoveller, not into Anas as its close look-alike the Teal was -- see above); Gould's own genus name survives, slightly respelled, as the modern species epithet."),

    dict(plate_page=80, text_page=81, english="Pintailed Duck", latin="Dafila acuta", author=None,
         modern_en="Northern Pintail", modern_latin="Anas acuta", status="reclassified",
         resolved_by="Moved from Dafila into Anas; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=84, text_page=85, english="Gadwall", latin="Chaulelasmus strepera", author=None,
         modern_en="Gadwall", modern_latin="Mareca strepera", status="reclassified",
         resolved_by="Moved from Chaulelasmus into Mareca, joining the Wigeon in that revived genus."),

    dict(plate_page=88, text_page=89, english="Pochard", latin="Nyroca ferina", author=None,
         modern_en="Common Pochard", modern_latin="Aythya ferina", status="reclassified",
         resolved_by="Moved from Nyroca into Aythya, the genus now used for all the diving ducks in this group."),

    dict(plate_page=92, text_page=93, english="White-eyed or Ferruginous Duck", latin="Nyroca leucophthalmos", author=None,
         modern_en="Ferruginous Duck", modern_latin="Aythya nyroca", status="reclassified",
         resolved_by="Moved from Nyroca into Aythya; Gould's own genus name survives as the modern species epithet."),

    dict(plate_page=96, text_page=97, english="Red-crested Duck", latin="Branta rufina", author=None,
         modern_en="Red-crested Pochard", modern_latin="Netta rufina", status="reclassified",
         resolved_by="Moved from Branta into Netta.",
         note="Gould's use of Branta for this duck is a striking false friend: the same genus name is used above for the Barnacle, Red-breasted, and Brent Geese, and today Branta is reserved exclusively for that group of black geese -- entirely unrelated to this diving duck."),

    dict(plate_page=100, text_page=101, english="Tufted Duck", latin="Fuligula cristata", author=None,
         modern_en="Tufted Duck", modern_latin="Aythya fuligula", status="reclassified",
         resolved_by="Moved from Fuligula into Aythya, with the epithet changed to fuligula -- Gould's own genus name survives as the modern species epithet."),

    dict(plate_page=104, text_page=105, english="Scaup Duck", latin="Fuligula marila", author=None,
         modern_en="Greater Scaup", modern_latin="Aythya marila", status="reclassified",
         resolved_by="Moved from Fuligula into Aythya; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=108, text_page=109, english="Steller's Duck", latin="Eniconetta stelleri", author=None,
         modern_en="Steller's Eider", modern_latin="Polysticta stelleri", status="reclassified",
         resolved_by="Moved from Eniconetta into its own genus, Polysticta; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=112, text_page=113, english="Eider Duck", latin="Somateria mollissima", author=None,
         modern_en="Common Eider", modern_latin="Somateria mollissima", status="stable"),

    dict(plate_page=116, text_page=117, english="King Duck", latin="Somateria spectabilis", author=None,
         modern_en="King Eider", modern_latin="Somateria spectabilis", status="stable"),

    dict(plate_page=120, text_page=121, english="Scoter", latin="Oidemia nigra", author=None,
         modern_en="Common Scoter", modern_latin="Melanitta nigra", status="reclassified",
         resolved_by="Moved from Oidemia into Melanitta, the genus now used for all three scoters in this volume.",
         note="This plate is printed almost entirely in matte black and was missed by this pass's automated colour-based plate detector -- found only by noticing the unusually wide gap between its neighbouring candidates and checking the page directly."),

    dict(plate_page=124, text_page=125, english="Velvet Scoter", latin="Oidemia fusca", author=None,
         modern_en="Velvet Scoter", modern_latin="Melanitta fusca", status="reclassified",
         resolved_by="Moved from Oidemia into Melanitta; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=128, text_page=129, english="Surf-Scoter", latin="Oidemia perspicillata", author=None,
         modern_en="Surf Scoter", modern_latin="Melanitta perspicillata", status="reclassified",
         resolved_by="Moved from Oidemia into Melanitta; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=132, text_page=133, english="Golden-eye", latin="Clangula glaucion", author=None,
         modern_en="Common Goldeneye", modern_latin="Bucephala clangula", status="reclassified",
         resolved_by="Moved from Clangula into Bucephala, with the epithet changed to clangula -- Gould's own genus name survives as the modern species epithet.",
         note="Gould's genus Clangula reappears a few plates on, reassigned to an entirely different bird: the Long-tailed Duck below."),

    dict(plate_page=136, text_page=137, english="Harlequin Duck", latin="Histrionicus torquatus", author=None,
         modern_en="Harlequin Duck", modern_latin="Histrionicus histrionicus", status="reclassified",
         resolved_by="Epithet standardised to the tautonym histrionicus, replacing Gould's torquatus; the genus was already correct in Gould's own heading."),

    dict(plate_page=140, text_page=141, english="Long-tailed Duck", latin="Harelda glacialis", author=None,
         modern_en="Long-tailed Duck", modern_latin="Clangula hyemalis", status="reclassified",
         resolved_by="Moved from Harelda into Clangula, with the epithet changed to hyemalis.",
         note="This is the same genus name Clangula that Gould applied a few plates earlier to the Golden-eye (now Bucephala clangula) -- a tidy example of an old generic name being recycled onto a different bird entirely as the group was reorganised."),

    dict(plate_page=144, text_page=145, english="Goosander", latin="Mergus castor", author="Linn.",
         modern_en="Common Merganser (Goosander)", modern_latin="Mergus merganser", status="reclassified",
         resolved_by="Epithet standardised to merganser, replacing Gould's castor; the genus was already correct in Gould's own heading."),

    dict(plate_page=148, text_page=149, english="Merganser", latin="Mergus serrator", author=None,
         modern_en="Red-breasted Merganser", modern_latin="Mergus serrator", status="stable"),

    dict(plate_page=152, text_page=153, english="Hooded Merganser", latin="Mergus cucullatus", author="Lin.",
         modern_en="Hooded Merganser", modern_latin="Lophodytes cucullatus", status="reclassified",
         resolved_by="Moved from Mergus into its own genus, Lophodytes; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=156, text_page=157, english="Smew, or Nun", latin="Mergus albellus", author=None,
         modern_en="Smew", modern_latin="Mergellus albellus", status="reclassified",
         resolved_by="Moved from Mergus into its own genus, Mergellus; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=160, text_page=161, english="Great-crested Grebe", latin="Podiceps cristatus", author=None,
         modern_en="Great Crested Grebe", modern_latin="Podiceps cristatus", status="stable"),

    dict(plate_page=164, text_page=165, english="Red-necked Grebe", latin="Podiceps rubricollis", author=None,
         modern_en="Red-necked Grebe", modern_latin="Podiceps grisegena", status="reclassified",
         resolved_by="Epithet standardised to grisegena, replacing Gould's rubricollis; the genus was already correct in Gould's own heading."),

    dict(plate_page=168, text_page=169, english="Horned Grebe", latin="Podiceps auritus", author=None,
         modern_en="Horned Grebe (Slavonian Grebe)", modern_latin="Podiceps auritus", status="stable"),

    dict(plate_page=172, text_page=173, english="Eared Grebe", latin="Podiceps nigricollis", author=None,
         modern_en="Black-necked Grebe (Eared Grebe)", modern_latin="Podiceps nigricollis", status="stable"),

    dict(plate_page=176, text_page=177, english="Little Grebe or Dabchick", latin="Podiceps minor", author=None,
         modern_en="Little Grebe", modern_latin="Tachybaptus ruficollis", status="reclassified",
         resolved_by="Moved from Podiceps into its own genus, Tachybaptus, with the epithet changed to ruficollis."),

    dict(plate_page=180, text_page=181, english="Great Northern Diver", latin="Colymbus glacialis", author="Lin.",
         modern_en="Common Loon", modern_latin="Gavia immer", status="reclassified",
         resolved_by="Moved from Colymbus into Gavia, the genus now used for all the divers/loons, with the epithet changed to immer."),

    dict(plate_page=184, text_page=185, english="Black-throated Diver", latin="Colymbus arcticus", author="Linn.",
         modern_en="Black-throated Diver (Arctic Loon)", modern_latin="Gavia arctica", status="reclassified",
         resolved_by="Moved from Colymbus into Gavia; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=188, text_page=189, english="Red-throated Diver", latin="Colymbus septentrionalis", author="Linn.",
         modern_en="Red-throated Loon", modern_latin="Gavia stellata", status="reclassified",
         resolved_by="Moved from Colymbus into Gavia, with the epithet changed to stellata."),

    dict(plate_page=192, text_page=193, english="Great Auk", latin="Alca impennis", author=None,
         modern_en="Great Auk", modern_latin="Pinguinus impennis", status="reclassified",
         resolved_by="Moved from Alca into its own genus, Pinguinus.",
         note="By far the most sobering entry in this volume: the Great Auk was already extinct by the time Gould published this account -- the last confirmed pair was killed on Eldey, off Iceland, on 3 June 1844, not thirty years before this plate was printed. Gould's own text (citing Newton's 1861 Ibis paper, in the synonymy above) treats it as a very recent loss rather than history."),

    dict(plate_page=196, text_page=197, english="Razorbill", latin="Alca torda", author="Linn.",
         modern_en="Razorbill", modern_latin="Alca torda", status="stable"),

    dict(plate_page=200, text_page=201, english="Common Guillemot", latin="Uria troile", author=None,
         modern_en="Common Murre (Common Guillemot)", modern_latin="Uria aalge", status="reclassified",
         resolved_by="Epithet standardised to aalge, replacing Gould's troile; the genus was already correct in Gould's own heading."),

    dict(plate_page=204, text_page=205, english="Black Guillemot", latin="Uria grylle", author=None,
         modern_en="Black Guillemot", modern_latin="Cepphus grylle", status="reclassified",
         resolved_by="Moved from Uria into its own genus, Cepphus; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=208, text_page=209, english="Little Auk", latin="Mergulus alle", author=None,
         modern_en="Little Auk (Dovekie)", modern_latin="Alle alle", status="reclassified",
         resolved_by="Moved from Mergulus into its own genus, Alle -- Gould's own species epithet becomes the tautonymous genus name."),

    dict(plate_page=212, text_page=213, english="Puffin", latin="Fratercula arctica", author=None,
         modern_en="Atlantic Puffin", modern_latin="Fratercula arctica", status="stable"),

    dict(plate_page=216, text_page=217, english="Cormorant", latin="Phalacrocorax carbo", author=None,
         modern_en="Great Cormorant", modern_latin="Phalacrocorax carbo", status="stable"),

    dict(plate_page=220, text_page=221, english="Crested Cormorant, or Shag", latin="Phalacrocorax graculus", author=None,
         modern_en="European Shag", modern_latin="Gulosus aristotelis", status="reclassified",
         resolved_by="Split off from Phalacrocorax into its own genus, Gulosus, with the epithet changed to aristotelis.",
         note="The epithet graculus that Gould used has not vanished -- it now belongs, confusingly, to an unrelated bird (the Alpine Chough, Pyrrhocorax graculus), one of several historical name collisions untangled as the cormorant family was revised."),

    dict(plate_page=224, text_page=225, english="Gannet, or Solan Goose", latin="Sula bassana", author=None,
         modern_en="Northern Gannet", modern_latin="Morus bassanus", status="reclassified",
         resolved_by="Moved from Sula (kept for the tropical boobies) into its own genus, Morus, with the epithet's ending corrected to agree with the masculine genus."),

    dict(plate_page=228, text_page=229, english="Great Black-backed Gull", latin="Larus marinus", author="Lin.",
         modern_en="Great Black-backed Gull", modern_latin="Larus marinus", status="stable"),

    dict(plate_page=232, text_page=233, english="Lesser Black-backed Gull", latin="Larus fuscus", author="Lin.",
         modern_en="Lesser Black-backed Gull", modern_latin="Larus fuscus", status="stable"),

    dict(plate_page=236, text_page=237, english="Glaucous Gull", latin="Larus glaucus", author="Brünn.",
         modern_en="Glaucous Gull", modern_latin="Larus hyperboreus", status="reclassified",
         resolved_by="Epithet standardised to hyperboreus, replacing Gould's glaucus (which survives only as the bird's English-derived common name, \"Glaucous Gull\")."),

    dict(plate_page=240, text_page=241, english="Iceland Gull", latin="Larus islandicus", author="Edm.",
         modern_en="Iceland Gull", modern_latin="Larus glaucoides", status="reclassified",
         resolved_by="Epithet standardised to glaucoides, replacing Gould's islandicus (which survives as the bird's English name)."),

    dict(plate_page=244, text_page=245, english="Herring Gull", latin="Larus argentatus", author="Brünn.",
         modern_en="European Herring Gull", modern_latin="Larus argentatus", status="stable"),

    dict(plate_page=248, text_page=249, english="Common Gull", latin="Larus canus", author="Linn.",
         modern_en="Common Gull (Mew Gull)", modern_latin="Larus canus", status="stable"),

    dict(plate_page=252, text_page=253, english="Kittiwake", latin="Rissa tridactyla", author=None,
         modern_en="Black-legged Kittiwake", modern_latin="Rissa tridactyla", status="stable"),

    dict(plate_page=256, text_page=257, english="Ivory Gull", latin="Pagophila eburnea", author=None,
         modern_en="Ivory Gull", modern_latin="Pagophila eburnea", status="stable"),

    dict(plate_page=260, text_page=261, english="Ross's Gull", latin="Rhodostethia rossii", author=None,
         modern_en="Ross's Gull", modern_latin="Rhodostethia rosea", status="reclassified",
         resolved_by="Epithet standardised to rosea, replacing Gould's rossii (which survives as the bird's English name honouring polar explorer James Clark Ross); the genus was already correct in Gould's own heading."),

    dict(plate_page=264, text_page=265, english="Black-headed Gull", latin="Chroicocephalus ridibundus", author=None,
         modern_en="Black-headed Gull", modern_latin="Chroicocephalus ridibundus", status="stable",
         note="Gould's genus Chroicocephalus was submerged into the broad genus Larus for most of the twentieth century, then revived by DNA evidence in the 2000s -- so, as with the Wigeon and Shoveller earlier in this volume, this heading is already the modern name."),

    dict(plate_page=268, text_page=269, english="Bonaparte's Gull", latin="Chroicocephalus philadelphia", author=None,
         modern_en="Bonaparte's Gull", modern_latin="Chroicocephalus philadelphia", status="stable"),

    dict(plate_page=272, text_page=273, english="Little Gull", latin="Hydrocoloeus minutus", author=None,
         modern_en="Little Gull", modern_latin="Hydrocoloeus minutus", status="stable"),

    dict(plate_page=276, text_page=277, english="Sabine's Gull", latin="Xema Sabini", author=None,
         modern_en="Sabine's Gull", modern_latin="Xema sabini", status="stable"),

    dict(plate_page=280, text_page=281, english="Caspian Tern", latin="Hydroprogne caspia", author=None,
         modern_en="Caspian Tern", modern_latin="Hydroprogne caspia", status="stable"),

    dict(plate_page=284, text_page=285, english="Sandwich Tern", latin="Actochelidon cantiaca", author=None,
         modern_en="Sandwich Tern", modern_latin="Thalasseus sandvicensis", status="reclassified",
         resolved_by="Moved from Actochelidon into Thalasseus, the genus now used for the crested terns, with the epithet changed to sandvicensis."),

    dict(plate_page=288, text_page=289, english="Common Tern", latin="Sterna hirundo", author="Lin.",
         modern_en="Common Tern", modern_latin="Sterna hirundo", status="stable"),

    dict(plate_page=292, text_page=293, english="Roseate Tern", latin="Sterna paradisea", author="Brünn.",
         modern_en="Roseate Tern", modern_latin="Sterna dougallii", status="reclassified",
         resolved_by="Epithet standardised to dougallii, honouring the Scottish naturalist Patrick Neill MacGillivray's contemporary Dr MacDougall (traditionally credited as the first to distinguish the species).",
         note="An easy mix-up worth flagging: the name Gould's heading cites for this plate, Sterna paradisea, is today the scientific epithet (spelled paradisaea) of a completely different bird -- the Arctic Tern, on the very next plate. Tern nomenclature in this period was genuinely unsettled, and paradisea/paradisaea seems to have floated between species in different authors' hands before settling on the Arctic Tern."),

    dict(plate_page=296, text_page=297, english="Arctic Tern", latin="Sterna macrura", author="Naum.",
         modern_en="Arctic Tern", modern_latin="Sterna paradisaea", status="reclassified",
         resolved_by="Epithet standardised to paradisaea, replacing Gould's macrura -- see the note on the preceding Roseate Tern plate for how that name had, in Gould's own day, been applied instead to that other species."),

    dict(plate_page=300, text_page=301, english="Little Tern", latin="Sternula minuta", author=None,
         modern_en="Little Tern", modern_latin="Sternula albifrons", status="reclassified",
         resolved_by="Epithet standardised to albifrons, replacing Gould's minuta; the genus was already correct in Gould's own heading."),

    dict(plate_page=304, text_page=305, english="Gull-billed Tern", latin="Gelochelidon anglica", author=None,
         modern_en="Gull-billed Tern", modern_latin="Gelochelidon nilotica", status="reclassified",
         resolved_by="Epithet standardised to nilotica, replacing Gould's anglica; the genus was already correct in Gould's own heading."),

    dict(plate_page=308, text_page=309, english="Black Tern", latin="Hydrochelidon nigra", author=None,
         modern_en="Black Tern", modern_latin="Chlidonias niger", status="reclassified",
         resolved_by="Moved from Hydrochelidon into Chlidonias, the genus now used for all three marsh terns in this volume; the species epithet was already correct (bar spelling) in Gould's own heading."),

    dict(plate_page=312, text_page=313, english="White-winged Tern", latin="Hydrochelidon leucoptera", author=None,
         modern_en="White-winged Tern (White-winged Black Tern)", modern_latin="Chlidonias leucopterus", status="reclassified",
         resolved_by="Moved from Hydrochelidon into Chlidonias; the species epithet was already correct (bar its grammatical ending) in Gould's own heading."),

    dict(plate_page=316, text_page=317, english="Whiskered Tern", latin="Hydrochelidon leucopareia", author=None,
         modern_en="Whiskered Tern", modern_latin="Chlidonias hybridus", status="reclassified",
         resolved_by="Moved from Hydrochelidon into Chlidonias, with the epithet changed to hybridus, replacing Gould's leucopareia."),

    dict(plate_page=320, text_page=321, english="Great Skua", latin="Stercorarius catarrhactes", author=None,
         modern_en="Great Skua", modern_latin="Stercorarius skua", status="reclassified",
         resolved_by="Epithet standardised to skua, replacing Gould's catarrhactes.",
         note="The old epithet catarrhactes did not disappear -- it now names an entirely unrelated bird, the Southern Rockhopper Penguin (Eudyptes chrysocome, long placed in a genus \"Catarrhactes\" in older literature), another case of a 19th-century name migrating to a completely different family."),

    dict(plate_page=324, text_page=325, english="Pomatorhine Skua", latin="Stercorarius pomatorhinus", author=None,
         modern_en="Pomarine Skua (Pomarine Jaeger)", modern_latin="Stercorarius pomarinus", status="reclassified",
         resolved_by="Epithet standardised to pomarinus, a minor respelling of Gould's pomatorhinus; the genus was already correct in Gould's own heading."),

    dict(plate_page=328, text_page=329, english="Arctic Skua", latin="Stercorarius parasiticus", author=None,
         modern_en="Arctic Skua (Parasitic Jaeger)", modern_latin="Stercorarius parasiticus", status="stable"),

    dict(plate_page=332, text_page=333, english="Long-tailed Skua", latin="Stercorarius longicaudus", author=None,
         modern_en="Long-tailed Skua (Long-tailed Jaeger)", modern_latin="Stercorarius longicaudus", status="stable"),

    dict(plate_page=336, text_page=337, english="Fulmar", latin="Procellaria glacialis", author="Linn.",
         modern_en="Northern Fulmar", modern_latin="Fulmarus glacialis", status="reclassified",
         resolved_by="Moved from Procellaria into its own genus, Fulmarus; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=340, text_page=341, english="Great Shearwater", latin="Puffinus major", author="Fab.",
         modern_en="Great Shearwater", modern_latin="Ardenna gravis", status="reclassified",
         resolved_by="Moved from Puffinus into Ardenna, the genus now used for the larger shearwaters, with the epithet changed to gravis."),

    dict(plate_page=344, text_page=345, english="Manx Shearwater", latin="Puffinus anglorum", author=None,
         modern_en="Manx Shearwater", modern_latin="Puffinus puffinus", status="reclassified",
         resolved_by="Epithet standardised to the tautonym puffinus, replacing Gould's anglorum; the genus was already correct in Gould's own heading."),

    dict(plate_page=348, text_page=349, english="Fork-tailed Storm-Petrel", latin="Thalassidroma Leachii", author=None,
         modern_en="Leach's Storm Petrel", modern_latin="Hydrobates leachii", status="reclassified",
         resolved_by="Moved from Thalassidroma into Hydrobates, the genus now used for all the Northern Hemisphere storm-petrels."),

    dict(plate_page=352, text_page=353, english="Storm-Petrel", latin="Thalassidroma pelagica", author=None,
         modern_en="European Storm Petrel", modern_latin="Hydrobates pelagicus", status="reclassified",
         resolved_by="Moved from Thalassidroma into Hydrobates; the species epithet was already correct (bar its grammatical ending) in Gould's own heading.",
         note="The very last plate of the five-volume work -- fittingly, the smallest seabird in the North Atlantic, which Gould's own text calls out as barely a fortieth the weight of the great albatrosses it opens the account by comparing it to."),
]

assert len(SPECIES_GB_V5) == 86
