---
name: library-testing
description: Use when the user asks to audit a source library component such as HTTP, sockets, crypto, or protocol handling for reachable vulnerabilities.
---

# Library Testing

This skill audits source-code libraries by component, focusing on reachable sinks and behavior under structured harnesses.

## Scope
- Analyze only the requested component or subsystem.
- Use the minimum required context and call graph before deeper analysis.
- Validate every candidate through harness execution.

## Techniques
- Repository graph and AST analysis
- Hybrid SAST and sink triage
- Component-specific fuzzing and harness construction
- Refute-first verification against the pinned library revision

## Safety
- Verify all findings with a reproducing harness or sandbox run before reporting.
