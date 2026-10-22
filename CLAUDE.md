# AI Security Workflow Plugin

This repository is a portable AI security testing plugin designed for use with Claude Code, GitHub Copilot CLI, and OpenClaw.

## Operating Rules
- Follow the engagement scope and authorization file before running any active testing.
- Use the sandbox gate and verification step before reporting findings.
- Do not run destructive tests without explicit allowlisting and a valid sandbox profile.
- Prefer scoped discovery, evidence-backed hypotheses, and refute-first verification.
- Treat all untrusted binaries or firmware as read-only until hash-pinned and validated in a disposable environment.

## Supported Domains
- Web testing
- IoT and embedded testing
- Supply chain analysis
- Network reconnaissance and service testing
- Reverse engineering and firmware triage
- Library source audit

## MCP Integration
- Burp MCP: for HTTP and application traffic analysis
- Ghidra MCP: for binary and firmware decompilation
- Nmap MCP: for network discovery and service fingerprinting

## General agent behavior
- Validate target scope before all actions.
- Log exact evidence for every finding.
- Suppress unverified hypotheses.
- Keep the workflow modular by domain and by component.
- Use the `skills/` directory as the canonical task orchestration layer.

## Safety Notes
- Network exposure is disabled by default for triage and verification.
- Write access is off by default unless explicitly approved.
- Hash-pinning is required for all binaries and firmware before analysis.
