# Priority Audit (preliminary)

## Searches performed on 2026-09-02

Queries included:

- `"tilde f_p" chordal graphs convolution`
- `"labeled chordal graphs" "polynomial multiplication"`
- `"Counting and Sampling Labeled Chordal Graphs" citations`
- `"faster" "chordal graphs" exact counting`
- direct searches for the ESA 2023 paper, its arXiv record, the authors' repository, the 2025 dissertation, STACS 2025, and Sun 2026

Search surfaces reached: arXiv, DBLP, Crossref-linked Dagstuhl metadata, eScholarship, GitHub, and the cited-paper pages exposed by those services. Google Scholar, MathSciNet, and zbMATH were not reliably accessible through the current search interface and remain uncertainty items.

## Closest prior work

The authors' 2025 dissertation explicitly states the open problem of a substantially faster exact counter or uniform sampler after recording `O(n^7)` arithmetic operations and `O(n^9 log n)` RAM time. However, the same dissertation already contains the `r=x'+ell'` regrouping and six-argument `h` helper in §2.5.4, with the resulting `O(n^7)` analysis. Therefore that regrouping is prior art.

ESA 2023 supplies the labeled DP and `O(n^7)` bound; STACS 2025 addresses unlabeled sampling and automorphism-conditioned labeled counting; Sun 2026 addresses equivariant/unlabeled enumeration. None of the records inspected states the proposed EGF/FPS acceleration of the labeled recurrence.

## Overlap matrix

| Work | Labeled exact count | `r`/`h` regrouping | EGF/FPS acceleration | Uniform labeled sampler |
|---|---:|---:|---:|---:|
| ESA 2023 | yes | no in conference text | no | yes |
| Hébert-Johnson dissertation 2025 | yes | yes | no | yes |
| STACS 2025 | automorphism-conditioned subproblem | inherited/extended | no | related unlabeled sampler |
| Sun 2026 | equivariant/unlabeled | builds on labeled DP | no identified | no |
| present proposal | intended | not novel by itself | intended | intended |

## Provisional novelty conclusion

The only plausible contribution is exposing additional convolution/ODE structure beyond the dissertation's `h` helper and proving a faster total bound. Priority is **not established**: the required exhaustive database search and author inquiry remain outstanding, and the actual research note containing the proposed formulas was not supplied in the referenced file.

No “first” or “world's first” language is authorized.

## Additional search pass on 2026-09-03

The attempted direct OpenAlex, Semantic Scholar, Crossref, and arXiv API URLs were rejected by the web interface as unsafe URLs, so they provide no evidence and are not treated as searched records. Compact indexed searches did return the ESA/arXiv record, Dagstuhl metadata, DBLP, and the dissertation again. A query for `"formal power series" chordal graphs counting` returned generic formal-power-series material and unrelated chord-diagram work, but no candidate paper claiming the proposed recurrence acceleration.

This pass therefore strengthens record discovery only; it does not establish an exhaustive negative result. The overlap matrix and provisional conclusion remain unchanged. In particular, the dissertation's prior `r`/`h` regrouping is still the closest directly documented overlap, while EGF/FPS acceleration remains an unverified novelty claim pending broader bibliographic coverage and author inquiry.

## Sun 2026 follow-up

The newly required Sun investigation is recorded in `research/SUN2026_AUDIT.md`. His paper and cached repository README identify `assemble.py` as the labeled HLV base-case implementation and identify the new work as equivariant/unlabeled divisor-bundle enumeration. The repository source and commit history were not retrievable from the current GitHub endpoint, so no code-level negative claim is made. OEIS A058862 records Sun's 2026 extensions but contains no EGF/FPS acceleration note. Sun is therefore contemporary related work, not demonstrated duplicate priority.
