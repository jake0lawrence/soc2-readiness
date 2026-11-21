# SOC 2 Readiness for a One-Person Platform

What one operator can prove, what one operator cannot, and why a control that was built but not kept running is the difference between a Type I and a Type II. The public mirror of the research piece at [jakelawrence.xyz/research/soc2-readiness](https://jakelawrence.xyz/research/soc2-readiness): a SOC 2 readiness self-assessment of a one-person platform against the AICPA Trust Services Criteria. Version 1.1.3 is the newest, published 2026-11-21.

> **Not an audit.** This is a self-assessment, not an audit. Only an independent CPA firm can issue a SOC 2 report, and this platform has not engaged one. Nothing on this page claims compliance.

Every file here is a frozen release, exactly as the site publishes it, with its checksums. Nothing in this repository is written by hand: it is generated from the site on each release, so the two cannot drift. A correction is made on the site and arrives here as a new version.

| | |
|---|---|
| The live page | https://jakelawrence.xyz/research/soc2-readiness |
| The newest release's files | https://jakelawrence.xyz/downloads/soc2-readiness/v1.1.3/ |
| One permanent link per version | `https://jakelawrence.xyz/research/soc2-readiness/v/<version>` |
| License | CC BY 4.0 ([LICENSE.md](LICENSE.md)) |
| Cite | [CITATION.cff](CITATION.cff) (GitHub's "Cite this repository" reads it) |

## What it is

- **23 controls** across the Trust Services Categories, each graded twice: for design (what a Type I report tests, at one point in time) and for operation (what a Type II report tests, across a period).
- **Design:** 14 ready, 7 partial, 2 gap. **Operating:** 9 ready, 9 partial, 5 gap. **8** controls grade lower for operation than for design.
- **`worksheet.md`** is the readiness worksheet, for another operator to fill in with their own evidence. `controls.csv` and `controls.json` hold every control with both grades. `crosswalk.csv` maps them to two outside frameworks.

The crosswalk (from 1.1.3) quotes the NIST Cybersecurity Framework 2.0 outcomes verbatim (a U.S. Government work, not subject to copyright, 17 U.S.C. 105) and names CIS Critical Security Controls v8 safeguards by title only, read from CIS's Controls Assessment Specification. CIS keeps its own terms.

The data files name the publisher's own code as evidence for each control, by path. Those paths are named, not linked: the code they point into is not public.

## Versions

Each folder under `downloads/soc2-readiness/` is one frozen version, and `latest.json` names the newest. A released version is never altered.

| Version | Published | Contents | Frozen page |
|---|---|---|---|
| [1.1.3](downloads/soc2-readiness/v1.1.3) | 2026-11-21 | 23 controls, 8 slip a grade | [https://jakelawrence.xyz/research/soc2-readiness/v/1.1.3](https://jakelawrence.xyz/research/soc2-readiness/v/1.1.3) |
| [1.1.2](downloads/soc2-readiness/v1.1.2) | 2026-11-20 | 23 controls, 8 slip a grade | [https://jakelawrence.xyz/research/soc2-readiness/v/1.1.2](https://jakelawrence.xyz/research/soc2-readiness/v/1.1.2) |

Files in each version: `controls.json`, `controls.csv`, `worksheet.md`, `crosswalk.csv`, `CITATION.cff`, `README.md`, `manifest.json`, `SHA256SUMS`. The site's HTML browse page for each version is left out; the files are the release.

## Check it

```
python3 scripts/verify.py
```

checks every file of every version against its `SHA256SUMS` and `manifest.json`, with nothing but the Python standard library. Or, inside one version's folder, `sha256sum -c SHA256SUMS`. The check runs on every push ([.github/workflows/verify.yml](.github/workflows/verify.yml)).

## Cite

Archived on Zenodo with a DOI:

- **All versions** (always the newest): [https://doi.org/10.5281/zenodo.24427334](https://doi.org/10.5281/zenodo.24427334)
- **1.1.3:** [https://doi.org/10.5281/zenodo.24427335](https://doi.org/10.5281/zenodo.24427335)

Cite the version you used by its own DOI.

Version 1.1.3, as the release gives it:

```
Lawrence, J. (2026). SOC 2 Readiness for a One-Person Platform (version 1.1.3) [Data set]. https://jakelawrence.xyz/research/soc2-readiness. CC BY 4.0.
```

[CITATION.cff](CITATION.cff) is the same in machine-readable form, for version 1.1.3. Each version's own `CITATION.cff` is in its folder. The release files carry `doi: null` by design, since a version is frozen before its DOI can exist; the DOI is recorded in the site's Zenodo registry and in this README and `CITATION.cff`.

## What changed, version by version

From the 1.1.3 release's own README:

- 1.1.3 (2026-11-21): Adds a crosswalk: each of the 23 controls names where it falls in the NIST Cybersecurity Framework 2.0, quoting NIST's outcome text, and in the CIS Critical Security Controls v8 by safeguard title, with full or partial fit, a confidence and the reason. Controls with no honest fit say why. Grades are unchanged and were last read on November 20, which stays the as-of date.
- 1.1.2 (2026-11-20): All 23 controls re-read against the run history, grades unchanged. Detection: the gap said the health check had stopped, which stopped being true on October 8; the gap now names what still keeps it partial (how long an outage can go unheard, and one person on the receiving end). Backups: six weekly restore tests have passed since the schedule came back (October 11 to November 15), so the gap now counts them instead of saying there are none. The page no longer says a test fails at the review date; that test was retired on October 16.
- 1.1.1 (2026-10-31): All 23 controls re-read, grades unchanged. Health check cadence: the agent tick that runs the site-health sweep moved from hourly to every three hours (an Actions spend cut), so the status page now reads a check up to three hours old; the evidence line follows the workflow.
- 1.1.0 (2026-10-08): All 23 controls regraded after the July 29 schedule freeze was lifted: 43 scheduled jobs run again. Health check regraded to ready; backups and retention sweeps from gap to partial, because a restored schedule is not yet a period of evidence.
- 1.0.0 (2026-09-23): First assessment: 23 controls across all five Trust Services Categories, graded for design and for operation.

## License

Creative Commons Attribution 4.0 International (CC BY 4.0). See [LICENSE.md](LICENSE.md). Copy, adapt and reuse it, including commercially, with attribution.

## Corrections

Open an issue; see [CONTRIBUTING.md](CONTRIBUTING.md). Corrections are made on the site and mirrored here as a new version, never edited in place in this repository.

Written and edited by Jake Lawrence. Published at [jakelawrence.xyz](https://jakelawrence.xyz).
