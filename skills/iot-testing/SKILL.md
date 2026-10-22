---
name: iot-testing
description: Use when the user asks to analyze firmware, embedded devices, protocol handlers, hardcoded secrets, or memory corruption risk in IoT targets.
---

# IoT Testing

This skill addresses firmware extraction, embedded protocol analysis, and emulated validation for IoT and embedded products.

## Scope
- Validate the firmware hash and target architecture.
- Treat the environment as untrusted and isolated.
- Use emulation-first methods before any live hardware validation.

## Techniques
- Firmware extraction and filesystem analysis
- Protocol parser testing and mutation
- Static analysis for hardcoded secrets and unsafe sinks
- Emulator-based behavior validation

## Safety
- Network must remain disabled unless explicitly approved.
- Physical-device testing requires separate authorization.
