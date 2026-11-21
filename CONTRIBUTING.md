# Contributing

Thank you for reading closely. Corrections are the most useful thing anyone
sends.

## Reporting a correction

Open an issue: https://github.com/jake0lawrence/soc2-readiness/issues

Say which file and which control (the `id` in the data files is enough), what
is wrong, and how you know: a statute, a framework's own text, a control you
have run, a link that does not open. A wrong or missing mapping, a sentence
that overstates, a broken link, a README that says something the file does not:
all welcome.

## Why corrections are not made in this repository

The files here are generated. SOC 2 Readiness for a One-Person Platform is written and versioned on its own
site (https://jakelawrence.xyz/research/soc2-readiness), each version is frozen there with checksums, and this
repository is regenerated from those releases. A released file is never edited
in place: a correction is made on the site, released as a new version folder,
and mirrored here, and the old version stays for anyone who cited it. So a pull
request that edits a file here cannot be merged as it is, but it is a perfectly
good way to show a correction; it will be read like an issue.

## Forking

Fork freely under the license in LICENSE.md (CC BY 4.0: keep the attribution,
say what you changed). Run `python3 scripts/verify.py` after copying to confirm
you have the releases intact.

## Running the check

```
python3 scripts/verify.py
```

checks every file of every version against its `SHA256SUMS` and `manifest.json`,
using only the Python standard library. It runs on every push
([.github/workflows/verify.yml](.github/workflows/verify.yml)).
