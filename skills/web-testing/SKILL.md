---
name: web-testing
description: Use when the user asks to test for SQL injection, XSS, SSRF, IDOR, request smuggling, or authentication weaknesses in a web application.
---

# Web Testing

This skill covers web application attack surface mapping, mutation-based testing, and validation of candidate findings.

## Scope
- Validate the engagement and authorization context first.
- Limit testing to the approved target list.
- Prefer evidence-backed discovery over speculative findings.

## Techniques
- Endpoint mapping and traffic analysis
- Parameter tampering and structured payload generation
- Playbook-based validation for SQLi, XSS, SSRF, request smuggling, and auth issues
- Refute-first verification in a sandboxed environment

## Safety
- Do not run destructive verbs without explicit scope and allowlisting.
- Use sandbox execution for all exploit verification.
