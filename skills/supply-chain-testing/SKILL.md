---
name: supply-chain-testing
description: Use when the user asks to audit dependencies, lockfiles, package provenance, typosquatting, or build-system trust issues.
---

# Supply Chain Testing

This skill covers dependency resolution, package provenance checks, ecosystem reachability analysis, and malicious or vulnerable dependency chains.

## Scope
- Validate manifest and dependency graph scope.
- Prefer transitive dependency analysis over blind scanning.
- Use OSV and package metadata as evidence, not proof of exploitability.

## Techniques
- Manifest parsing and lockfile review
- Dependency confusion and typosquat checks
- Reachability analysis and import-path validation
- Build sandboxing and provenance review

## Safety
- Build execution is disabled by default unless explicitly allowed and sandboxed.
