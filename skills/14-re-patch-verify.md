---
name: re-patch-verify
phase: gate
domain: reverse-engineering
tools: [ghidra-mcp, ida-mcp, dd, qemu]
policy: diff-first
---

# Patch Verification

## Parameters
`engagement_token`, `binary_sha256`, `patch_offsets`, `expected_bytes`
(original), `replacement_bytes`, `emulator_profile`.

## Procedure
1. Record original bytes at each `patch_offset` — baseline for diff.
2. Apply patch carefully, then load the binary under emulator.
3. Validate that the expected behavior changes.
4. If the patch does not produce the expected change, revert and record `PATCH_FAILED`.
5. Emit a `patch_report.json` with offsets, before/after bytes, emulator command, and observed output.

## Constraint
Patching is only permitted after a triage + static analysis pair has produced an address-backed hypothesis.
