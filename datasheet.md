# SOC 2 Readiness for a One-Person Platform

A SOC 2 readiness self-assessment of a one-person web platform against the AICPA Trust Services Criteria, published by Jake Lawrence under CC BY 4.0. Every control is graded twice: once for design, which is what a Type I report tests at one point in time, and once for operation, which is what a Type II report tests across a period. The operating grade falls wherever a control was built and then stopped running, and each control one person cannot satisfy alone (separation of duties, access review, the people controls) carries a note saying so. It is a self-assessment, not an audit and not a SOC 2 report. This record holds one frozen version.

## What it is

- `controls.json`: the same version as data. Every control with its criteria reference, category, both grades, the gap, the one-person note and the file paths of its evidence that the live page shows, plus the tallies, the controls whose operating grade slipped, and the categories.
- `controls.csv`: the controls as one row each, for a spreadsheet.
- `worksheet.md`: the readiness worksheet with all five categories in scope, for another operator to fill in with their own evidence.
- `crosswalk.csv`: where each control falls in the NIST Cybersecurity Framework 2.0 (NIST's outcome quoted verbatim) and in the CIS Critical Security Controls v8 (safeguard titles only, read from CIS's Controls Assessment Specification): per row the reference, full or partial, a confidence and the reason, plus a row for each control with no honest fit and why. From version 1.1.3 on; the same is in each control's `crosswalk` in `controls.json`.
- `CITATION.cff`: how to cite this version, in the Citation File Format.
- `README.md`: the version, the license, the files and how to cite them.
- `manifest.json`: this record's manifest, with the SHA-256 of every file in it. (The website download also carries its own manifest and `SHA256SUMS`; the record's manifest replaces both here.)

## Versions

Each version is frozen when it is published: its files on the website (`/downloads/soc2-readiness/v<version>/`) never change, and a frozen page shows it at `/research/soc2-readiness/v/<version>`. A regrade is a new version, with a changelog entry, and a new version DOI under this record's concept DOI.

## Read with

*Policy as Code, Graded Twice*, a methods preprint by the same author, describes how this self-assessment and the policy template published beside it are kept true to a running system, and what replaying their checks against the site's own history caught and missed. DOI [10.5281/zenodo.24430329](https://doi.org/10.5281/zenodo.24430329), which always resolves to the newest version of the paper.

## What it is not

Not an audit and not a SOC 2 report. Only an independent CPA firm can issue a SOC 2 report, and this platform has not engaged one. Nothing in this record claims compliance.

The live page names the files in the publisher's code behind each control, and a test re-checks them on every change. The paths the page shows are in the data files as they stood at this version; they point into a private repository and can move without a grade changing.
