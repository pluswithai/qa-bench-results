# Method

## Runs

- **Benchmark:** QA Bench at upstream commit `809ab59` (Momentic's published results were graded at `e77c72b`; the label counts are the same). One change in our fork: the official grader can reach its model through an OpenAI-compatible gateway (`QA_BENCH_GRADER_BASE_URL`). The grading prompt and model are unchanged; `grading_method_sha256` in every `judge-verdict.json` matches the benchmark's.
- **Apps:** the benchmark's own images, pinned by sha256 (see [`config/environment.json`](config/environment.json)), with the benchmark's seed data. Each run gets a fresh copy in its own E2B sandbox.
- **Agent:** the same agent (prompts, skills and models) for every run, run as a customer would run it, on the Team plan. No rules about the apps were given, as the benchmark requires.
- **Time:** 30 minutes per run, strictly; only findings reported within them count (`reported_at_seconds` in each `submission.json`).
- **Repetitions:** every area three times; tables report the mean, as the benchmark does. A run that ended without writing a report (an infrastructure failure) was repeated and not counted.

## What was sent to the grader

Plus Agent labels each finding itself during the run: bug, intended behavior, test environment, not reproduced, or duplicate. Only findings it labeled as bugs were sent to the grader (`submission.json`). The rule is part of the benchmark adapter and was fixed before the first series.

## Grading

The official grader (`--grade-only`) scored every run against the benchmark's labels. A finding that matches a confirmed bug is correct with that bug's severity (1, 3 or 5); one that matches a known-invalid claim is incorrect; a second report of the same bug is a duplicate; anything else is unmatched. Score = severity sum − incorrect − duplicates.

## Review of unmatched findings

The benchmark's labels were built from the findings of the agents Momentic ran: for Mo, Momentic reviewed the unmatched findings by hand and added the real ones to the labels. An agent that finds different bugs therefore starts with more unmatched findings. We reviewed ours the same way:

1. Only findings the official grader left unmatched were reviewed. Duplicates were grouped into one bug per area.
2. An independent reviewer model, Claude Fable 5.2, judged each bug against its screenshots, video frames, reproduction video and the app's source at the benchmark's version, and proposed accept or reject, a severity and a reason. It did not see the labels.
3. We went through every verdict and changed the ones we disagreed with, some after checking them by hand on a clean copy of the app. Each published verdict carries the reason behind the final call.
4. In each run, an accepted bug counts as correct with its severity, a rejected one as incorrect, and a second report of the same bug in the same run as a duplicate.

Addresses and parameters the app does not generate itself (typed or edited by the agent) are treated as input, as in [OWASP WSTG-ERRH-01](https://wstg.owasp.org/latest/4-Web_Application_Security_Testing/08-Error_Handling/01-Improper_Error_Handling/): if the app breaks on them (error page, blank page, endless loading, raw error), the finding counts; if it handles them (a default view, a redirect or a not-found message), it does not. A response that comes from the test sandbox's proxy rather than from the app is a test-environment effect.

## Incidents

These runs are counted as they are.

- **Metabase, Admin, runs 1 and 3:** at minutes 7.7 and 6.0 the agent turned on *Redirect to HTTPS*. Behind the benchmark sandbox's TLS proxy this put Metabase in a redirect loop, so the instance was unreachable for the rest of the run; on a correctly deployed instance the setting works. Most findings of those runs could not be reproduced and were labeled "not reproduced" by the agent.
- **Gitea, Repository settings, run 2, and Metabase, Querying, run 2:** some of the team's containers could not start because our dev environment reached its container limit, so those runs had 3 and 6 testers instead of 15. `team_container_errors` in `run-metadata.json` records it.
- **Saleor, Vouchers:** the area where we tried the agent before freezing the version. General changes to the agent came out of those trials; the counted series ran after the freeze.

## Reproducing

`node src/agents/pluswithai/bench-series.mjs --name <series> --fixtures <app> --runs 3` in our fork runs a series with a Pluswithai account, and `pnpm eval --agent pluswithai --fixtures <fixture> --grade-only --run-id <id>` grades a run with the official grader.
