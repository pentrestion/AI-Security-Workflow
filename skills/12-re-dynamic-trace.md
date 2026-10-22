---
name: re-dynamic-trace
phase: attack
domain: reverse-engineering
tools: [frida-mcp, gdb, strace, dtrace, rea]
requires: [binary_sha256, sandbox_vm, target_process]
blocks_execution_if: [network_enabled, host_mounts_present]
---

# Dynamic Tracing

## Parameters
`engagement_token`, `binary_sha256`, `target_function` (address or symbol),
`trace_backend` (`frida` | `gdb` | `strace` | `dtrace`), `duration_sec`,
`capture_args` (bool), `capture_return` (bool).

## Procedure
1. Confirm the sandbox VM has **no host mounts** and `network_enabled=false`.
2. Spawn the target under the tracer.
3. Trace `target_function`: arguments, return value, syscalls, and memory writes.
4. Correlate runtime behavior with static analysis. If inconsistent, record a contradiction.
5. For `/socket` and `/http` components, capture protocol bytes and feed them back as harness seeds.
6. Use `strace` for syscall-level behavior; Frida for user-space hook observation.

## Constraint
Never trace on the host. Tracing requires a disposable VM and no host mounts.
