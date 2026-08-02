# Volume III — Tile Component Checklist

*A verification pass over all 96 species tiles in Volume III (Insessores, cont.), run directly against the built `app.html`, not just the source data — so this reflects what actually renders.*

## What prompted this

Jan flagged that Cole Tit and Marsh Tit (plates 164–165) were missing an authority citation, and asked me to check the plate print itself ("Linn."). That led to discovering the entire Volume III species file had never had an `author` field populated — 96 species, all missing it. This checklist covers the fix and a full component-by-component check of every tile in the volume.

## 1. Authority citations — 96/96 checked, 92 added, 4 correctly left blank

Every one of the 96 species was checked directly against the original 1832–37 plate text (re-extracted from the source PDF, cross-checked against the volume's own table of contents where the plate print was too degraded to read). Citations use the same abbreviated form Gould's own plates print (e.g. "Linn.", "Temm.", "Pall.") — matching the convention already used in Volumes I, IV and V.

- **92 species** now carry a sourced authority, taken directly from the plate or table of contents (e.g. Cole Tit and Marsh Tit both confirmed as "Linn.").
- **4 species were left blank on purpose**: Doubtful Sparrow, Citril Finch, Pine Grosbeak's synonym plate ("Siberian Grosbeak"), and Rosy Grosbeak. In all four cases, Gould's own plate genuinely printed no author next to the binomial — leaving these blank is the honest option rather than guessing.
- Two cases where the table of contents and the plate text disagreed were resolved in favour of the plate's own species-level citation (Penduline Tit: plate says "Boie.", not the contents' "Vig."; American Cuckoo: plate says "Bonap.", not the contents' "Vieill.", which turned out to be citing the genus author, not the species author).

## 2. Every other tile component — checked against the live HTML

| Component | Status |
|---|---|
| Plate number | 96/96 present |
| English title | 96/96 present |
| Latin binomial line | 96/96 present |
| Latin-word etymology tooltips | 96/96 present |
| Author citation | 96/96 present (92 sourced, 4 honestly blank — see above) |
| DE/FR names table | 96/96 present |
| Family/genus/artist tag chips | 96/96 present |
| Artist credit line | 96/96 present |
| Card image + click-to-zoom hi-res | 96/96 present |
| Genus description ("Gen. Char.") | 91/96 present |
| Gould's original written account | 93/96 present |

## 3. Pre-existing gaps found along the way (not part of the original ask, left untouched)

Seven species are missing their genus description and/or Gould's original account text — this is a separate, older gap in the data (not something I introduced, and not something Jan asked me to fix this round):

- **Snow Bunting** (plate 180) — missing both.
- **Coal Tit** and **House Sparrow** — missing Gould's account only. Both share a plate with another species (Marsh Tit; Tree Sparrow), and the original OCR capture of that combined plate text appears to have been dropped entirely rather than mis-split.
- **Lapland Longspur** (Lark-heeled Bunting), **Common Rosefinch** (Scarlet Grosbeak), **Trumpeter Finch** (Vinous Grosbeak), and the "Identity uncertain" Rosy Grosbeak plate — missing the genus description box, most likely because their genus isn't yet mapped in the separate genus-description lookup table.

Happy to take these on as a follow-up if useful — flagging now rather than folding it silently into "done."

## Sources

- Original plate text: *The Birds of Europe*, Vol. III (John Gould, 1832–37) — re-extracted directly from the source PDF via `pdftotext -layout`, cross-checked against the volume's own table of contents.
