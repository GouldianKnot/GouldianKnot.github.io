# Birds of Great Britain -- Volume IV (Gould, 1873)
# Rasores & Grallatores: pigeons and game birds, bustards, the crane, herons,
# storks, spoonbill, plovers and their allies, and the great run of waders
# (sandpipers, godwits, snipes, phalaropes) ending with the crakes and rails.
#
# Schema matches species_gb_vol2.py / species_gb_vol3.py:
#   plate_page, text_page (or None), shares_with, plate_note,
#   english, latin, author, modern_en, modern_latin, status, resolved_by/note
#
# Sourcing discipline (lesson learned the hard way in Volume II): every
# `latin`/`author` pair below is taken from the actual printed heading line
# at the top of the species' text page (bold small caps genus + species,
# often followed by an authority abbreviation) -- never from an older name
# buried further down in the synonymy list. Headings were read directly off
# rendered page images and cross-checked against the OCR dump at
# /tmp/vol4_all_headings.txt.
#
# Plate/text pairing and the shared-plate list below were established by
# visually inspecting every irregular gap in the colourfulness-heuristic
# candidate list (detect_vol4_plates.py), not assumed from a fixed cadence --
# several "false positive" candidates turned out to be heavily foxed blank
# versos (pages 35, 89, 117, 161, 301) which were excluded after direct
# image inspection, exactly as happened with Volume III's page 36/281.
#
# Seven plates share their written account with a preceding plate (Gould's
# usual practice for a second plumage/season/age of the same species):
#   43 -> 40   (Ptarmigan, summer plumage)
#   46 -> 40   (Ptarmigan, third plate -- a further plumage/sex variant;
#               this plate's own caption did not survive legibly in the scan)
#   153 -> 150 (Grey Plover, winter plumage and young of the year)
#   159 -> 156 (Golden Plover, winter plumage)
#   249 -> 246 (Ruff, plumage of the first autumn)
#   279 -> 276 (Dunlin, winter plumage)
#   327 -> 324 (Grey Phalarope, winter plumage)

SPECIES_GB_V4 = [

    dict(plate_page=12, text_page=13, english="Wood-Pigeon or Cushat", latin="Palumbus torquatus", author=None,
         modern_en="Common Wood Pigeon", modern_latin="Columba palumbus", status="reclassified",
         resolved_by="Moved from the split-off genus Palumbus back into Columba, where it sits with the other true pigeons."),

    dict(plate_page=16, text_page=17, english="Stock-Dove", latin="Columba oenas", author="Linn.",
         modern_en="Stock Dove", modern_latin="Columba oenas", status="stable"),

    dict(plate_page=20, text_page=21, english="Rock-Pigeon", latin="Columba livia", author="Temm.",
         modern_en="Rock Dove", modern_latin="Columba livia", status="stable",
         note="Gould credits the heading to Temminck rather than Linnaeus, but the binomial itself was already the modern one -- the ancestor of every domestic and feral pigeon."),

    dict(plate_page=24, text_page=25, english="Turtledove", latin="Turtur auritus", author="Ray",
         modern_en="European Turtle Dove", modern_latin="Streptopelia turtur", status="reclassified",
         resolved_by="Moved from Turtur into Streptopelia along with the rest of the Old World turtle-doves and collared-doves."),

    dict(plate_page=28, text_page=29, english="Capercailzie or Cock of the Wood", latin="Tetrao urogallus", author="Linn.",
         modern_en="Western Capercaillie", modern_latin="Tetrao urogallus", status="stable"),

    dict(plate_page=32, text_page=33, english="Blackcock", latin="Tetrao tetrix", author="Linn.",
         modern_en="Black Grouse", modern_latin="Lyrurus tetrix", status="reclassified",
         resolved_by="Split from Tetrao (retained for the Capercaillie) into its own genus Lyrurus, reflecting the lyre-shaped tail Gould's own text singles out as diagnostic."),

    dict(plate_page=36, text_page=37, english="Red Grouse", latin="Lagopus scoticus", author=None,
         modern_en="Red Grouse", modern_latin="Lagopus lagopus scotica", status="lumped",
         resolved_by="No longer treated as its own species -- folded into Lagopus lagopus (Willow Ptarmigan/Willow Grouse) as the endemic British and Irish subspecies scotica, distinguished mainly by never turning white in winter."),

    dict(plate_page=40, text_page=41, english="Ptarmigan", latin="Lagopus mutus", author=None,
         modern_en="Rock Ptarmigan", modern_latin="Lagopus muta", status="stable",
         note="Effectively the same name Gould used; the epithet's ending was later corrected from mutus to muta to agree grammatically with the feminine genus Lagopus, per the ICZN rules of Latin gender agreement -- not a change of identity. This plate shows the white winter plumage; plates 43 and 46 (same page-41 account) show the summer and a further plumage of the same bird."),
    dict(plate_page=43, text_page=None, shares_with=40, plate_note="Summer plumage",
         english="Ptarmigan", latin="Lagopus mutus", author=None,
         modern_en="Rock Ptarmigan", modern_latin="Lagopus muta", status="stable"),
    dict(plate_page=46, text_page=None, shares_with=40, plate_note="Further plumage (caption not legible in this scan)",
         english="Ptarmigan", latin="Lagopus mutus", author=None,
         modern_en="Rock Ptarmigan", modern_latin="Lagopus muta", status="stable"),

    dict(plate_page=50, text_page=51, english="Pallas's Sandgrouse", latin="Syrrhaptes paradoxus", author=None,
         modern_en="Pallas's Sandgrouse", modern_latin="Syrrhaptes paradoxus", status="stable"),

    dict(plate_page=54, text_page=55, english="Common Pheasant", latin="Phasianus colchicus", author="Lin.",
         modern_en="Common Pheasant", modern_latin="Phasianus colchicus", status="stable"),

    dict(plate_page=58, text_page=59, english="Partridge", latin="Perdix cinerea", author="Lin.",
         modern_en="Grey Partridge", modern_latin="Perdix perdix", status="reclassified",
         resolved_by="Species epithet standardised to perdix (matching the genus, a tautonym), replacing Gould's cinerea."),

    dict(plate_page=62, text_page=63, english="Red-legged Partridge", latin="Caccabis rubra", author=None,
         modern_en="Red-legged Partridge", modern_latin="Alectoris rufa", status="reclassified",
         resolved_by="Moved from Caccabis into Alectoris with the rest of the rock-partridges, and the epithet standardised to rufa."),

    dict(plate_page=66, text_page=67, english="Common Quail", latin="Coturnix communis", author=None,
         modern_en="Common Quail", modern_latin="Coturnix coturnix", status="reclassified",
         resolved_by="Epithet standardised to the tautonym coturnix, replacing Gould's communis."),

    dict(plate_page=70, text_page=71, english="Andalusian Turnix", latin="Turnix africanus", author="Des.",
         modern_en="Small Buttonquail", modern_latin="Turnix sylvaticus", status="contested",
         note="Gould's africanus is now generally treated as a synonym of Turnix sylvaticus (Small Buttonquail); the old, very occasional British/Iberian records of this bird are themselves disputed and it is not accepted as a genuine part of the British list today."),

    dict(plate_page=74, text_page=75, english="Great Bustard", latin="Otis tarda", author="Linn.",
         modern_en="Great Bustard", modern_latin="Otis tarda", status="stable"),

    dict(plate_page=78, text_page=79, english="Little Bustard", latin="Otis tetrax", author="Linn.",
         modern_en="Little Bustard", modern_latin="Tetrax tetrax", status="reclassified",
         resolved_by="Split off from Otis (kept for the Great Bustard) into its own genus, Tetrax -- a case of the species epithet becoming the genus name."),

    dict(plate_page=82, text_page=83, english="Common Crane", latin="Grus cinerea", author=None,
         modern_en="Common Crane", modern_latin="Grus grus", status="reclassified",
         resolved_by="Epithet standardised to the tautonym grus, replacing Gould's cinerea."),

    dict(plate_page=86, text_page=87, english="Heron", latin="Ardea cinerea", author="Lin.",
         modern_en="Grey Heron", modern_latin="Ardea cinerea", status="stable"),

    dict(plate_page=90, text_page=91, english="Purple Heron", latin="Ardea purpurea", author="Lin.",
         modern_en="Purple Heron", modern_latin="Ardea purpurea", status="stable"),

    dict(plate_page=94, text_page=95, english="Great White Egret or White Heron", latin="Herodias alba", author=None,
         modern_en="Great Egret", modern_latin="Ardea alba", status="reclassified",
         resolved_by="Moved from Herodias back into Ardea, where it sits with the other large herons -- the genus name Gould gives it has itself become the modern species epithet."),

    dict(plate_page=98, text_page=99, english="Little Egret", latin="Herodias garzetta", author=None,
         modern_en="Little Egret", modern_latin="Egretta garzetta", status="reclassified",
         resolved_by="Moved from Herodias into Egretta, the genus now used for the smaller white egrets."),

    dict(plate_page=102, text_page=103, english="Buff-backed Heron", latin="Bubulcus russatus", author=None,
         modern_en="Western Cattle Egret", modern_latin="Bubulcus ibis", status="reclassified",
         resolved_by="Genus Bubulcus is unchanged from Gould's own heading; the epithet was standardised to ibis, an older name that took priority over russatus."),

    dict(plate_page=106, text_page=107, english="Squacco Heron", latin="Buphus comatus", author=None,
         modern_en="Squacco Heron", modern_latin="Ardeola ralloides", status="reclassified",
         resolved_by="Moved from Buphus into Ardeola (the genus for the squacco herons generally), with the epithet standardised to ralloides."),

    dict(plate_page=110, text_page=111, english="Night-Heron", latin="Nycticorax griseus", author=None,
         modern_en="Black-crowned Night Heron", modern_latin="Nycticorax nycticorax", status="reclassified",
         resolved_by="Epithet standardised to the tautonym nycticorax, replacing Gould's griseus; the genus itself was already correct in Gould's own heading."),

    dict(plate_page=114, text_page=115, english="Bittern", latin="Botaurus stellaris", author=None,
         modern_en="Great Bittern", modern_latin="Botaurus stellaris", status="stable"),

    dict(plate_page=118, text_page=119, english="American Bittern", latin="Botaurus lentiginosus", author=None,
         modern_en="American Bittern", modern_latin="Botaurus lentiginosus", status="stable"),

    dict(plate_page=122, text_page=123, english="Little Bittern", latin="Ardetta minuta", author=None,
         modern_en="Little Bittern", modern_latin="Ixobrychus minutus", status="reclassified",
         resolved_by="Moved from Ardetta into Ixobrychus, the genus now used for the small bitterns worldwide."),

    dict(plate_page=126, text_page=127, english="Stork", latin="Ciconia alba", author=None,
         modern_en="White Stork", modern_latin="Ciconia ciconia", status="reclassified",
         resolved_by="Epithet standardised to the tautonym ciconia, replacing Gould's alba; the genus was already correct in Gould's heading."),

    dict(plate_page=130, text_page=131, english="Black Stork", latin="Ciconia nigra", author=None,
         modern_en="Black Stork", modern_latin="Ciconia nigra", status="stable"),

    dict(plate_page=134, text_page=135, english="Spoonbill", latin="Platalea leucorodia", author="Lin.",
         modern_en="Eurasian Spoonbill", modern_latin="Platalea leucorodia", status="stable"),

    dict(plate_page=138, text_page=139, english="Lapwing or Peewit", latin="Vanellus cristatus", author=None,
         modern_en="Northern Lapwing", modern_latin="Vanellus vanellus", status="reclassified",
         resolved_by="Epithet standardised to the tautonym vanellus, replacing Gould's cristatus; the genus was already correct."),

    dict(plate_page=142, text_page=143, english="Stilt- or Long-legged Plover", latin="Himantopus candidus", author=None,
         modern_en="Black-winged Stilt", modern_latin="Himantopus himantopus", status="reclassified",
         resolved_by="Epithet standardised to the tautonym himantopus, replacing Gould's candidus."),

    dict(plate_page=146, text_page=147, english="Stone-Plover, or Thick-knee", latin="Oedicnemus crepitans", author=None,
         modern_en="Eurasian Stone-curlew", modern_latin="Burhinus oedicnemus", status="reclassified",
         resolved_by="Moved from Oedicnemus into Burhinus, the genus now used for all the thick-knees; Gould's own genus name survives as the modern species epithet."),

    dict(plate_page=150, text_page=151, english="Grey Plover", latin="Squatarola helvetica", author=None,
         modern_en="Grey Plover", modern_latin="Pluvialis squatarola", status="reclassified",
         resolved_by="Moved from the split-off genus Squatarola into Pluvialis, alongside the golden plovers; Gould's own genus name survives as the modern species epithet. This plate shows the summer plumage; plate 153 (same account) shows the winter plumage and young of the year."),
    dict(plate_page=153, text_page=None, shares_with=150, plate_note="Plumage of winter, and young of the year",
         english="Grey Plover", latin="Squatarola helvetica", author=None,
         modern_en="Grey Plover", modern_latin="Pluvialis squatarola", status="reclassified"),

    dict(plate_page=156, text_page=157, english="Golden Plover", latin="Charadrius pluvialis", author="Linn.",
         modern_en="European Golden Plover", modern_latin="Pluvialis apricaria", status="reclassified",
         resolved_by="Moved from Charadrius into Pluvialis, and the epithet standardised to apricaria -- itself already given in Gould's own synonymy as Linnaeus's name for the summer bird. This plate shows the (unstated, presumably breeding) plumage; plate 159 (same account) is explicitly captioned winter plumage."),
    dict(plate_page=159, text_page=None, shares_with=156, plate_note="Winter plumage",
         english="Golden Plover", latin="Charadrius pluvialis", author="Linn.",
         modern_en="European Golden Plover", modern_latin="Pluvialis apricaria", status="reclassified"),

    dict(plate_page=162, text_page=163, english="Kentish Plover", latin="Aegialophilus cantianus", author=None,
         modern_en="Kentish Plover", modern_latin="Charadrius alexandrinus", status="reclassified",
         resolved_by="Moved from Aegialophilus into Charadrius, and the epithet standardised to alexandrinus, replacing Gould's cantianus (the name commemorating its former Kentish breeding colonies, now long gone from England)."),

    dict(plate_page=166, text_page=167, english="Ringed Plover", latin="Aegialitis hiaticula", author=None,
         modern_en="Common Ringed Plover", modern_latin="Charadrius hiaticula", status="reclassified",
         resolved_by="Moved from Aegialitis back into Charadrius; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=170, text_page=171, english="Little Ringed Plover", latin="Aegialitis minor", author=None,
         modern_en="Little Ringed Plover", modern_latin="Charadrius dubius", status="reclassified",
         resolved_by="Moved from Aegialitis into Charadrius, and the epithet standardised to dubius, an older name with priority over Gould's minor."),

    dict(plate_page=174, text_page=175, english="Dotterel", latin="Eudromias morinellus", author=None,
         modern_en="Eurasian Dotterel", modern_latin="Charadrius morinellus", status="reclassified",
         resolved_by="Moved from the split-off genus Eudromias back into Charadrius; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=178, text_page=179, english="Cream-Coloured Courser", latin="Cursorius gallicus", author="Gme.",
         modern_en="Cream-coloured Courser", modern_latin="Cursorius cursor", status="reclassified",
         resolved_by="Epithet standardised to the tautonym cursor, replacing Gould's gallicus."),

    dict(plate_page=182, text_page=183, english="Oyster-catcher", latin="Haematopus ostralegus", author="Linn.",
         modern_en="Eurasian Oystercatcher", modern_latin="Haematopus ostralegus", status="stable"),

    dict(plate_page=186, text_page=187, english="Common Pratincole", latin="Glareola pratincola", author=None,
         modern_en="Collared Pratincole", modern_latin="Glareola pratincola", status="stable"),

    dict(plate_page=190, text_page=191, english="Glossy Ibis", latin="Falcinellus igneus", author=None,
         modern_en="Glossy Ibis", modern_latin="Plegadis falcinellus", status="reclassified",
         resolved_by="Moved from Falcinellus into Plegadis; Gould's own genus name survives, slightly altered, as the modern species epithet."),

    dict(plate_page=194, text_page=195, english="Curlew", latin="Numenius arquata", author=None,
         modern_en="Eurasian Curlew", modern_latin="Numenius arquata", status="stable"),

    dict(plate_page=198, text_page=199, english="Whimbrel", latin="Numenius phaeopus", author=None,
         modern_en="Whimbrel", modern_latin="Numenius phaeopus", status="stable"),

    dict(plate_page=202, text_page=203, english="Black-tailed Godwit", latin="Limosa melanura", author=None,
         modern_en="Black-tailed Godwit", modern_latin="Limosa limosa", status="reclassified",
         resolved_by="Epithet standardised to the tautonym limosa, replacing Gould's melanura."),

    dict(plate_page=206, text_page=207, english="Bar-tailed Godwit", latin="Limosa rufa", author=None,
         modern_en="Bar-tailed Godwit", modern_latin="Limosa lapponica", status="reclassified",
         resolved_by="Epithet standardised to lapponica, replacing Gould's rufa -- lapponica already appears in Gould's own synonymy as Linnaeus's older name, a mirror of the Black-tailed Godwit's case just above."),

    dict(plate_page=210, text_page=211, english="Avocet", latin="Recurvirostra avocetta", author="Linn.",
         modern_en="Pied Avocet", modern_latin="Recurvirostra avosetta", status="stable",
         note="Only a spelling variant (avocetta/avosetta) separates Gould's heading from the modern name."),

    dict(plate_page=214, text_page=215, english="Greenshank", latin="Glottis canescens", author=None,
         modern_en="Common Greenshank", modern_latin="Tringa nebularia", status="reclassified",
         resolved_by="Moved from Glottis into Tringa, and the epithet standardised to nebularia, replacing Gould's canescens."),

    dict(plate_page=218, text_page=219, english="Redshank", latin="Totanus calidris", author=None,
         modern_en="Common Redshank", modern_latin="Tringa totanus", status="reclassified",
         resolved_by="Moved from Totanus into Tringa, with the epithet changed to totanus -- so genus and epithet have effectively traded places with Gould's heading."),

    dict(plate_page=222, text_page=223, english="Spotted Redshank", latin="Totanus fuscus", author=None,
         modern_en="Spotted Redshank", modern_latin="Tringa erythropus", status="reclassified",
         resolved_by="Moved from Totanus into Tringa, and the epithet standardised to erythropus, replacing Gould's fuscus."),

    dict(plate_page=226, text_page=227, english="Green Sandpiper", latin="Totanus ochropus", author=None,
         modern_en="Green Sandpiper", modern_latin="Tringa ochropus", status="reclassified",
         resolved_by="Moved from Totanus into Tringa; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=230, text_page=231, english="Wood-Sandpiper", latin="Totanus glareola", author=None,
         modern_en="Wood Sandpiper", modern_latin="Tringa glareola", status="reclassified",
         resolved_by="Moved from Totanus into Tringa; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=234, text_page=235, english="Summer Snipe", latin="Actitis hypoleucos", author=None,
         modern_en="Common Sandpiper", modern_latin="Actitis hypoleucos", status="stable",
         note="Gould's English name (\"Summer Snipe\") has simply fallen out of use in favour of Common Sandpiper; the scientific name he gives is already the modern one."),

    dict(plate_page=238, text_page=239, english="Spotted Sandpiper", latin="Actitis macularius", author=None,
         modern_en="Spotted Sandpiper", modern_latin="Actitis macularius", status="stable"),

    dict(plate_page=242, text_page=243, english="Turnstone", latin="Strepsilas interpres", author=None,
         modern_en="Ruddy Turnstone", modern_latin="Arenaria interpres", status="reclassified",
         resolved_by="Moved from Strepsilas into Arenaria; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=246, text_page=247, english="Ruff", latin="Machetes pugnax", author=None,
         modern_en="Ruff", modern_latin="Calidris pugnax", status="reclassified",
         resolved_by="Moved from Machetes (and later, for much of the 20th century, its own genus Philomachus) into Calidris, following DNA evidence that the sandpipers form one closely related group with no clean dividing lines between the old genera. This plate shows the adult male and female (Reeve); plate 249 (same account) shows the plumage of the first autumn."),
    dict(plate_page=249, text_page=None, shares_with=246, plate_note="Ruff and Reeve in the plumage of the first autumn",
         english="Ruff", latin="Machetes pugnax", author=None,
         modern_en="Ruff", modern_latin="Calidris pugnax", status="reclassified"),

    dict(plate_page=252, text_page=253, english="Bartram's Sandpiper", latin="Actiturus bartramius", author=None,
         modern_en="Upland Sandpiper", modern_latin="Bartramia longicauda", status="reclassified",
         resolved_by="Moved from Actiturus into its own genus Bartramia (named, as was the old epithet, for the naturalist William Bartram), with the epithet changed to longicauda."),

    dict(plate_page=256, text_page=257, english="Buff-breasted Sandpiper", latin="Tryngites rufescens", author=None,
         modern_en="Buff-breasted Sandpiper", modern_latin="Calidris subruficollis", status="reclassified",
         resolved_by="Moved from Tryngites into Calidris, with the epithet changed to subruficollis."),

    dict(plate_page=260, text_page=261, english="Knot", latin="Tringa canutus", author="Linn.",
         modern_en="Red Knot", modern_latin="Calidris canutus", status="reclassified",
         resolved_by="Moved from Tringa into Calidris; the species epithet -- traditionally said to honour King Canute -- was already correct in Gould's own heading."),

    dict(plate_page=264, text_page=265, english="Sanderling", latin="Calidris arenaria", author=None,
         modern_en="Sanderling", modern_latin="Calidris alba", status="reclassified",
         resolved_by="Genus unchanged -- Gould's own heading already used Calidris, a genus he applied narrowly to just this one bird, long before molecular work in the 2000s showed that Calidris should be expanded to absorb Tringa canutus, Machetes pugnax, and most of the other small sandpipers in this volume (see the Knot, Ruff, and stints above). The species epithet itself was standardised to alba, replacing arenaria."),

    dict(plate_page=268, text_page=269, english="Pectoral Sandpiper", latin="Limnocinclus pectoralis", author=None,
         modern_en="Pectoral Sandpiper", modern_latin="Calidris melanotos", status="reclassified",
         resolved_by="Moved from Limnocinclus into Calidris, with the epithet changed to melanotos."),

    dict(plate_page=272, text_page=273, english="Curlew Sandpiper", latin="Ancylocheilus subarquata", author=None,
         modern_en="Curlew Sandpiper", modern_latin="Calidris ferruginea", status="reclassified",
         resolved_by="Moved from Ancylocheilus into Calidris, with the epithet changed to ferruginea."),

    dict(plate_page=276, text_page=277, english="Dunlin", latin="Pelidna cinclus", author=None,
         modern_en="Dunlin", modern_latin="Calidris alpina", status="reclassified",
         resolved_by="Moved from Pelidna into Calidris, with the epithet changed to alpina. This plate shows the summer plumage; plate 279 (same account) shows the winter plumage.",
         note="Gould's own text is visibly uncertain here -- his synonymy leads with a tentative \"Tringa Schinzii, Brehm?\", one of several 19th-century names later absorbed into the single, highly variable species Calidris alpina."),
    dict(plate_page=279, text_page=None, shares_with=276, plate_note="Winter plumage",
         english="Dunlin", latin="Pelidna cinclus", author=None,
         modern_en="Dunlin", modern_latin="Calidris alpina", status="reclassified"),

    dict(plate_page=282, text_page=283, english="Bonaparte's Sandpiper", latin="Pelidna Bonapartei", author=None,
         modern_en="White-rumped Sandpiper", modern_latin="Calidris fuscicollis", status="reclassified",
         resolved_by="Moved from Pelidna into Calidris, with the epithet changed to fuscicollis; the English name has also shifted from honouring Charles Lucien Bonaparte to describing the bird's white rump."),

    dict(plate_page=286, text_page=287, english="Little Stint", latin="Actodromas minuta", author=None,
         modern_en="Little Stint", modern_latin="Calidris minuta", status="reclassified",
         resolved_by="Moved from Actodromas into Calidris; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=290, text_page=291, english="Temminck's Stint", latin="Leimonites Temminckii", author=None,
         modern_en="Temminck's Stint", modern_latin="Calidris temminckii", status="reclassified",
         resolved_by="Moved from Leimonites into Calidris; the species epithet was already correct (bar capitalisation) in Gould's own heading."),

    dict(plate_page=294, text_page=295, english="Purple Sandpiper", latin="Arquatella maritima", author=None,
         modern_en="Purple Sandpiper", modern_latin="Calidris maritima", status="reclassified",
         resolved_by="Moved from Arquatella into Calidris; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=298, text_page=299, english="Broad-billed Sandpiper", latin="Limicola pygmaea", author=None,
         modern_en="Broad-billed Sandpiper", modern_latin="Calidris falcinellus", status="contested",
         note="Long placed in its own genus Limicola (under the older epithet falcinellus, not Gould's pygmaea, which is now treated as a synonym); a 2021 genomic study recommended folding Limicola into Calidris along with the other sandpipers, and some checklists have adopted this while others still keep Limicola falcinellus -- so both generic placements are current usage as of this writing."),

    dict(plate_page=302, text_page=303, english="Red-breasted or Brown Snipe", latin="Macrorhamphus griseus", author=None,
         modern_en="Short-billed Dowitcher", modern_latin="Limnodromus griseus", status="reclassified",
         resolved_by="Moved from Macrorhamphus into Limnodromus, the genus now used for both dowitcher species; the species epithet was already correct in Gould's own heading."),

    dict(plate_page=306, text_page=307, english="Woodcock", latin="Scolopax rusticola", author="Linn.",
         modern_en="Eurasian Woodcock", modern_latin="Scolopax rusticola", status="stable",
         note="Gould's account of the Woodcock runs unusually long (several extra pages of shooting statistics and wing-measurement tables), which is why the gap to the next plate is wider than the volume's usual four-page rhythm -- not a sign of any missing plate."),

    dict(plate_page=312, text_page=313, english="Great Snipe", latin="Gallinago major", author=None,
         modern_en="Great Snipe", modern_latin="Gallinago media", status="reclassified",
         resolved_by="Epithet standardised to media, replacing Gould's major; the genus was already correct in Gould's own heading."),

    dict(plate_page=316, text_page=317, english="Common Snipe", latin="Gallinago scolopacina", author=None,
         modern_en="Common Snipe", modern_latin="Gallinago gallinago", status="reclassified",
         resolved_by="Epithet standardised to the tautonym gallinago, replacing Gould's scolopacina; the genus was already correct in Gould's own heading."),

    dict(plate_page=320, text_page=321, english="Jack Snipe", latin="Lymnocryptes gallinula", author=None,
         modern_en="Jack Snipe", modern_latin="Lymnocryptes minimus", status="reclassified",
         resolved_by="Epithet standardised to minimus, replacing Gould's gallinula; the genus was already correct in Gould's own heading."),

    dict(plate_page=324, text_page=325, english="Grey Phalarope", latin="Phalaropus fulicarius", author=None,
         modern_en="Red Phalarope", modern_latin="Phalaropus fulicarius", status="stable",
         note="Same scientific name Gould used; only the preferred English name has drifted, from Grey Phalarope (its non-breeding look, the one usually seen in Britain) to Red Phalarope (its striking breeding plumage, shown on this very plate) in most modern usage. This plate shows the summer plumage; plate 327 (same account) shows the winter plumage."),
    dict(plate_page=327, text_page=None, shares_with=324, plate_note="Winter plumage",
         english="Grey Phalarope", latin="Phalaropus fulicarius", author=None,
         modern_en="Red Phalarope", modern_latin="Phalaropus fulicarius", status="stable"),

    dict(plate_page=330, text_page=331, english="Red-necked Phalarope", latin="Lobipes hyperboreus", author=None,
         modern_en="Red-necked Phalarope", modern_latin="Phalaropus lobatus", status="reclassified",
         resolved_by="Moved from the split-off genus Lobipes back into Phalaropus, with the epithet changed to lobatus."),

    dict(plate_page=334, text_page=335, english="Coot", latin="Fulica atra", author=None,
         modern_en="Eurasian Coot", modern_latin="Fulica atra", status="stable"),

    dict(plate_page=338, text_page=339, english="Moorhen", latin="Gallinula chloropus", author=None,
         modern_en="Common Moorhen", modern_latin="Gallinula chloropus", status="stable"),

    dict(plate_page=342, text_page=343, english="Water-Rail", latin="Rallus aquaticus", author="Linn.",
         modern_en="Water Rail", modern_latin="Rallus aquaticus", status="stable"),

    dict(plate_page=346, text_page=347, english="Land-Rail, or Corn-Crake", latin="Crex pratensis", author=None,
         modern_en="Corn Crake", modern_latin="Crex crex", status="reclassified",
         resolved_by="Epithet standardised to the tautonym crex, replacing Gould's pratensis."),

    dict(plate_page=350, text_page=351, english="Spotted Crake", latin="Porzana maruetta", author=None,
         modern_en="Spotted Crake", modern_latin="Porzana porzana", status="reclassified",
         resolved_by="Epithet standardised to the tautonym porzana, replacing Gould's maruetta."),

    dict(plate_page=354, text_page=355, english="Baillon's Crake", latin="Porzana pygmaea", author=None,
         modern_en="Baillon's Crake", modern_latin="Zapornia pusilla", status="contested",
         note="Gould's own epithet pygmaea has long been treated as a synonym of the older pusilla; more recently a molecular study split the old genus Porzana apart, moving most of its small crakes -- including this one -- into a revived genus Zapornia, though many field guides and checklists still list it as Porzana pusilla."),

    dict(plate_page=358, text_page=359, english="Olivaceous Crake", latin="Porzana minuta", author=None,
         modern_en="Little Crake", modern_latin="Zapornia parva", status="reclassified",
         resolved_by="Moved, along with Baillon's Crake above, from Porzana into the revived genus Zapornia, with the epithet standardised to parva; the English name has also shifted from Gould's \"Olivaceous Crake\" to the now-standard \"Little Crake\"."),
]

assert len(SPECIES_GB_V4) == 90
