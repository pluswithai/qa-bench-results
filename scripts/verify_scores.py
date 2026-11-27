#!/usr/bin/env python3
"""Recompute every published table from the raw files in this repository.

For each app, area and run it reads the official grader's verdict (judge-verdict.json) and applies the review
(review/<area>/verdicts.json) exactly as METHOD.md describes:

  - only findings the official grader left unmatched are reviewed (unverified, and not matched outside the area);
  - an accepted bug counts as correct with its severity, a rejected one as incorrect;
  - a second report of the same bug in the same run is a duplicate; "unsure" bugs count for nothing.

Score = severity sum - incorrect - duplicates. Areas are the mean of their runs; apps and the total are sums of
area means, as in the benchmark. Precision = correct / (correct + incorrect). Recall uses the area's labeled bugs
plus the new bugs the review accepted. Mo's rows come from Momentic's published results, unchanged.

Usage: python3 scripts/verify_scores.py
"""
import csv
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS = [("gitea", "Gitea"), ("metabase", "Metabase"), ("saleor", "Saleor"), ("twenty", "Twenty")]
# Area folder -> area name in Momentic's results CSV.
AREA_NAMES = {
    "issues": "Issues", "labels": "Labels", "milestones": "Milestones", "notifications": "Notifications",
    "profiles-account-settings": "Profiles & account settings", "pull-requests": "Pull requests", "releases": "Releases",
    "repository-code": "Repository code", "repository-settings": "Repository settings",
    "site-administration": "Site administration", "wiki": "Wiki",
    "admin": "Admin", "dashboards": "Dashboards", "data-modeling": "Data modeling", "querying": "Querying",
    "vouchers": "Vouchers",
    "records-views": "Record lists & views", "record-pages-activities": "Record pages & activities",
    "settings-data-model": "Settings & data model", "workflows": "Workflows",
}


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def momentic_mo():
    rows = {}
    with open(os.path.join(ROOT, "data", "momentic-results-2026-11-02.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["Agent"] == "Mo" and r["Effort"] == "30 min":
                rows[(r["App"], r["Area"])] = (float(r["Correct"]), float(r["Incorrect"]), float(r["Score"]))
    return rows


def area_result(app_dir, area):
    runs_dir = os.path.join(app_dir, "runs", area)
    runs = sorted(d for d in os.listdir(runs_dir) if d.startswith("run-"))
    vpath = os.path.join(app_dir, "review", area, "verdicts.json")
    bugs = load(vpath)["bugs"] if os.path.exists(vpath) else []
    official = {"correct": 0.0, "incorrect": 0.0, "dup": 0.0, "score": 0.0}
    reviewed = {"correct": 0.0, "incorrect": 0.0, "dup": 0.0, "score": 0.0}
    labels = None
    for run in runs:
        n = int(run.split("-")[1])
        v = load(os.path.join(runs_dir, run, "judge-verdict.json"))
        s = v["scores"]
        c, i, d, sc = int(s["known_hits"]), int(s["known_invalid"]), int(s["duplicates"]), float(s["score"])
        labels = int(s["ground_truth"])
        outside = {x["findingIndex"] for key in ("knownHits", "knownInvalid") for x in (v.get("outsideArea") or {}).get(key, [])}
        unmatched = {x["findingIndex"] for x in v["assessment"].get("unverified", [])} - outside
        ac = ai = ad = sev = 0
        for b in bugs:
            if b["verdict"] == "unsure":
                continue
            seen = False
            for f in b["findings"]:
                m = re.match(r"run(\d+)-(\d+)$", f)
                if int(m.group(1)) != n or int(m.group(2)) - 1 not in unmatched:
                    continue
                if seen:
                    ad += 1
                    continue
                seen = True
                if b["verdict"] == "accept":
                    ac += 1
                    sev += b["severity"]
                else:
                    ai += 1
        for k, val in (("correct", c), ("incorrect", i), ("dup", d), ("score", sc)):
            official[k] += val / len(runs)
        for k, val in (("correct", c + ac), ("incorrect", i + ai), ("dup", d + ad), ("score", sc + sev - ai - ad)):
            reviewed[k] += val / len(runs)
    new_bugs = sum(1 for b in bugs if b["verdict"] == "accept")
    return official, reviewed, labels, new_bugs, len(runs)


def pct(a, b):
    return f"{100 * a / b:.1f} %" if b else "-"


def main():
    mo = momentic_mo()
    grand = {"c": 0.0, "i": 0.0, "s": 0.0, "mc": 0.0, "mi": 0.0, "ms": 0.0, "areas": 0, "runs": 0}
    for app, name in APPS:
        app_dir = os.path.join(ROOT, app)
        if not os.path.isdir(os.path.join(app_dir, "runs")):
            continue
        print(f"\n{name}")
        print(f"{'Area':32} {'Runs':>4} {'Correct':>8} {'Incorr.':>8} {'Score':>7} {'Official':>9} {'Mo score':>9}")
        t = {"c": 0.0, "i": 0.0, "s": 0.0, "os": 0.0, "lab": 0, "mc": 0.0, "mi": 0.0, "ms": 0.0}
        for area in sorted(os.listdir(os.path.join(app_dir, "runs"))):
            off, rev, labels, nb, runs = area_result(app_dir, area)
            mc, mi, ms = mo.get((name, AREA_NAMES[area]), (0.0, 0.0, 0.0))
            print(f"{area:32} {runs:>4} {rev['correct']:>8.2f} {rev['incorrect']:>8.2f} {rev['score']:>7.2f} {off['score']:>9.2f} {ms:>9.2f}")
            t["c"] += rev["correct"]; t["i"] += rev["incorrect"]; t["s"] += rev["score"]; t["os"] += off["score"]
            t["lab"] += labels + nb; t["mc"] += mc; t["mi"] += mi; t["ms"] += ms
            grand["areas"] += 1; grand["runs"] += runs
        print(f"{'Total':32} {'':>4} {t['c']:>8.2f} {t['i']:>8.2f} {t['s']:>7.2f} {t['os']:>9.2f} {t['ms']:>9.2f}")
        print(f"  precision {pct(t['c'], t['c'] + t['i'])} (Mo {pct(t['mc'], t['mc'] + t['mi'])}), recall {pct(t['c'], t['lab'])}")
        for k in ("c", "i", "s", "mc", "mi", "ms"):
            grand[k] += t[k]
    print(f"\nAll apps: {grand['areas']} areas, {grand['runs']} runs")
    print(f"  Pluswithai: correct {grand['c']:.2f}, incorrect {grand['i']:.2f}, score {grand['s']:.2f}, precision {pct(grand['c'], grand['c'] + grand['i'])}")
    print(f"  Mo:         correct {grand['mc']:.2f}, incorrect {grand['mi']:.2f}, score {grand['ms']:.2f}, precision {pct(grand['mc'], grand['mc'] + grand['mi'])}")


if __name__ == "__main__":
    main()
