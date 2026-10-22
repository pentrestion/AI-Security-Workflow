---
name: supply-chain
phase: attack
tools: [osv-lookup, manifest-parser, ast-parser, sigstore-verify]
writes_to: attack_graph
---

# Supply Chain Testing

## Parameters
`engagement_token`, `manifest_paths`, `ecosystems`, `allow_build_exec` (bool),
`depth`.

## Procedure
1. Parse manifests and lockfiles for each ecosystem in `ecosystems`.
2. Resolve the full transitive graph; record resolved versions, not ranges.
3. Query OSV.dev for each resolved `(ecosystem, package, version)`.
4. **Reachability filter:** for each vulnerable dependency, AST-check whether the
   vulnerable symbol is actually imported and called. Downgrade unreachable
   findings to `INFORMATIONAL`.
5. Check for: dependency confusion (internal namespace published publicly),
   typosquat neighbors, maintainer changes on critical paths, missing
   signature/provenance.
6. Emit an attack graph where nodes are packages and edges are
   `depends_on | typosquat_of | same_maintainer`.

## Constraint
`allow_build_exec=false` by default. If true, builds run only in the sandbox with
`--network=none` after dependency resolution is complete and vendored.
Never execute a package's `postinstall`/`setup.py` outside the sandbox.
