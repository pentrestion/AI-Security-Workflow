---
name: re-static-decompile
phase: attack
domain: reverse-engineering
tools: [ghidra-mcp, ida-mcp, binaryninja-mcp, kong]
requires: [binary_sha256, function_addresses, calling_context]
requires_verification: false
---

# Static Decompilation & Symbol Recovery

## Parameters
`engagement_token`, `binary_sha256`, `function_addresses` (list from skill 10),
`context_depth` (1–3 hops), `write_back` (bool, default false),
`naming_convention` (`snake_case` | `hungarian` | `pascal`).

## Procedure
1. For each target address, pull **minimum context**: the function, its callers
   up to `context_depth`, callees, and any string/data references in the call path.
2. Decompile with the engine's tool call (`decompile_function` or equivalent).
3. Identify known patterns first: CRC loops, string decoders, licence checks,
   crypto constants, and local path validation.
4. Propose names and types only for functions where decompilation supports the inference.
5. If `write_back=true`, apply renames/types through the engine's write API. If the engine is read-only, emit a patch proposal JSON.
6. Do not claim behavior equivalence from decompiler text alone; confirm with execution evidence.

## Output
```json
{"functions":[{"addr":"","proposed_name":"","type":"","evidence":"","calls":[]}],
 "known_signatures":[],"write_back_applied":false,"patch_proposals":[]}
```
