---
name: iot-firmware
phase: attack
tools: [binwalk, ghidra-mcp, aflpp, firmadyne]
requires_verification: true
safety: emulation-only
---

# IoT / Embedded Firmware Testing

## Parameters
`engagement_token`, `firmware_image`, `arch`, `emulation_profile`
(`firmadyne`|`qemu-user`), `fuzz_budget_sec`, `network_isolation` (must be true).

## Procedure
1. Extract: `binwalk -eM {firmware_image}`. Record filesystem type and offsets.
2. Identify the network-facing binary set (listen sockets, `httpd`, `upnpd`,
   `telnetd`). Cross-reference with Ghidra call graph via `ghidra-mcp`.
3. Static pass: hardcoded credentials, private keys, `strcpy`/`sprintf` sinks on
   attacker-controlled paths, command-injection `system()`/`popen()` callers.
4. Emulate in `emulation_profile` with `network_isolation=true` — egress blocked,
   inbound only from the harness bridge.
5. Fuzz the identified parsers with AFL++ using LLM-generated seeds from the
   decompiled protocol grammar. Budget: `fuzz_budget_sec`.
6. Triage crashes. A `CONFIRMED` finding needs a crashing input **and** a
   debugger trace showing control of a security-relevant register or return address.

## Hard constraint
Physical-device testing requires a separate skill and separate authorization.
This skill is emulation-only. If a finding depends on real hardware behavior,
mark `REQUIRES_PHYSICAL` and stop.
