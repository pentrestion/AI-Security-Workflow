---
name: reporting
phase: output
inputs: [verified_findings, engagement_metadata]
formats: [sarif, json, html, md]
---

# Reporting

## Parameters
`engagement_token`, `format`, `severity_floor`, `include_poc`, `redact_secrets`
(must be true), `program_template`.

## Procedure
1. Accept only findings carrying a valid verification signature from skill 08.
2. Redact: credentials, tokens, PII, internal hostnames beyond the first label,
   and any data that would identify a third party.
3. Structure each finding: Title / Summary / Affected component / Reproduction
   steps (numbered, from a clean state) / Evidence / Impact / Remediation /
   CVSS / References.
4. Reproduction steps must be executable by a reviewer who was not present.
5. Emit per `program_template` (HackerOne, Bugcrowd, Intigriti, or internal).
6. Write the AI session notes to `cve-reference/{id}/ai-notes.md`: which model,
   which prompts, what it got right, what it hallucinated.

## Constraint
`redact_secrets=true` is not overridable by engagement parameters. If a PoC
cannot be redacted without becoming non-reproducible, describe the technique
and withhold the literal payload.
