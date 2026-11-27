# Plus Agent on QA Bench

Plus Agent is Pluswithai's QA agent; every run used the agent `pluswithai/plus-agent`.

Results of Plus Agent on [QA Bench](https://github.com/momentic-ai/qa-bench), Momentic's open benchmark for QA agents. Every area runs 3 times for 30 minutes; tables are the mean of the runs, as in the benchmark. Mo's numbers are Momentic's published [results/2026-11-02.csv](https://github.com/momentic-ai/qa-bench/blob/main/results/2026-11-02.csv), unchanged (a copy is in [`data/`](data)).

Recompute every number below from the raw files:

```
python3 scripts/verify_scores.py
```

## Summary

| App | Areas | Runs | Plus Agent correct | Mo correct | Plus Agent score | Mo score | Plus Agent precision | Mo precision |
|---|---|---|---|---|---|---|---|---|
| [Gitea](gitea) | 11 | 33 | **133.3** | 85.0 | **254.0** | 192.7 | 78.0 % | 92.4 % |
| [Metabase](metabase) | 4 | 12 | **47.3** | 30.7 | 60.7 | **64.0** | 68.3 % | 82.9 % |
| [Saleor](saleor) | 1 | 3 | **20.7** | 17.0 | 42.0 | **44.0** | 77.5 % | 91.1 % |
| [Twenty](twenty) | 4 | 12 | 34.7 | **44.0** | 41.3 | **84.7** | 57.1 % | 74.6 % |
| **Total** | 20 | 60 | **236.0** | 176.7 | **398.0** | 385.4 | 72.0 % | 85.5 % |

Score = severity sum − incorrect − duplicates (severity 1 cosmetic, 3 functional, 5 broken page or raw error). Precision = correct / (correct + incorrect). Every number includes the review of unmatched findings described in [METHOD.md](METHOD.md); the official grader's numbers before review are in each app's README table and in `judge-verdict.json`.

## Examples from the runs

Five findings the agent reported during the 30-minute runs and the grader confirmed, each with the recording of its reproduction.

**Gitea, Milestones (run 2): a milestone with a blank title is created.** Typing a space as the title shows "The milestone ' ' has been created" and adds nameless rows to the list.

https://github.com/user-attachments/assets/d70bc59d-09ef-43f4-bef6-bfead9a38e40

**Metabase, Dashboards (run 1): the History tab shows the raw word "undefined".** Info → History reads "undefined modified this."

https://github.com/user-attachments/assets/634cd2ff-d7ec-4c8d-a804-60cc722284a8

**Saleor, Vouchers (run 1): the dashboard crashes.** Assigning two categories to a voucher ends on "We've encountered an unexpected error".

https://github.com/user-attachments/assets/38634336-f0af-45be-be8b-4911666a4fcc

**Saleor, Vouchers (run 3): the checklist counts codes twice.** After adding two codes the setup checklist says "4 codes ready".

https://github.com/user-attachments/assets/a5c56fe7-29d0-4cb9-a27f-260a954b4d45

**Twenty, Records & views (run 3): the Kanban board goes blank.** Changing a column's aggregate to Sum empties the whole By Stage board.

https://github.com/user-attachments/assets/b9f6ef3f-0376-450c-a919-2c7f8786a994

## Gitea (11 areas)

| Area | Correct | Incorrect | Score | Score before review | Mo score |
|---|---|---|---|---|---|
| Issues | 10.67 | 5.00 | 17.67 | 16.00 | **36.33** |
| Labels | 10.67 | 1.33 | **22.67** | 14.00 | 4.00 |
| Milestones | 11.00 | 2.33 | 21.33 | 19.00 | **24.00** |
| Notifications | 5.67 | 1.67 | **14.67** | 7.00 | 1.67 |
| Profiles & account settings | 10.67 | 4.00 | **17.33** | 12.67 | 8.67 |
| Pull requests | 7.67 | 3.00 | 15.67 | 11.33 | **16.33** |
| Releases | 19.67 | 5.67 | **34.00** | 34.00 | 23.67 |
| Repository code | 21.33 | 2.00 | **44.33** | 27.33 | 20.67 |
| Repository settings | 11.33 | 2.00 | 26.67 | 19.00 | 26.67 |
| Site administration | 12.00 | 5.33 | **17.67** | 8.67 | 12.67 |
| Wiki | 12.67 | 5.33 | **22.00** | 19.00 | 18.00 |

## Metabase (4 areas)

| Area | Correct | Incorrect | Score | Score before review | Mo score |
|---|---|---|---|---|---|
| Admin | 10.33 | 2.00 | 19.00 | 12.33 | **40.33** |
| Dashboards | 13.33 | 10.67 | **15.00** | 10.00 | 10.00 |
| Data modeling | 18.00 | 7.00 | **16.67** | 10.33 | 10.00 |
| Querying | 5.67 | 2.33 | **10.00** | 2.33 | 3.67 |

Two of the three Admin runs lost most of their time to a test-environment issue (see METHOD.md, Incidents).

## Saleor (1 area)

| Area | Correct | Incorrect | Score | Score before review | Mo score |
|---|---|---|---|---|---|
| Vouchers | 20.67 | 6.00 | 42.00 | 39.00 | **44.00** |

## Twenty (4 areas)

| Area | Correct | Incorrect | Score | Score before review | Mo score |
|---|---|---|---|---|---|
| Record pages & activities | 13.67 | 5.67 | 17.67 | 12.33 | **30.67** |
| Record lists & views | 6.00 | 5.67 | **9.00** | 8.33 | 4.00 |
| Settings & data model | 8.00 | 7.33 | 5.67 | 4.33 | **28.33** |
| Workflows | 7.00 | 7.33 | 9.00 | 6.67 | **21.67** |

## What is here

| Path | Contents |
|---|---|
| [`config/environment.json`](config/environment.json) | Versions: benchmark commit, grader, and the sha256 of every app image. |
| `<app>/runs/<area>/run-N/submission.json` | What was sent to the grader, with the second each finding was reported (all within 1800 s). |
| `<app>/runs/<area>/run-N/judge-verdict.json` | The official grader's scores and per-finding assessment. |
| `<app>/runs/<area>/run-N/run-metadata.json` | Start time, duration, stop reason and credits recorded. |
| `<app>/review/<area>/verdicts.json` | The review of every finding the grader could not match. |
| `<app>/NEW_BUGS.md` | Bugs accepted in review, with severity, reason and source links. |
| `<app>/REJECTED_FINDINGS.md` | Everything counted as incorrect: the grader's known-invalid matches and the review's rejections, with owner overrides. |
| Screenshots and recordings | Each finding was recorded by the agent (screenshots and a reproduction video). They are not in this repository; the three recordings above are examples, and the rest are available on request. The notes in `NEW_BUGS.md` and `review/` describe what they show. |
| [`momentic-format-patch/`](momentic-format-patch) | The accepted and rejected bugs in the benchmark's own label schema, ready to add to `fixtures/web/oss/...`. |
| [`scripts/verify_scores.py`](scripts/verify_scores.py) | Recomputes every table here from the files above (Python standard library only). |

## Cost

Plus Agent's cost is the price a Pluswithai customer pays, in credits at $0.01 each, everything included: the testing team, the verification of every finding, cloud browsers, recordings and storage. Each `run-metadata.json` has the run's credits, split into testing team and verification.

| App | Runs | Credits per run | Credits per correct bug |
|---|---|---|---|
| Gitea | 33 | 1,109 (≈ $11.09) | 92 (≈ $0.92) |
| Metabase | 12 | 1,140 (≈ $11.40) | 96 (≈ $0.96) |
| Saleor | 3 | 1,530 (≈ $15.30) | 74 (≈ $0.74) |
| Twenty | 12 | 1,146 (≈ $11.46) | 132 (≈ $1.32) |

Momentic's figures for the other agents are their usage at list prices.
