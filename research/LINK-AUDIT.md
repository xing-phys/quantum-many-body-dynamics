# Primary citation link and publication-metadata audit

Audit date: **22 October 2026**. Scope: the 153 entries in `core.bib` (17),
`thermal.bib` (54), `transport.bib` (39), and `information.bib` (43), before
canonical deduplication into `all.bib`. This is a link/identity/metadata audit,
not a new independent verification of every scientific claim in those papers.

## Method and exact limits of the result

`research/check_citation_links.py` parsed the source bibliographies and issued
ordinary HTTP GET requests to each distinct `url` and DOI resolver address,
following redirects. It captured status codes and available primary-page citation
metadata. The initial result covered **265 distinct endpoints**:

| Outcome | Count | Interpretation |
|---|---:|---|
| Successful HTTP response | 248 | Endpoint accessible to this automated request; metadata checked where present |
| HTTP 403 | 15 | Publisher access/bot restriction; **not evidence of a broken link** |
| Read timeout | 1 | Inconclusive automated request |
| HTTP 500 | 1 | Transient server failure; **not evidence of a broken link** |
| HTTP 404 or 410 | 0 | No not-found/gone responses observed |

The timeout (`arXiv:1508.03344`, Khemani et al.) and transient 500
(`arXiv:2604.11085`, Fu et al.) were subsequently opened successfully with the
primary-source browser tool and their identities checked. The initial raw
outcomes remain preserved rather than being silently overwritten.

**Do not describe this as “every link verified working.”** Some publisher
endpoints remain inaccessible to automation. Most have an accessible primary
arXiv alternative. A DOI resolver redirect to a publisher that returns 403 is
different from an unregistered DOI or a 404.

Artifacts:

- `research/citation-link-results.json`: source snapshot, 265 URL outcomes,
  extracted metadata, and manual-follow-up notes. Large incidental reference
  lists and author affiliations were removed from the stored metadata.
- `research/core-doi-metadata.json`: DOI registration metadata for all 17 core
  publications, used to repair their publication fields.
- `references/core.overrides.json`: reviewed metadata overrides, applied by
  `scripts/fetch_core_bib.py` after future arXiv BibTeX refreshes.

## Repairs implemented in the core bibliography

All 17 core records were exported from arXiv as `@misc`; all are now `@article`
with verified published title, journal, volume, issue, pages or article number,
and publication year. Their arXiv identifiers and links remain present. DOI
registration metadata was obtained for every entry; accessible publisher HTML
was cross-checked against it. The PNAS pagination absent from its DOI registration
was checked in the publisher-deposited [full article in PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC5441767/).

| Key | Published venue and pagination | Year | Material correction |
|---|---|---:|---|
| `page1993average` | Physical Review Letters 71(9), 1291–1294 | 1993 | Added publication fields |
| `popescu2006foundations` | Nature Physics 2(11), 754–758 | 2006 | Published title is **Entanglement and the foundations of statistical mechanics**, shorter than the preprint title |
| `bravyi2006locality` | Physical Review Letters 97(5), 050401 | 2006 | Added publication fields |
| `vidal2004tebd` | Physical Review Letters 93(4), 040502 | **2004** | Corrected stale arXiv year 2003; publisher date 19 July 2004 |
| `schollwock2011mps` | Annals of Physics 326(1), 96–192 | 2011 | Added publication fields; restored author spelling Schollwöck |
| `haegeman2016tdvp` | Physical Review B 94(16), 165116 | **2016** | Corrected year 2015; publisher date 10 October 2016 |
| `dziarmaga2005ising` | Physical Review Letters 95(24), 245701 | 2005 | Replaced preprint title with published **Dynamics of a Quantum Phase Transition: Exact Solution of the Quantum Ising Model** |
| `heyl2013dqpt` | Physical Review Letters 110(13), 135704 | 2013 | Added publication fields and published title punctuation |
| `heyl2018review` | Reports on Progress in Physics 81(5), 054001 | 2018 | Added publication fields |
| `tran2020hierarchy` | Physical Review X 10(3), 031009 | **2020** | Corrected year 2022; publisher date 13 July 2020 |
| `kaufman2016thermalization` | Science 353(6301), 794–800 | 2016 | Added publication fields |
| `cheneau2012lightcone` | Nature 481(7382), 484–487 | 2012 | Added publication fields |
| `bernien2017simulator` | Nature 551(7682), 579–584 | 2017 | Added publication fields |
| `brydges2019renyi` | Science 364(6437), 260–263 | 2019 | Published title explicitly includes **Rényi** |
| `chen2026gauge` | Journal of High Energy Physics 2026(10), 137 | **2026** | Published on **12 October 2026**, within the cutoff; no longer only a preprint |
| `berges2017fixedpoints` | Physical Review D 95(3), 036016 | 2017 | Added publication fields |
| `sels2017counterdiabatic` | Proceedings of the National Academy of Sciences 114(20), E3909–E3916 | **2017** | Corrected preprint year 2016 and used published “counterdiabatic” spelling |

The override mechanism was tested offline for every entry, including replacement
of nested-brace titles, preservation of URLs and unrelated fields, conversion of
entry type, and completeness of the resulting 17 article records. The network
refresh itself was not rerun unnecessarily. No chapters, Quarto configuration,
or build outputs were changed in this audit.

## Other concrete metadata repairs for integration

Two `information.bib` entries use preprint titles while supplying journal
publication details. Prefer these publisher titles for the article records:

| Key | Current title | Published title verified from DOI landing-page metadata |
|---|---|---|
| `info-noel2022` | Observation of measurement-induced quantum phases in a trapped-ion quantum computer | **Measurement-induced quantum phases realized in a trapped-ion quantum computer**; [Nature Physics DOI](https://doi.org/10.1038/s41567-022-01619-7) |
| `info-maldacena2016syk` | Comments on the Sachdev-Ye-Kitaev model | **Remarks on the Sachdev-Ye-Kitaev model**; [Physical Review D DOI](https://doi.org/10.1103/PhysRevD.94.106002) |

These are title changes between preprint and publication, **not wrong-paper
links**. The root integration agent was notified; only the core repairs were
authorized for direct implementation in this pass.

Other title-comparison flags were harmless or already appropriate:

- `turner2018scars`: arXiv title *Quantum many-body scars* differs from the
  published *Weak ergodicity breaking from quantum many-body scars*. The
  bibliography already uses the published title correctly.
- `info-verstraete2009`: the preprint has a longer title mentioning quantum phase
  transitions; the bibliography already uses the correct Nature Physics title.
- Bethe's 1931 publisher title is shortened in landing-page metadata; the full
  bibliographic subtitle is consistent with the cited paper.
- Math/HTML markup in the Prosen XXZ title caused a raw string-comparison false
  positive; the DOI and paper identity match.
- Expanded “many-body localization” versus “MBL,” and expanded
  “Kardar-Parisi-Zhang” versus “KPZ,” are title-form differences that do not
  change paper identity. Prefer publisher forms when polishing canonical data.

## A known metadata trap: Knill–Laflamme

The arXiv record `quant-ph/9604034` presently lists an inconsistent related
journal DOI, `10.1103/PhysRevLett.84.2525`. Do **not** import that field over the
correct entry. The primary [PRA publication](https://doi.org/10.1103/PhysRevA.55.900)
confirms *Theory of quantum error-correcting codes*, Knill and Laflamme,
Physical Review A 55, 900 (1997). `info-knill1997` already uses this correct
PRA DOI. The automated journal-reference extractor's original generic `jref`
cell also selected a report number in this record and the Chen record; those
fields in the raw snapshot carry an explicit extraction note. The script now
targets the journal-reference row specifically.

## 2026 status and identities checked

There were **19 entries labeled 2026** in the source snapshot. Their titles,
arXiv identifiers where present, and publication/preprint distinctions were
checked using primary records; DOI-only information entries were cross-checked
with publisher and DOI registration metadata.

Published records consistent with the cutoff and current bibliography:

- Serbyn et al., PRX 16, 031042, DOI `10.1103/4zs8-7kf4`;
- Bertini, Claeys and Prosen, RMP 98, 025001, DOI `10.1103/yx73-dk86`;
- Scopa et al., PRL 137, 113404, DOI `10.1103/yfjc-r69d`;
- Tan and Brouwer, PRB 114, 074308, DOI `10.1103/p5d4-dmj6`;
- Liu, Ippoliti and Ho, PRL 136, 100404, DOI `10.1103/mjgs-y2z9`, published
  12 March 2026;
- Sherry and Roy, PRB 113, 174309, DOI `10.1103/x397-3nk5`, published
  18 May 2026;
- Du et al., Nature Communications 17, 8052, DOI
  `10.1038/s41467-026-74924-x`, published 27 June 2026;
- Chen et al., JHEP 2026(10), 137, published 12 October 2026 (repaired above).

The remaining eleven 2026 records are appropriately retained as preprints:
Desaules `2605.05297`; Petrova `2607.15132`; Cruickshank `2606.31667`;
Fu `2604.11085`; Goss `2605.14293`; Cemin `2610.12597`;
Anand `2602.15933`; Santra `2603.02158`; McCulloch `2604.27074`;
Mark `2609.30248`; Feng `2606.08756`.
The most recent cited submission, Cemin et al., is dated 8 October 2026;
the Mark et al. review is dated 24 September 2026. The revised title of Tan
and Brouwer and the “KPZ-like” wording of Anand et al. match the current
primary records rather than stale search-result titles.

No DOI/URL paper-identity mismatch was established. The identified substantive
problems were stale publication years, omitted publication fields, two
preprint-versus-published title choices outside core, and a bad related DOI
inside an upstream arXiv record that the bibliography itself already avoids.
