---
name: re-binary-triage
phase: discovery
domain: reverse-engineering
tools: [ghidra-mcp, ida-mcp, rea, file, objdump]
requires: [binary_sha256, analysis_engine, sandbox_vm]
blocks_execution_if: [hash_unpinned, network_enabled, write_access_true]
---

# Binary Triage

## Parameters (all required)
| Parameter | Type | Validation |
|---|---|---|
| `engagement_token` | string | valid, unexpired |
| `binary_sha256` | hex[64] | must match the file on disk |
| `analysis_engine` | enum | `ghidra`, `ida`, `binaryninja`, `radare2`, `rea` |
| `sandbox_vm` | string | disposable VM ID, snapshot taken |
| `network_enabled` | bool | **must be false** |
| `write_access` | bool | **must be false** for triage |
| `arch` | string | `x86`, `x64`, `arm`, `arm64`, `mips`, `riscv` |

## Procedure
1. Verify `binary_sha256` matches the artifact. Refuse on mismatch — this is the
   chain-of-custody gate.
2. Confirm `network_enabled=false` and `write_access=false`. Triage is read-only.
3. Run `file`, `objdump -h`, and `strings -n 8`. Record section entropy and
   suspicious strings.
4. Connect to the engine via its MCP bridge and request:
   - exported function list with addresses
   - import table grouped by library
   - cross-references to `recv`, `read`, `system`, `popen`, `strcpy`, `memcpy`
5. Produce a **function map** with addresses. Every claim must cite an address
   and the instruction or string behind it.
6. Flag anti-analysis signals: `ud2`, `int3` sleds, TLS callbacks, `ptrace`
   self-checks, timing loops.
7. **Do not rename, retype, or patch.** Triage is observation only.

## Output schema
```json
{"binary":"","sha256":"","arch":"","entry":"","functions":[{"addr":"","name":"","xrefs":[]}],
 "suspicious_strings":[],"anti_analysis":[],"engine":"","tool_calls":0}
```

Confident-mistake guard

If the agent asserts a function's purpose without an address, the orchestrator
rejects the finding and re-prompts with: "cite the address and the instruction."
Confidence and accuracy are unrelated in this domain.
