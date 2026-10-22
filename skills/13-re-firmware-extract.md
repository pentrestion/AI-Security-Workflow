---
name: re-firmware-extract
phase: attack
domain: reverse-engineering
tools: [binwalk, emba, ghidra-mcp, firmadyne, qemu-user]
requires: [firmware_sha256, arch, emulation_profile]
safety: emulation-only
---

# Firmware Extraction & Analysis

## Parameters
`engagement_token`, `firmware_sha256`, `arch`, `emulation_profile`
(`firmadyne` | `qemu-user`), `network_isolation` (**must be true**),
`filesystem_extract` (bool).

## Procedure
1. `binwalk -eM firmware.bin` — record offsets, filesystem types, and compression.
2. Identify the network-facing binaries and look for config files, secrets, and startup scripts.
3. Static pass via GhidraMCP: hardcoded credentials, private keys, `strcpy` and `sprintf` sinks, and command-execution patterns.
4. Emulate with `network_isolation=true`. Inbound only from the harness bridge.
5. Confirm any secret or vulnerable behavior with emulator output, not by reading a decompiler alone.

## Constraint
Physical-device testing requires separate authorization. This skill is emulation-only.
