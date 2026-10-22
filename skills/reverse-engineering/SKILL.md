---
name: reverse-engineering
description: Use when the user asks to reverse engineer a binary, firmware image, or protocol handler and needs static triage, decompilation, or emulator validation.
---

# Reverse Engineering

This skill handles binary triage, static analysis, emulation, firmware extraction, and patch verification for approved reverse engineering tasks.

## Scope
- Hash-pin all target artifacts before analysis.
- Work in a disposable VM with network disabled.
- Treat all code as untrusted and potentially malicious.

## Techniques
- Function mapping and imports analysis
- String and anti-analysis inspection
- Decompilation and symbol recovery
- Dynamic tracing and emulator validation
- Firmware extraction and root cause verification

## Safety
- Read-only triage is mandatory by default.
- Patch and write-back operations require a validated hypothesis and emulator check.
