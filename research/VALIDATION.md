# Validation record — 22 October 2026

This record separates implementation checks from scientific evidence. It does
not claim independent reproduction or peer review of every cited research paper.

## Scientific and bibliographic review

- Three parallel primary-literature investigations produced thermalization,
  transport, and information evidence ledgers. The book organizes their material
  by physical questions rather than researchers.
- Independent cross-review checked representative derivations, signs, factors,
  ensemble conventions, orders of limits, and claims about universality. Repairs
  include number-versus-spin current conventions, finite-size return-amplitude
  zeros, the limits of entropy-based MPS bounds, membrane-tension dimensions,
  Hermitian bath-coupling conventions, and local versus global purification.
- 153 source records consolidate to **146 distinct papers/reviews** by DOI or
  arXiv identity. All 17 core records were enriched with verified journal fields;
  publication overrides prevent stale arXiv export years from returning.
- The link audit requested 265 distinct source/DOI endpoints. No 404/410 response
  was observed. Fifteen publisher endpoints restricted automated access; two
  transient failures were subsequently opened successfully. This is not a claim
  that every publisher permits automated retrieval. See `LINK-AUDIT.md`.

## Numerical execution

`make data` completed successfully after integration, running all six generators:
core quenches, thermalization/localization/Floquet examples, transport/dual gates,
gauge protection, MPS compression, and monitored circuits. All asserted analytic,
normalization, conservation, positivity, algebra, reference-error, and
truncation/splitting-order checks passed. These checks establish the stated small
models and approximations, not thermodynamic phases. See `NUMERICAL-REVIEW.md`
and the parameter records in `data/`.

`make figures` completed successfully using the three pinned Python plotting
scripts. Julia performs quantum evolution; Python plots saved data and original
conceptual diagrams. The project includes 21 CSV files and 23 PNG/vector-PDF
figure pairs. The dense MPS construction is explicitly an educational reference,
not a scalable time-evolution library.

## Rendered web edition

- Quarto rendered all **38 pages** (32 scientific chapters plus front matter,
  source map, references, and appendices).
- The source audit passed: all citations, labeled references, and linked assets
  resolve. The current source contains 274 labeled equations.
- Rendered-file checks passed for local navigation, target anchors, image/script
  paths, citation targets, and the combined-PDF download target.
- An isolated headless Chrome tested six representative served pages, MathJax,
  image loading, light/dark layouts, and actual slider/circuit outputs. Browser
  circuit limits p=0 and p=1 passed. No application page errors were observed.
- A separate 390-pixel viewport audit checked **every page**, with no document
  overflow and no MathJax error nodes. Long display equations scroll within their
  own containers. This is a viewport test, not physical testing on every browser
  or mobile device. Machine-readable reports accompany this record.

## Combined PDF

LuaLaTeX compiled the complete book. Representative pages were rasterized and
inspected for equations, headings, figures, captions, exercises, tables, and
references. Scientific figures use their vector originals through a Pandoc
filter. An all-page text-bounds check found no text extending to the paper edge.
The final edition has 208 A4 pages. Contents spacing and source-table column
widths were corrected and rechecked after the last render.

## Publication

The GitHub repository is public and GitHub Pages is configured for a workflow
build. The publication workflow renders both editions from the committed sources,
audits the output, then deploys it. The final deployment result and public HTTP
checks will be added once completed.
