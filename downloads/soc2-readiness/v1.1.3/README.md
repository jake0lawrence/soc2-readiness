# SOC 2 Readiness for a One-Person Platform, version 1.1.3

A self-assessment of a one-person platform against the AICPA Trust Services Criteria: 23 controls, each graded for design and for operation.

Published 2026-11-21. License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Canonical page: https://jakelawrence.xyz/research/soc2-readiness

> This is a self-assessment, not an audit. Only an independent CPA firm can issue a SOC 2 report, and this platform has not engaged one. Nothing on this page claims compliance.

## Files

- `controls.json`
- `controls.csv`
- `worksheet.md`
- `crosswalk.csv`
- `CITATION.cff`
- `README.md`
- `manifest.json`
- `SHA256SUMS`

`worksheet.md` is the blank-able worksheet. `controls.csv` and `controls.json` hold every control with both grades; `slipped` lists the controls whose operating grade is below the design grade. `crosswalk.csv` (and each control's `crosswalk` in `controls.json`) maps the controls to the NIST Cybersecurity Framework 2.0 and to the CIS Critical Security Controls v8: per mapping the reference, full or partial, a confidence and the reason, and per gap the reason there is no honest fit. NIST outcomes are quoted from NIST's own text; CIS rows carry safeguard titles only, read from CIS's Controls Assessment Specification.

Verify the files with `sha256sum -c SHA256SUMS`.

## Cite as

Lawrence, J. (2026). SOC 2 Readiness for a One-Person Platform (version 1.1.3) [Data set]. https://jakelawrence.xyz/research/soc2-readiness. CC BY 4.0.

## Changes

- 1.1.3 (2026-11-21): Adds a crosswalk: each of the 23 controls names where it falls in the NIST Cybersecurity Framework 2.0, quoting NIST's outcome text, and in the CIS Critical Security Controls v8 by safeguard title, with full or partial fit, a confidence and the reason. Controls with no honest fit say why. Grades are unchanged and were last read on November 20, which stays the as-of date.
- 1.1.2 (2026-11-20): All 23 controls re-read against the run history, grades unchanged. Detection: the gap said the health check had stopped, which stopped being true on October 8; the gap now names what still keeps it partial (how long an outage can go unheard, and one person on the receiving end). Backups: six weekly restore tests have passed since the schedule came back (October 11 to November 15), so the gap now counts them instead of saying there are none. The page no longer says a test fails at the review date; that test was retired on October 16.
- 1.1.1 (2026-10-31): All 23 controls re-read, grades unchanged. Health check cadence: the agent tick that runs the site-health sweep moved from hourly to every three hours (an Actions spend cut), so the status page now reads a check up to three hours old; the evidence line follows the workflow.
- 1.1.0 (2026-10-08): All 23 controls regraded after the July 29 schedule freeze was lifted: 43 scheduled jobs run again. Health check regraded to ready; backups and retention sweeps from gap to partial, because a restored schedule is not yet a period of evidence.
- 1.0.0 (2026-09-23): First assessment: 23 controls across all five Trust Services Categories, graded for design and for operation.
