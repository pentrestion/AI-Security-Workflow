---
name: library-source-audit
phase: attack
target_kind: source
tools: [semgrep, bandit, repo-graph, ast-parser]
requires_verification: true
---

# Library Component Audit (`/http`, `/socket`, `/crypto`, …)

## Parameters
`engagement_token`, `library_root`, `component` (path segment),
`language`, `build_cmd`, `test_cmd`, `sast_ruleset`.

## Procedure
1. Build the two-layer index: file-level graph + function-level call graph
   (`core/repo_graph_builder.py`). Never load the whole repo into context.
2. Run hybrid SAST (`semgrep --config {sast_ruleset}`) to get candidate sinks.
3. For each candidate, pull the **minimum context set**: the sink, its callers
   up to 3 hops, and any config module the call path touches.
4. Reason about reachability: is the sink reachable from the component's public
   API? If not, mark `UNREACHABLE` and deprioritize.
5. Construct a harness under `library-testing/{component}/inputs/harness/` that
   drives the public API into the sink.
6. Run the harness in the sandbox. Capture crash/behavior evidence.
7. `CONFIRMED` requires a reproducing harness committed to the repo.

## Component-specific seeds
- `/http` → raw request fixtures, header corpora, URL parser differentials
- `/socket` → pcap samples, protocol state traces, length-prefix mutations
- `/crypto` → known-answer vectors, padding oracles, nonce-reuse scenarios

## Constraint
Never submit a finding that only exists under a modified build. The harness must
run against the unmodified library at the pinned commit.
