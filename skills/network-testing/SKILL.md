---
name: network-testing
description: Use when the user asks to perform network footprinting, service enumeration, exposed ports, default credentials, or configuration review.
---

# Network Testing

This skill performs sanctioned network discovery and service validation for in-scope targets.

## Scope
- Validate target CIDR range and service allowlist.
- Keep rate limits and concurrency under control.
- Avoid destructive probes or password spraying.

## Techniques
- Port and service scanning
- Banner and technology fingerprinting
- Default credential checking from approved lists only
- Configuration review and service hardening assessment

## Safety
- Do not run DoS sequences, floods, or unrestricted credential attacks.
