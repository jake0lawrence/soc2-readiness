#!/usr/bin/env python3
"""Check every frozen release in this repository against its own checksums.

    python3 scripts/verify.py

For each release folder under downloads/<piece>/v<version>/: every line of
SHA256SUMS must match its file byte for byte, every file the release's
manifest.json lists under "sha256" must match, the manifest's version must be
the folder's, each latest.json must point at a folder that exists, and the
version in the root CITATION.cff must be the one latest.json names. Prints one
line per folder and exits non-zero on any mismatch. Needs nothing but the
Python standard library.

A released version is never edited here: a correction is a new version folder
and latest.json moves. So a mismatch means the copy you have is not the release.
"""

import hashlib
import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DL = os.path.join(ROOT, "downloads")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def manifest_hashes(m):
    """The {file: sha256} map a release manifest carries under "sha256"."""
    table = m.get("sha256") if isinstance(m, dict) else None
    if not isinstance(table, dict):
        return {}
    return {name: h for name, h in table.items() if isinstance(h, str)}


def main():
    if not os.path.isdir(DL):
        print(f"no releases at {DL}")
        return 1
    problems, folders, checked, latest_seen = [], 0, 0, []
    for dirpath, _dirs, names in sorted(os.walk(DL)):
        rel = os.path.relpath(dirpath, DL)
        if "latest.json" in names:
            with open(os.path.join(dirpath, "latest.json"), encoding="utf-8") as fh:
                latest = json.load(fh)
            latest_seen.append(latest["latest"])
            if not os.path.isdir(os.path.join(dirpath, latest["latest"])):
                problems.append(f"{rel}/latest.json points at {latest['latest']}, which is not here")
        if "SHA256SUMS" not in names:
            continue
        folders += 1
        n = 0
        with open(os.path.join(dirpath, "SHA256SUMS"), encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                want, name = line.split(None, 1)
                name = name.lstrip("*")
                path = os.path.join(dirpath, name)
                n += 1
                if not os.path.exists(path):
                    problems.append(f"{rel}/{name}: listed in SHA256SUMS, missing")
                elif sha256(path) != want:
                    problems.append(f"{rel}/{name}: does not match SHA256SUMS")
        if "manifest.json" in names:
            with open(os.path.join(dirpath, "manifest.json"), encoding="utf-8") as fh:
                m = json.load(fh)
            if m.get("version") and "v" + str(m["version"]) != os.path.basename(dirpath):
                problems.append(f"{rel}/manifest.json: version {m['version']} is not this folder's")
            for name, want in manifest_hashes(m).items():
                path = os.path.join(dirpath, name)
                if not os.path.exists(path):
                    problems.append(f"{rel}/{name}: listed in manifest.json, missing")
                    continue
                n += 1
                if sha256(path) != want:
                    problems.append(f"{rel}/{name}: does not match manifest.json")
        checked += n
        print(f"{rel}: {n} checks")
    cff = os.path.join(ROOT, "CITATION.cff")
    if os.path.exists(cff) and latest_seen:
        with open(cff, encoding="utf-8") as fh:
            found = re.search(r"^version:\s*(\S+)\s*$", fh.read(), re.M)
        if not found or "v" + found.group(1) not in latest_seen:
            problems.append(f"CITATION.cff names version {found.group(1) if found else 'none'}, but latest.json names {', '.join(latest_seen)}")
    for p in problems:
        print("FAIL " + p)
    print(f"{folders} release folders, {checked} checks, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
