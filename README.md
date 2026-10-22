# Quantum Many-Body Dynamics and Quantum Information

A Quarto research textbook connecting undergraduate quantum mechanics to modern
many-body dynamics and quantum information. The teaching sequence is documented
in [research/OUTLINE.md](research/OUTLINE.md); source checks are in `research/`.

Published book: <https://xing-phys.github.io/quantum-many-body-dynamics/>

This edition has 32 scientific chapters, 146 selected sources, 24 original
figure/diagram pairs, 21 numerical datasets, and three browser laboratories.
The literature cutoff is 22 October 2026.

## Build and reproduce

Quarto 1.10.18 and LuaLaTeX build the web book and a combined PDF. Julia 1.12.6
generated the numerical data using only standard libraries. Book rendering uses
checked-in data and does not require executing code or fetching scientific data.

```sh
make data figures check
quarto render
python3 scripts/audit.py --rendered
quarto preview --no-browser --port 4242
```

HTML: `_site/index.html`. PDF: `_site/quantum-many-body-dynamics.pdf`. The preview
prints its URL. Figures retain PDF vector originals and PNG counterparts.
Diagrams are pre-rendered, so PDF builds do not require browser conversion.
Browser labs require no account or server computation.

## Organization and updating

- Root `.qmd` files are chapters. `_quarto.yml` defines six parts and appendices.
- `references/` holds verified BibTeX; `research/` records investigation date,
  evidence, publication status, and interpretive limits.
- `numerics/` contains Julia calculations and invariant checks; `data/` contains
  CSV outputs and provenance; `scripts/` contains plotting and output audits.
- `demos/` contains browser experiments with explicit mathematical models.
- Keep `assets/macros.sty` and `assets/mathjax-config.html` equivalent. Use native
  Quarto equation labels and cross-references.

The selected literature was verified through 22 October 2026. Paper bridges
explain motivations, methods, limitations, and possible reproductions. Preprints
retain their status. The bibliography is a curated path, not an exhaustive
database. Worked exercise solutions are included in the chapters.

AI-assisted drafting and computation are part of the production history. The
repository exposes derivations, sources, assumptions, and checks for independent
scientific scrutiny and correction.

For updates, add sources to the evidence ledger before incorporating claims.
Verify metadata and status; reproduce a well-defined observable before claiming
paper reproduction. Update the coverage map and `CHANGELOG.md`, run relevant
numerics, and render both formats. GitHub Actions publishes from `main`.
