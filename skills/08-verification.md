---
name: verification
phase: gate
blocks: [reporting]
policy: refute-first
---

# Verification Gate

## Parameters
`engagement_token`, `candidate_set`, `sandbox_profile`, `repro_attempts` (≥2),
`require_poc` (default true).

## Procedure
1. For each candidate, attempt to **disprove** it first. Actively look for the
   benign explanation: caching, WAF behavior, test data, non-production config.
2. Re-run the candidate `repro_attempts` times in a fresh sandbox instance each
   time. Non-deterministic results → `FLAKY`, not `CONFIRMED`.
3. `CONFIRMED` requires all of:
   - a reproducing artifact (request log, harness, or crashing input)
   - deterministic across attempts
   - a stated impact that follows from the artifact
   - a CVSS vector with justification per metric
4. Anything failing the gate is written to `findings/suppressed/` with the
   refutation reason. Suppressed findings are valuable — they train the
   hypothesis engine.
5. Emit the verified set to `reporting`.

## Output
```json
{"confirmed":[...],"suppressed":[{"id":"","refutation":"","evidence_hash":""}]}
```

Rationale

An unverified finding costs more than a missed one: it burns researcher time,
damages credibility with the program, and poisons the memory module. The gate
exists to make the agent's output trustworthy, not to make it look productive.
